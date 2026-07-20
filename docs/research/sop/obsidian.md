---
title: Obsidian
description: Obsidian 学习记录
---

# 一、Obsidian 是什么？

**Obsidian 是一个以本地 Markdown 文件为基础的知识管理和笔记软件。**

它既可以当作普通的 Markdown 编辑器，也可以把大量笔记通过双向链接连接起来，形成个人知识库。每篇笔记本质上都是一个存储在电脑上的 `.md` 纯文本文件，而不是被锁在某个平台的数据库中。([Obsidian][1])

可以把它理解成：

> **Markdown 编辑器 + 本地文件管理 + 双向链接 + 个人知识库**

例如，你有三篇笔记：

```text
GUI Agent
├── Computer Use Agent
├── GUI Agent Benchmark
└── Multimodal LLM
```

在“GUI Agent”笔记中写：

```md
GUI Agent 通常依赖 [[Multimodal LLM]] 理解界面，
并通过 [[Computer Use Agent]] 执行操作。

目前常用评测方式见 [[GUI Agent Benchmark]]。
```

Obsidian 会识别这些链接，并建立笔记之间的关系。

---

## 二、Obsidian 和普通笔记软件有什么区别？

### 1. 笔记保存在本地

一个 Obsidian 仓库实际上就是电脑上的一个文件夹：

```text
My Research Vault/
├── GUI Agent.md
├── Multimodal LLM.md
├── Papers/
│   └── OSWorld.md
└── Attachments/
    └── architecture.png
```

其中：

* 笔记是 `.md` 文件；
* 图片、PDF等附件也是普通文件；
* 可以使用 Finder、VS Code、Git 或其他工具直接管理；
* 即使以后不使用 Obsidian，Markdown 文件仍然可以打开。

Obsidian 官方将这个知识库文件夹称为 **Vault，即仓库**。([Obsidian][1])

### 2. 强调“链接”，而不只是“文件夹”

传统笔记主要依靠目录：

```text
人工智能/
└── GUI Agent/
    └── Benchmark/
```

但一篇论文可能同时属于：

* GUI Agent；
* 多模态模型；
* Agent 评测；
* Computer Use；
* 强化学习。

只用文件夹，很难同时表达这些关系。

Obsidian 可以通过链接解决：

```md
主题：[[GUI Agent]]
相关方向：[[Multimodal LLM]]、[[Computer Use]]
评测环境：[[OSWorld]]
涉及方法：[[Reinforcement Learning]]
```

Obsidian 支持 Wiki 风格链接 `[[笔记名称]]`，也支持普通 Markdown 链接。重命名笔记时，还可以自动更新内部链接。([Obsidian][2])

### 3. 支持双向链接

假设在 `OSWorld.md` 中写：

```md
OSWorld 是一个 [[GUI Agent Benchmark]]。
```

那么：

* `OSWorld` 指向 `GUI Agent Benchmark`；
* `GUI Agent Benchmark` 的反向链接中，也会显示 `OSWorld`。

因此，你不仅能知道“这篇笔记链接了谁”，还能知道“谁提到了这篇笔记”。

---

# 三、什么是 Markdown 笔记？

Markdown 是一种非常轻量的文本格式。

例如，你输入：

```md
# GUI Agent

## 核心问题

GUI Agent 需要完成以下任务：

- 理解界面
- 制定计划
- 执行动作
- 根据反馈调整

**关键能力**是视觉理解和动作决策。
```

Obsidian 会显示为带有标题、列表和加粗效果的笔记。

Markdown 的特点是：

* 直接使用键盘输入；
* 不需要频繁点击格式按钮；
* 原始文件仍然是可读的纯文本；
* 适合写论文笔记、代码、公式、实验记录和技术文档。

Obsidian 使用 Markdown 作为主要笔记格式，并在标准 Markdown 基础上增加了内部链接、嵌入、标注框和块引用等扩展语法。([Obsidian][3])

---

# 四、如何开始使用 Obsidian？

## 第一步：创建仓库

安装并打开 Obsidian 后：

1. 点击“创建新仓库”；
2. 输入名称，例如：

```text
Research Vault
```

3. 选择电脑上的保存位置；
4. 创建仓库。

建议不要一开始创建多个仓库。

对于科研，先使用一个仓库即可：

```text
Research Vault
```

所有论文、概念、项目和实验记录都放在里面，通过文件夹和链接分类。

---

## 第二步：创建第一篇笔记

使用快捷键：

```text
macOS：Command + N
Windows：Ctrl + N
```

输入笔记名称：

```text
GUI Agent
```

然后开始写 Markdown。Obsidian 官方入门流程同样是先创建仓库，再通过 `Cmd/Ctrl + N` 创建笔记。([Obsidian][4])

---



# 六、Obsidian 最重要的特殊语法

## 1. 链接另一篇笔记

```md
[[GUI Agent]]
```

输入两个左方括号：

```text
[[
```

Obsidian 就会搜索已有笔记。

如果笔记不存在，也可以先写：

```md
[[GUI Grounding]]
```

点击后再创建这篇笔记。

---

## 2. 修改链接显示名称

```md
[[Multimodal Large Language Model|多模态大模型]]
```

实际链接的是：

```text
Multimodal Large Language Model.md
```

但当前笔记中显示：

```text
多模态大模型
```

---

## 3. 链接到某个标题

```md
[[GUI Agent#核心模块]]
```

表示跳转到 `GUI Agent` 笔记中的“核心模块”章节。

显示其他文字：

```md
[[GUI Agent#核心模块|查看 GUI Agent 的组成]]
```

---

## 4. 嵌入另一篇笔记

普通链接：

```md
[[GUI Agent]]
```

只是跳转。

加上感叹号：

```md
![[GUI Agent]]
```

会直接把整篇笔记显示在当前位置。

也可以只嵌入一个章节：

```md
![[GUI Agent#核心模块]]
```

Obsidian 使用 `![[...]]` 语法嵌入笔记、章节、块和附件。([Obsidian][2])

---

## 5. 标签

```md
#GUI-Agent
#论文
#待读
```

也支持层级标签：

```md
#论文/待读
#论文/精读
#论文/已完成
```

但不要给每篇笔记添加十几个标签。

一个实用原则是：

* **文件夹**表示笔记是什么；
* **链接**表示笔记和谁有关；
* **标签**表示当前状态或特殊属性。

例如：

```text
文件夹：Papers
链接：[[GUI Agent]]、[[Benchmark]]
标签：#论文/精读
```

---

## 6. 属性

属性用于为笔记添加结构化信息。

例如一篇论文笔记顶部可以写：

```yaml
---
type: paper
title: "OSWorld"
year: 2024
status: reading
topics:
  - GUI Agent
  - Benchmark
rating: 4
---
```

这些属性可以用于：

* 按年份筛选论文；
* 查找所有待读论文；
* 创建论文表格；
* 按主题统计；
* 建立阅读数据库。

Obsidian 的属性通常存储在 Markdown 文件顶部的 YAML 前置元数据中；当前的 Bases 核心功能也可以依据这些属性建立表格、列表和卡片视图。([Obsidian][7])

---

## 7. 标注框 Callout

```md
> [!note]
> 这是普通备注。

> [!important]
> 这是重要内容。

> [!warning]
> 这里存在实验风险。

> [!question]
> 为什么该方法在跨应用场景下降明显？

> [!tip]
> 阅读实验部分时，优先找到主表和消融实验。
```

科研笔记中很适合统一含义：

```md
> [!abstract]
> 论文核心摘要

> [!question]
> 尚未理解的问题

> [!danger]
> 论文可能存在的缺陷

> [!example]
> 一个具体案例
```

---

## 8. 注释

只在编辑模式中保留，但阅读时不显示：

```md
%%这里是我暂时不想展示的备注%%
```

例如：

```md
%%后续需要验证作者是否公开完整代码%%
```

---

# 七、科研笔记推荐的仓库结构

不建议刚开始就建立几十层目录。

可以使用下面这套结构：

```text
Research Vault/
├── 00 Inbox/
├── 10 Projects/
├── 20 Papers/
├── 30 Concepts/
├── 40 Experiments/
├── 50 Maps/
├── 90 Templates/
└── 99 Attachments/
```

各目录用途如下。

## `00 Inbox`

临时收集，暂未整理：

```text
突然想到的研究点
某篇论文地址
会议中记录的关键词
待处理的截图
```

## `10 Projects`

具体研究项目：

```text
GUI Agent 研究入门
GUI Agent Benchmark 调研
OSWorld 复现
GUI Grounding 实验
```

## `20 Papers`

一篇论文对应一篇 Markdown：

```text
OSWorld.md
WebArena.md
Mind2Web.md
SeeClick.md
```

## `30 Concepts`

概念型笔记：

```text
GUI Grounding.md
Action Space.md
Visual Grounding.md
Chain of Thought.md
Agent Memory.md
```

这里适合保存可以跨论文复用的知识。

## `40 Experiments`

实验日志：

```text
2026-07-19 OSWorld 环境安装.md
2026-07-20 基线模型运行.md
2026-07-21 参数调整记录.md
```

## `50 Maps`

知识地图，也称 MOC，Map of Content：

```text
GUI Agent 知识地图.md
多模态模型知识地图.md
论文阅读索引.md
```

## `90 Templates`

存放论文笔记、概念笔记和实验记录模板。

## `99 Attachments`

存放：

* 图片；
* PDF；
* 截图；
* 数据文件；
* 图表。

然后在设置中把附件默认位置设为：

```text
99 Attachments
```

Obsidian 支持指定统一附件文件夹，也支持把附件放到当前笔记目录或其子目录。([Obsidian][8])

---

# 八、推荐的科研笔记类型

不要把所有内容都写进一篇巨大的笔记。建议至少区分四种笔记。

## 1. 论文笔记

回答：

* 论文解决什么问题？
* 为什么这个问题重要？
* 作者提出了什么方法？
* 实验是否支持结论？
* 有什么缺陷？
* 对自己的研究有什么价值？

## 2. 概念笔记

例如：

```text
GUI Grounding
```

这篇笔记不属于某一篇论文，而是综合多篇论文后形成的知识：

```md
# GUI Grounding

## 定义

GUI Grounding 是将自然语言意图或目标元素映射到界面位置的过程。

## 常见输入

- 截图
- HTML/DOM
- Accessibility Tree
- 自然语言指令

## 常见输出

- 坐标
- Bounding Box
- Element ID

## 相关论文

- [[SeeClick]]
- [[CogAgent]]
- [[Mind2Web]]

## 开放问题

- 跨分辨率泛化
- 小目标识别
- 动态页面变化
```

## 3. 项目笔记

用于统筹一个研究任务：

```md
# GUI Agent Benchmark 调研

## 目标

形成现有 GUI Agent Benchmark 的完整分类。

## 待办

- [ ] 收集桌面端 Benchmark
- [ ] 收集网页端 Benchmark
- [ ] 收集移动端 Benchmark
- [ ] 比较任务环境
- [ ] 比较评测指标

## 核心论文

- [[OSWorld]]
- [[WebArena]]
- [[AndroidWorld]]

## 当前结论

……

## 下一步

……
```

## 4. 实验日志

用于保证实验可以复现：

````md
# 2026-07-19 OSWorld 环境安装

## 实验目标

完成 OSWorld 基础环境安装。

## 环境

- 系统：
- Python：
- CUDA：
- GPU：
- Git commit：

## 执行命令

```bash
conda create -n osworld python=3.11
````

## 结果

* [x] 仓库下载完成
* [ ] 依赖安装完成
* [ ] 第一个任务运行成功

## 错误记录

### 错误一

现象：

原因：

解决：

## 下一步

……

````

---

# 九、论文笔记模板

可以把下面内容保存为：

```text
90 Templates/论文笔记模板.md
````

````md
---
type: paper
title:
authors:
year:
venue:
url:
code:
status: unread
topics:
  -
rating:
created: "{{date:YYYY-MM-DD}}"
---

# {{title}}

## 一句话总结

这篇论文通过……解决了……问题，主要结果是……

## 基本信息

- 论文：
- 作者：
- 会议或期刊：
- 年份：
- 项目主页：
- 代码：
- PDF：

## 研究背景

### 研究领域

这篇论文属于：

- [[]]

### 现有问题

现有方法主要存在：

1.
2.
3.

## Motivation

作者为什么要研究这个问题？

- 实际问题：
- 现有方法不足：
- 论文切入点：

## Research Question

论文真正想回答的问题是：

> 

## 核心贡献

1.
2.
3.

## 方法概览

### 输入

### 输出

### 总体流程

```text
输入
  ↓
感知
  ↓
规划
  ↓
动作生成
  ↓
环境反馈
```

### 关键模块

#### 模块一

#### 模块二

#### 模块三

## 公式

### 公式一

$$

$$

变量含义：

- $x$：
- $y$：

直观解释：

## 实验设计

### 数据集或环境

### 对比方法

### 评价指标

### 实现细节

## 实验结果

### 主要结果

### 消融实验

### 案例分析

### 失败案例

## 我的判断

### 优点

-

### 缺点

-

### 结论是否被实验充分支持

-

### 是否值得复现

- [ ] 值得完整复现
- [ ] 只复现核心模块
- [ ] 只作为参考
- [ ] 暂不复现

原因：

## 尚未理解的问题

- [ ]
- [ ]

## 对我的研究的启发

### 可以借鉴的方法

### 可以改进的地方

### 潜在研究问题

1.
2.
3.

## 相关知识

- [[]]
- [[]]

## 相关论文

- [[]]
- [[]]
````

Obsidian 自带模板核心插件，可以在模板中使用日期、时间和标题变量，然后将模板插入新笔记。([Obsidian][9])

---

# 十、真正有效的 Obsidian 工作流

## 第一步：快速记录

所有没有时间整理的内容先进入：

```text
00 Inbox
```

例如：

```md
# GUI Agent 临时想法

- OSWorld 是否可以增加中文系统环境？
- GUI Grounding 能否结合 accessibility tree？
- 查一下 self-correction 在 GUI Agent 中的应用。
```

不要因为分类困难而停止记录。

## 第二步：把“资料”变成“理解”

不要只复制论文原文：

```md
作者提出了一种新的 GUI Agent 方法……
```

应该进一步写：

```md
## 我的理解

作者真正解决的是动作空间过大的问题。

其方法不是直接预测任意坐标，而是先生成候选元素，再在候选元素中进行选择，因此降低了决策难度。
```

推荐区分：

```md
## 原文信息

## 我的理解

## 我的质疑

## 对我的启发
```

## 第三步：提取概念笔记

当一篇论文中出现值得复用的概念时，不要只放在论文笔记里。

例如，从论文中提取：

```md
[[GUI Grounding]]
[[Accessibility Tree]]
[[Action Space]]
[[Agent Self-Correction]]
```

每个概念单独形成笔记。

## 第四步：建立链接

不要为了链接而链接。

只有当你能说出关系时才建立链接：

```md
[[SeeClick]] 使用 [[GUI Grounding]] 将语言描述映射为屏幕坐标。

[[OSWorld]] 是用于评估 [[Computer Use Agent]] 的真实桌面环境。

[[Accessibility Tree]] 可以作为 [[GUI Agent]] 的结构化界面输入。
```

链接周围的文字非常重要，因为它解释了两个概念为什么相关。

## 第五步：定期整理知识地图

例如创建：

```md
# GUI Agent 知识地图

## 总览

GUI Agent 的基本闭环：

![[GUI Agent#基本闭环]]

## 核心问题

- [[GUI Perception]]
- [[GUI Grounding]]
- [[Task Planning]]
- [[Action Space]]
- [[Agent Memory]]
- [[Self-Correction]]

## 环境类型

- [[Web Agent]]
- [[Desktop Agent]]
- [[Mobile Agent]]

## Benchmark

- [[OSWorld]]
- [[WebArena]]
- [[AndroidWorld]]
- [[Mind2Web]]

## 当前研究问题

- 跨应用泛化
- 长程任务规划
- 动作错误恢复
- 隐私与安全
- 高成本轨迹采集
```

这类笔记不是具体知识本身，而是知识导航入口。

---

# 十一、初学者常见误区

## 误区一：刚开始就安装大量插件

一开始只需要掌握：

* 文件；
* Markdown；
* 内部链接；
* 反向链接；
* 搜索；
* 模板；
* 属性。

Obsidian 确实支持大量核心插件、社区插件和主题，但插件应该服务于已经明确的工作流，而不是先安装再寻找用途。([Obsidian][1])

## 误区二：花大量时间设计目录

目录只需要满足“能大概找到”。

真正的知识关系应当通过：

```md
[[内部链接]]
```

表达。

## 误区三：复制很多，但没有自己的总结

论文笔记至少应该有：

```md
## 一句话总结

## 我的理解

## 我的质疑

## 对研究的启发
```

否则 Obsidian 只是一个资料仓库，而不是知识库。

## 误区四：一篇笔记写所有内容

一篇名为：

```text
GUI Agent 全部知识.md
```

最终可能有几万字，难以复用和链接。

更好的方式是拆成：

```text
GUI Agent.md
GUI Grounding.md
Action Space.md
Agent Memory.md
OSWorld.md
WebArena.md
```

然后通过链接连接。

## 误区五：为了让关系图好看而乱加链接

关系图只是链接结果的可视化，不是记笔记的目标。

你的目标应该是：

> 将论文中的信息转化为可复用、可检索、可连接的研究知识。

---

# 十二、最小可行使用方案

刚开始使用时，只执行下面五件事：

1. 创建一个 `Research Vault`；
2. 建立 `Inbox、Projects、Papers、Concepts、Templates、Attachments`；
3. 每篇论文建立一篇论文笔记；
4. 遇到重要概念时，创建 `[[概念笔记]]`；
5. 每篇笔记写清楚“总结、理解、问题、启发”。

最核心的 Markdown 只需要先记住：

```md
# 标题

## 二级标题

- 列表

- [ ] 任务

**加粗**

==高亮==

[[内部链接]]

![[嵌入笔记或图片]]

`行内代码`

$$
数学公式
$$
```

先形成稳定的记录和整理习惯，再逐步加入属性、模板、Bases 和社区插件。

[1]: https://obsidian.md/help/obsidian?utm_source=chatgpt.com "About Obsidian - Obsidian Help"
[2]: https://obsidian.md/zh/help/links?utm_source=chatgpt.com "内部链接 - Obsidian 中文帮助"
[3]: https://obsidian.md/zh/help/obsidian-flavored-markdown?utm_source=chatgpt.com "Obsidian 风格的 Markdown 语法 - Obsidian 中文帮助"
[4]: https://obsidian.md/help/?utm_source=chatgpt.com "Home - Obsidian Help"
[5]: https://obsidian.md/zh/help/%E7%BC%96%E8%BE%91%E4%B8%8E%E6%A0%BC%E5%BC%8F%E5%8C%96/%E5%9F%BA%E6%9C%AC%E6%A0%BC%E5%BC%8F%E8%AF%AD%E6%B3%95?utm_source=chatgpt.com "基本格式语法 - Obsidian 中文帮助"
[6]: https://obsidian.md/zh/help/file-formats?utm_source=chatgpt.com "支持的文件格式 - Obsidian 中文帮助"
[7]: https://obsidian.md/zh/help/%E7%BC%96%E8%BE%91%E4%B8%8E%E6%A0%BC%E5%BC%8F%E5%8C%96/%E5%B1%9E%E6%80%A7?utm_source=chatgpt.com "属性 - Obsidian 中文帮助"
[8]: https://obsidian.md/zh/help/settings?utm_source=chatgpt.com "设置 - Obsidian 中文帮助"
[9]: https://obsidian.md/zh/help/%E6%8F%92%E4%BB%B6/%E6%A8%A1%E6%9D%BF?utm_source=chatgpt.com "模板 - Obsidian 中文帮助"
