# Learnings

## [LRN-20260730-001] correction

**Logged**: 2026-07-30T16:38:22+08:00
**Priority**: high
**Status**: pending
**Area**: docs

### Summary

Profile content represents the author's internalized knowledge and must not be expanded by the assistant.

### Details

The author supplies the complete substantive content. Assistance should be limited to information hierarchy, typography, Markdown/VitePress formatting, and link consistency unless the author explicitly requests new content.

### Suggested Action

Preserve the author's wording and scope when editing profile pages; do not add explanations, research opinions, or inferred sections.

### Metadata

- Source: user_feedback
- Related Files: docs/
- Tags: content-ownership, formatting, profile

---

## [LRN-20260804-001] correction

**Logged**: 2026-08-04T14:22:34+08:00
**Priority**: high
**Status**: pending
**Area**: infra

### Summary

A workflow whose goal is to maintain a user's GitHub contribution streak must attribute commits to that user's GitHub-linked email, not to `github-actions[bot]`.

### Details

The daily activity workflow originally configured Git author and committer metadata as `github-actions[bot]`. Although the workflow wrote a file to `main` every day, those commits were not attributed to `willwang2528`. GitHub contribution credit requires the commit email to be associated with the intended account and the commit to be on the default or `gh-pages` branch.

### Suggested Action

Configure both Git author and committer as `Will Wang <willwang2528@users.noreply.github.com>`, verify both emails before pushing, and keep the daily commit on `main`.

### Metadata

- Source: user_feedback
- Related Files: .github/workflows/daily-github-activity.yml
- Tags: github-actions, contribution-attribution, git-identity, cron

---
