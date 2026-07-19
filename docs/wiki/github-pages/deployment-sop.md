---
title: GitHub Pages 部署 SOP
description: 将 Markdown 文档或静态网页通过 GitHub Pages 发布到公网
outline: deep
---

# GitHub Pages 部署 SOP

> 来源：[飞书原文](https://tcnalm3egehv.feishu.cn/wiki/NEXrw8d7iiA3aSkn00qcPSrqnte)  
> 同步日期：2026-07-19  
> 说明：本站保存公开副本，原文仍是上游来源。

用途：将指定 GitHub 仓库中的 Markdown 文档或静态网页发布到 GitHub Pages，使其可从公网访问。

## 输入

- `REPO`：GitHub 仓库，格式为 `OWNER/REPO`
- `SOURCE_DIR`：待发布目录，例如 `docs`

## 完成条件

1. GitHub Actions 执行成功。
2. GitHub Pages 公网根地址返回 HTTP 200。

## 部署步骤

### 1. 获取默认分支并检查权限

```bash
DEFAULT_BRANCH=$(gh repo view "$REPO" \
  --json defaultBranchRef \
  --jq '.defaultBranchRef.name')

gh repo view "$REPO" \
  --json viewerPermission \
  --jq '.viewerPermission'
```

操作者必须能够修改仓库并管理 GitHub Pages。

### 2. 确认发布目录有首页

如果 `$SOURCE_DIR/index.html` 存在，按静态 HTML 发布。

如果发布 Markdown，必须存在 `$SOURCE_DIR/index.md`。每个需要转换成网页的 Markdown 文件必须以前置元数据开头：

```markdown
---
---
```

### 3. 启用 GitHub Pages

设置 GitHub Actions 为发布来源。先查询：

```bash
gh api "repos/$REPO/pages" --jq '.build_type'
```

如果返回 HTTP 404：

```bash
gh api --method POST \
  "repos/$REPO/pages" \
  -f build_type=workflow
```

如果 Pages 已存在，但 `build_type` 不是 `workflow`：

```bash
gh api --method PUT \
  "repos/$REPO/pages" \
  -f build_type=workflow
```

验证：

```bash
gh api "repos/$REPO/pages" \
  --jq '{build_type,html_url}'
```

`build_type` 必须为 `workflow`。

### 4. 新增 GitHub Actions 工作流

在功能分支创建 `.github/workflows/pages.yml`。

发布 Markdown/Jekyll 文档时写入：

```yaml
on:
  push:
    branches: [DEFAULT_BRANCH]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  pages:
    runs-on: ubuntu-latest
    environment: github-pages
    steps:
      - uses: actions/checkout@v5
      - uses: actions/configure-pages@v5
      - uses: actions/jekyll-build-pages@v1
        with:
          source: ./SOURCE_DIR
          destination: ./_site
      - uses: actions/upload-pages-artifact@v4
        with:
          path: ./_site
      - uses: actions/deploy-pages@v4
```

把 `DEFAULT_BRANCH` 和 `SOURCE_DIR` 替换为实际值。

如果 `$SOURCE_DIR/index.html` 已存在，删除 `actions/jekyll-build-pages` 步骤，并将上传步骤改为：

```yaml
- uses: actions/upload-pages-artifact@v4
  with:
    path: ./SOURCE_DIR
```

### 5. 合入默认分支

提交功能分支，创建 PR，并合并到默认分支。合并后 `pages.yml` 自动触发。

### 6. 验证部署

```bash
RUN_ID=$(gh run list \
  --repo "$REPO" \
  --workflow pages.yml \
  --limit 1 \
  --json databaseId \
  --jq '.[0].databaseId')

gh run watch "$RUN_ID" \
  --repo "$REPO" \
  --exit-status

SITE_URL=$(gh api "repos/$REPO/pages" --jq '.html_url')

curl -fsSL \
  -o /dev/null \
  -w '%{http_code}\n' \
  "$SITE_URL"
```

只有 workflow 成功且公网地址返回 `200`，才报告部署完成并输出 `$SITE_URL`。

## 故障规则

如果 `actions/configure-pages` 报 `Get Pages site failed` 或 HTTP 404，说明 Pages 尚未启用。执行“启用 GitHub Pages”步骤后重新运行 workflow。Node.js deprecation 警告不是该 404 的原因。
