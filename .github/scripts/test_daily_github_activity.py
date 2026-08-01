import unittest
from datetime import date
from zoneinfo import ZoneInfo

from daily_github_activity import render_report, summarize_events


TIMEZONE = ZoneInfo("Asia/Shanghai")
TARGET_DATE = date(2026, 7, 31)


def event(event_type, created_at, repo, payload):
    return {
        "type": event_type,
        "created_at": created_at,
        "repo": {"name": repo},
        "payload": payload,
    }


class DailyGitHubActivityTest(unittest.TestCase):
    def test_groups_pushes_and_uses_shanghai_day_boundary(self):
        events = [
            event(
                "PushEvent",
                "2026-07-31T15:59:00Z",
                "willwang2528/project",
                {"ref": "refs/heads/main", "distinct_size": 2},
            ),
            event(
                "PushEvent",
                "2026-07-30T16:00:00Z",
                "willwang2528/project",
                {"ref": "refs/heads/main", "distinct_size": 1},
            ),
            event(
                "PushEvent",
                "2026-07-31T16:00:00Z",
                "willwang2528/project",
                {"ref": "refs/heads/main", "distinct_size": 99},
            ),
        ]

        lines = summarize_events(events, TARGET_DATE, TIMEZONE, "willwang2528/profile")

        self.assertEqual(lines, ["willwang2528/project：向 main 推送 3 个提交"])

    def test_excludes_the_daily_automation_pr(self):
        events = [
            event(
                "PullRequestEvent",
                "2026-07-31T01:00:00Z",
                "willwang2528/profile",
                {
                    "action": "opened",
                    "pull_request": {
                        "number": 42,
                        "title": "chore: add GitHub activity for 2026-07-30",
                        "head": {"ref": "automation/daily-github-activity-2026-07-30"},
                    },
                },
            )
        ]

        lines = summarize_events(events, TARGET_DATE, TIMEZONE, "willwang2528/profile")

        self.assertEqual(lines, [])
        self.assertEqual(render_report(TARGET_DATE, lines), "2026-07-31\n无\n")

    def test_excludes_comments_on_the_daily_automation_pr(self):
        events = [
            event(
                "IssueCommentEvent",
                "2026-07-31T01:00:00Z",
                "willwang2528/profile",
                {
                    "action": "created",
                    "issue": {
                        "number": 42,
                        "title": "chore: add GitHub activity for 2026-07-30",
                        "pull_request": {"url": "https://api.github.com/example"},
                    },
                },
            )
        ]

        lines = summarize_events(events, TARGET_DATE, TIMEZONE, "willwang2528/profile")

        self.assertEqual(lines, [])

    def test_formats_a_pull_request(self):
        events = [
            event(
                "PullRequestEvent",
                "2026-07-31T02:00:00Z",
                "openai/example",
                {
                    "action": "opened",
                    "pull_request": {"number": 7, "title": "Make the report concise"},
                },
            )
        ]

        lines = summarize_events(events, TARGET_DATE, TIMEZONE, "willwang2528/profile")

        self.assertEqual(lines, ["openai/example：创建 PR #7「Make the report concise」"])


if __name__ == "__main__":
    unittest.main()
