#!/usr/bin/env python3
"""Write a concise daily summary of a user's public GitHub activity."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


API_ROOT = "https://api.github.com"
API_VERSION = "2022-11-28"
AUTOMATION_BRANCH_PREFIX = "automation/daily-github-activity-"
AUTOMATION_TITLE_PREFIX = "chore: add GitHub activity for "

Event = dict[str, Any]


def parse_event_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def event_local_date(event: Event, timezone: ZoneInfo) -> date:
    return parse_event_time(event["created_at"]).astimezone(timezone).date()


def fetch_public_events(
    username: str,
    token: str | None,
    target_date: date,
    timezone: ZoneInfo,
) -> list[Event]:
    """Fetch up to GitHub's documented 300-event public timeline limit."""
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "daily-github-activity",
        "X-GitHub-Api-Version": API_VERSION,
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    events: list[Event] = []
    for page in range(1, 4):
        query = urlencode({"per_page": 100, "page": page})
        request = Request(
            f"{API_ROOT}/users/{username}/events/public?{query}",
            headers=headers,
        )
        try:
            with urlopen(request, timeout=30) as response:
                page_events = json.load(response)
        except HTTPError as error:
            detail = error.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"GitHub API returned HTTP {error.code}: {detail}") from error
        except (URLError, TimeoutError) as error:
            raise RuntimeError(f"Could not reach the GitHub API: {error}") from error

        if not isinstance(page_events, list):
            raise RuntimeError("GitHub API returned an unexpected response")

        events.extend(page_events)
        if len(page_events) < 100:
            break
        if page_events and min(event_local_date(event, timezone) for event in page_events) < target_date:
            break

    return events


def is_daily_automation_event(event: Event, target_repository: str) -> bool:
    """Exclude activity created by this workflow's own report branch or PR."""
    if event.get("repo", {}).get("name", "").lower() != target_repository.lower():
        return False

    payload = event.get("payload", {})
    references = [payload.get("ref", "")]
    pull_request = payload.get("pull_request") or {}
    references.append(pull_request.get("head", {}).get("ref", ""))

    if any(str(ref).startswith(AUTOMATION_BRANCH_PREFIX) for ref in references):
        return True

    title = str(pull_request.get("title", ""))
    issue = payload.get("issue") or {}
    issue_title = str(issue.get("title", "")) if issue.get("pull_request") else ""
    return title.startswith(AUTOMATION_TITLE_PREFIX) or issue_title.startswith(
        AUTOMATION_TITLE_PREFIX
    )


def compact_text(value: Any, limit: int = 72) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= limit:
        return text
    return f"{text[: limit - 1].rstrip()}…"


def issue_label(issue: dict[str, Any]) -> str:
    kind = "PR" if issue.get("pull_request") else "Issue"
    number = issue.get("number", "?")
    title = compact_text(issue.get("title"))
    return f"{kind} #{number}「{title}」" if title else f"{kind} #{number}"


def format_event(event: Event) -> str | None:
    event_type = event.get("type", "GitHubEvent")
    repo = event.get("repo", {}).get("name", "未知仓库")
    payload = event.get("payload", {})

    if event_type == "PushEvent":
        return None

    if event_type == "PullRequestEvent":
        pull_request = payload.get("pull_request") or {}
        action = payload.get("action", "更新")
        if action == "closed" and pull_request.get("merged"):
            verb = "合并"
        else:
            verb = {
                "opened": "创建",
                "closed": "关闭",
                "reopened": "重新打开",
                "synchronize": "更新",
                "ready_for_review": "标记为可评审",
                "converted_to_draft": "转为草稿",
            }.get(action, compact_text(action))
        number = pull_request.get("number", payload.get("number", "?"))
        title = compact_text(pull_request.get("title"))
        label = f"PR #{number}「{title}」" if title else f"PR #{number}"
        return f"{repo}：{verb} {label}"

    if event_type == "IssuesEvent":
        action = {
            "opened": "创建",
            "closed": "关闭",
            "reopened": "重新打开",
        }.get(payload.get("action"), compact_text(payload.get("action", "更新")))
        return f"{repo}：{action} {issue_label(payload.get('issue') or {})}"

    if event_type == "IssueCommentEvent":
        action = {
            "created": "评论",
            "edited": "编辑评论",
            "deleted": "删除评论",
        }.get(payload.get("action"), "更新评论")
        return f"{repo}：{action} {issue_label(payload.get('issue') or {})}"

    if event_type == "PullRequestReviewEvent":
        review = payload.get("review") or {}
        state = {
            "approved": "批准评审",
            "changes_requested": "请求修改",
            "commented": "提交评审",
            "dismissed": "撤销评审",
        }.get(str(review.get("state", "")).lower(), "更新评审")
        pull_request = payload.get("pull_request") or {}
        return f"{repo}：{state} {issue_label({**pull_request, 'pull_request': True})}"

    if event_type == "PullRequestReviewCommentEvent":
        pull_request = payload.get("pull_request") or {}
        return f"{repo}：评论 {issue_label({**pull_request, 'pull_request': True})} 的代码"

    if event_type == "CommitCommentEvent":
        commit_id = str((payload.get("comment") or {}).get("commit_id", ""))[:7]
        suffix = f" {commit_id}" if commit_id else ""
        return f"{repo}：评论提交{suffix}"

    if event_type == "CreateEvent":
        ref_type = payload.get("ref_type", "内容")
        ref = compact_text(payload.get("ref"))
        nouns = {"repository": "仓库", "branch": "分支", "tag": "标签"}
        suffix = f" {ref}" if ref else ""
        return f"{repo}：创建{nouns.get(ref_type, ref_type)}{suffix}"

    if event_type == "DeleteEvent":
        ref_type = {"branch": "分支", "tag": "标签"}.get(
            payload.get("ref_type"), payload.get("ref_type", "内容")
        )
        return f"{repo}：删除{ref_type} {compact_text(payload.get('ref'))}"

    if event_type == "ReleaseEvent":
        release = payload.get("release") or {}
        name = compact_text(release.get("name") or release.get("tag_name"))
        return f"{repo}：{compact_text(payload.get('action', '发布'))} Release {name}"

    if event_type == "ForkEvent":
        fork_name = compact_text((payload.get("forkee") or {}).get("full_name"))
        suffix = f" 为 {fork_name}" if fork_name else ""
        return f"{repo}：创建 Fork{suffix}"

    if event_type == "WatchEvent":
        return f"{repo}：添加 Star"

    if event_type == "GollumEvent":
        count = len(payload.get("pages") or [])
        return f"{repo}：更新 {count} 个 Wiki 页面"

    if event_type == "PublicEvent":
        return f"{repo}：将仓库设为公开"

    if event_type == "MemberEvent":
        member = compact_text((payload.get("member") or {}).get("login"))
        return f"{repo}：添加协作者 {member}"

    if event_type == "DiscussionEvent":
        discussion = payload.get("discussion") or {}
        number = discussion.get("number", "?")
        title = compact_text(discussion.get("title"))
        return f"{repo}：{compact_text(payload.get('action', '更新'))} Discussion #{number}「{title}」"

    if event_type == "DiscussionCommentEvent":
        discussion = payload.get("discussion") or {}
        return f"{repo}：评论 Discussion #{discussion.get('number', '?')}"

    readable_type = re.sub(r"Event$", "", str(event_type))
    return f"{repo}：发生 {readable_type} 活动"


def summarize_events(
    events: list[Event],
    target_date: date,
    timezone: ZoneInfo,
    target_repository: str,
) -> list[str]:
    selected = [
        event
        for event in events
        if event_local_date(event, timezone) == target_date
        and not is_daily_automation_event(event, target_repository)
    ]

    pushes: dict[tuple[str, str], int] = defaultdict(int)
    lines: list[str] = []
    for event in reversed(selected):
        if event.get("type") == "PushEvent":
            payload = event.get("payload", {})
            repo = event.get("repo", {}).get("name", "未知仓库")
            ref = str(payload.get("ref", ""))
            branch = ref.removeprefix("refs/heads/") or "未知分支"
            count = payload.get("distinct_size")
            if count is None:
                count = payload.get("size")
            if count is None:
                count = len(payload.get("commits") or [])
            pushes[(repo, branch)] += int(count)
            continue

        line = format_event(event)
        if line:
            lines.append(line)

    push_lines = [
        f"{repo}：向 {branch} 推送 {count} 个提交"
        for (repo, branch), count in sorted(pushes.items())
    ]
    return push_lines + lines


def render_report(target_date: date, lines: list[str]) -> str:
    if not lines:
        return f"{target_date.isoformat()}\n无\n"
    return f"{target_date.isoformat()}\n" + "\n".join(f"- {line}" for line in lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", default=os.getenv("ACTIVITY_USER", "willwang2528"))
    parser.add_argument("--timezone", default=os.getenv("ACTIVITY_TIMEZONE", "Asia/Shanghai"))
    parser.add_argument("--repository", default=os.getenv("TARGET_REPOSITORY", "willwang2528/profile"))
    parser.add_argument("--date", help="Report date in YYYY-MM-DD; defaults to yesterday")
    parser.add_argument("--output-dir", type=Path, default=Path("tmp"))
    parser.add_argument("--events-file", type=Path, help="Read fixture events instead of calling GitHub")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        timezone = ZoneInfo(args.timezone)
    except ZoneInfoNotFoundError as error:
        print(f"error: unknown timezone {args.timezone}", file=sys.stderr)
        return 2

    try:
        target_date = (
            date.fromisoformat(args.date)
            if args.date
            else datetime.now(timezone).date() - timedelta(days=1)
        )
    except ValueError:
        print("error: --date must use YYYY-MM-DD", file=sys.stderr)
        return 2

    try:
        if args.events_file:
            events = json.loads(args.events_file.read_text(encoding="utf-8"))
            if not isinstance(events, list):
                raise RuntimeError("Events fixture must contain a JSON array")
        else:
            events = fetch_public_events(
                args.username,
                os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN"),
                target_date,
                timezone,
            )
        lines = summarize_events(events, target_date, timezone, args.repository)
    except (OSError, ValueError, RuntimeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    args.output_dir.mkdir(parents=True, exist_ok=True)
    output_path = args.output_dir / f"{target_date.isoformat()}.txt"
    output_path.write_text(render_report(target_date, lines), encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
