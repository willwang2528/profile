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
