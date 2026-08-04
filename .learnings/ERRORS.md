# Errors

## [ERR-20260730-001] vitepress-build

**Logged**: 2026-07-30T16:27:10+08:00
**Priority**: low
**Status**: resolved
**Area**: docs

### Summary

The documentation build could not start because project dependencies are not installed.

### Error

```text
> docs:build
> vitepress build docs

sh: vitepress: command not found
```

### Context

- Command: `npm run docs:build`
- The repository has `package-lock.json`, but `node_modules/` is absent.
- The attempted build was intended to validate a new VitePress research section.

### Suggested Fix

Run `npm ci`, then retry `npm run docs:build`.

### Metadata

- Reproducible: yes
- Related Files: package.json, package-lock.json

### Resolution

- **Resolved**: 2026-07-30T16:27:10+08:00
- **Notes**: Installed the locked dependencies with `npm ci`; `npm run docs:build -- --base /profile/` then completed successfully.

---

## [ERR-20260730-002] vitepress-dev-sandbox

**Logged**: 2026-07-30T16:38:22+08:00
**Priority**: low
**Status**: resolved
**Area**: docs

### Summary

The local VitePress server could not bind to a port inside the filesystem sandbox.

### Error

```text
listen EPERM: operation not permitted 127.0.0.1:5173
```

### Context

- Command: `npm run docs:dev -- --host 127.0.0.1 --base /profile/`
- The server was needed for a visual formatting check.

### Suggested Fix

Run the local preview with approved elevated permissions.

### Metadata

- Reproducible: yes
- Related Files: package.json

### Resolution

- **Resolved**: 2026-07-30T16:38:22+08:00
- **Notes**: The server started successfully after permission approval.

---

## [ERR-20260730-003] browser-preview

**Logged**: 2026-07-30T16:38:22+08:00
**Priority**: low
**Status**: pending
**Area**: docs

### Summary

No browser instance was available for visual inspection of the local page.

### Error

```text
No browser is available
```

### Context

- Target: `http://127.0.0.1:5173/profile/research/gui-agents/`
- Browser discovery returned an empty list.

### Suggested Fix

Retry visual inspection in a session with an in-app browser or connected Chrome instance.

### Metadata

- Reproducible: unknown
- Related Files: docs/research/gui-agents/index.md

---

## [ERR-20260801-001] macos-python-bytecode-cache

**Logged**: 2026-08-01T10:21:37+08:00
**Priority**: low
**Status**: resolved
**Area**: tests

### Summary

The macOS system Python could not write its redirected bytecode cache inside the filesystem sandbox.

### Error

```text
PermissionError: [Errno 1] Operation not permitted: '/Users/will/Library/Caches/com.apple.python/Users/will/Documents'
```

### Context

- Command: `python3 -m py_compile .github/scripts/daily_github_activity.py .github/scripts/test_daily_github_activity.py`
- The project files are writable, but this Python installation redirects `__pycache__` into `~/Library/Caches/com.apple.python/`.

### Suggested Fix

Set `PYTHONPYCACHEPREFIX` to a writable temporary directory when running bytecode checks in the sandbox.

### Metadata

- Reproducible: yes
- Related Files: .github/scripts/daily_github_activity.py, .github/scripts/test_daily_github_activity.py

### Resolution

- **Resolved**: 2026-08-01T10:21:37+08:00
- **Notes**: Re-run the check with `PYTHONPYCACHEPREFIX` pointing to a directory under `/tmp`.

---

## [ERR-20260801-002] git-push-network-sandbox

**Logged**: 2026-08-01T10:27:33+08:00
**Priority**: low
**Status**: resolved
**Area**: infra

### Summary

An SSH push to GitHub was blocked by the local network sandbox.

### Error

```text
ssh: connect to host github.com port 22: Operation not permitted
fatal: Could not read from remote repository.
```

### Context

- Command: `git push --set-upstream origin codex/daily-github-activity`
- The same SSH remote had worked for clone, confirming the repository and key were valid.

### Suggested Fix

Retry the push with approved network access outside the sandbox.

### Metadata

- Reproducible: yes
- Related Files: .git/config

### Resolution

- **Resolved**: 2026-08-01T10:27:33+08:00
- **Notes**: The push completed successfully with approved network access.

---

## [ERR-20260801-003] zsh-unquoted-api-query

**Logged**: 2026-08-01T10:43:10+08:00
**Priority**: low
**Status**: resolved
**Area**: infra

### Summary

An unquoted GitHub API path containing `?ref=` was interpreted as a zsh glob.

### Error

```text
zsh:1: no matches found: repos/willwang2528/profile/contents/tmp/2026-07-31.txt?ref=automation/daily-github-activity-2026-07-31
```

### Context

- Command: `gh api repos/.../2026-07-31.txt?ref=automation/...`
- zsh expands `?` before passing arguments to `gh`.

### Suggested Fix

Quote API paths that contain query strings.

### Metadata

- Reproducible: yes
- Related Files: .github/workflows/daily-github-activity.yml

### Resolution

- **Resolved**: 2026-08-01T10:43:10+08:00
- **Notes**: Use a quoted endpoint, or verify the merged file from the local checkout.

---

## [ERR-20260804-001] public-commit-page-fetch

**Logged**: 2026-08-04T14:22:34+08:00
**Priority**: low
**Status**: resolved
**Area**: infra

### Summary

The web fetcher could not open a public GitHub commit URL for identity verification.

### Error

```text
Internal Error: URL is not safe to open
Failed to fetch: Cache miss
```

### Context

- Targets: the public REST and HTML URLs for commit `8487c20`.
- The repository clone and official contribution documentation remained available.

### Suggested Fix

Verify attribution using the repository commit metadata and an end-to-end workflow run instead of relying on the web cache.

### Metadata

- Reproducible: unknown
- Related Files: .github/workflows/daily-github-activity.yml

### Resolution

- **Resolved**: 2026-08-04T14:22:34+08:00
- **Notes**: Continue with local metadata validation and verify the resulting commit through GitHub after the workflow runs.

---
