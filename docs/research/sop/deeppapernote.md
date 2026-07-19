---
title: DeepPaperNote
description: 面向 Claude Code / Codex 的论文精读插件
---

# [DeepPaperNote](https://github.com/917Dhj/DeepPaperNote)

### 介绍

DeepPaperNote 是一个面向 Claude Code / Codex 的论文精读插件，不是普通独立 App。它的目标是：一次处理一篇论文，把论文 PDF / DOI / arXiv / URL / Zotero 条目转成结构化、证据充分、适合长期保存的 Obsidian Markdown 笔记。

核心能力：

- 解析论文身份和元数据
- 获取或复用 PDF
- 抽取正文、章节、证据、图表资源
- 规划图表/表格是否插入笔记
- 生成 synthesis bundle，供模型基于证据写深度笔记
- 对最终笔记做结构、风格、数学公式、图表、grounding 校验
- 保存到 Obsidian vault，或没有 vault 时保存到当前 workspace

### 核心SKILL

- `deeppapernote`：主功能，生成单篇论文深度笔记
- `paper-glossary`：可选 companion skill，从已有论文材料里生成术语笔记

### 待优化点

以下是可选增强，目前没有强制安装：

- OCR：`tesseract`、`pdftoppm`、`pytesseract`、`Pillow`，仅扫描版 PDF 需要
- Semantic Scholar API Key：仅改善部分元数据识别
- Zotero：无需额外安装
