# university_is_dead 🎓

[English](README.md) | [한국어](README.ko.md) | **中文** | [日本語](README.ja.md) | [Español](README.es.md) | [Tiếng Việt](README.vi.md) | [Português](README.pt-BR.md)

**一套用 Claude 学习大学课程的指令集和 Obsidian 笔记模板。**
放入课程 PDF 后，用 `운체 3`（操作系统第 3 章）、`다음`（下一个）、`시험 정리본`（考试总结）这样的简短命令，就能按幻灯片顺序获得深入讲解。Claude 还能生成笔记骨架、考试总结和 ELI5 图画书。

> **语言说明：** 指令、模板、命令和示例库（vault）均以韩语编写，Claude 默认用韩语回答。目前只有文档和面向贡献者的文件提供英文版本。本 README 译自英文版；如两者有出入，以英文 README 为准。

---

## 功能一览

| 你说 | 会发生什么 |
|---|---|
| `운체 3` | 把第 3 章按"每组一个核心问题"划分，先展示分组地图，再讲解第 1 组 |
| `운체 3-2` / `다음` | 按幻灯片顺序讲解一个分组，附公式、带计算过程的数值示例和自测题 |
| `골격 만들어줘` + PDF | 生成格式为 `## 章节 / ### Slide Title (韩语) / - ` 的空白笔记 |
| `정리해줘` | 保留你写下的内容，依据 PDF 补全笔记 |
| `시험 정리본` | ★ 重要度标记、对比表、附评分标准的练习题，以及考点问答 |
| `/eli5 {笔记}` | 一本把比喻和课程定义区分开来的 HTML 图画书 |
| `저장해줘` / `운체 3 전부` | 把分组讲解保存为 `클코 설명/` 中的笔记，并用 `다음 →` 链接从头串到尾 |
| `기출 분석` + 往年试题或考试回忆 | 把按年份整理的题目表、高频主题和优先级写入 `클코 정리/기출 분석.md` |
| （在课程例外中写上 `증명 과목`） | 每个定理的证明模板、逆命题与成立条件表，以及按往年试题格式出的模拟考试 |

## 5 分钟上手

1. 获取本仓库：在 GitHub 上点击 **Use this template**，或选择 Code → Download ZIP。
2. 参考 `example-vault/`，在你的 Obsidian 库中创建课程文件夹。也可以把它放进学期文件夹；这样做的话，请在课程表中写上完整路径。
   ```
   (库根目录)/
   ├── CLAUDE.md          ← 使用 Claude Code 时（第 4 步）
   ├── templates/         ← 复制本仓库的 templates/
   ├── tools/             ← 复制本仓库的 tools/
   └── {课程}/
       ├── 강의자료/        ← 讲义 PDF（只读）
       ├── {讲义标题}.md  ← 每周笔记
       ├── 개념.md          ← 概念中心 + 每周笔记表
       ├── 클코 정리/       ← 考试总结、往年试题分析
       ├── 클코 설명/       ← 已保存的分组讲解
       └── 학습자료/        ← ELI5 HTML
   ```
   让每份讲义 PDF 与对应笔记同名（`1주차 정렬 기초.md` ↔ `강의자료/1주차 정렬 기초.pdf`），这样 PDF 页面链接才能正确跳转。
3. 打开 `INSTRUCTIONS.md`，在 **"📝 여기만 고치세요"**（“只改这里”）区块中填写你的学校、课程和缩写。课程文件夹请写成从库根目录开始的路径（例如 `딥러닝/`）。
4. 把指令交给 Claude。
   - **Claude Projects**：把内容粘贴到 Project instructions 中，并把课程文件夹和 `templates/` 中的文件上传为项目知识。
   - **Claude Code**：在 `CLAUDE.md` 中做同样的修改，把 `CLAUDE.md`、`templates/` 和 `tools/` 复制到库根目录，然后在那里运行 Claude Code。链接检查器需要 Python 3.8 或更高版本。
5. 试试 `{缩写} 1`。

## 仓库结构

| 路径 | 内容 |
|---|---|
| [`INSTRUCTIONS.md`](INSTRUCTIONS.md) | 指令（用于 Claude Projects） |
| [`CLAUDE.md`](CLAUDE.md) | 相同的指令（用于 Claude Code） |
| [`templates/`](templates) | 空白模板：笔记骨架、개념.md、考试总结、分组讲解、往年试题分析、ELI5 HTML |
| [`tools/check_links.py`](tools/check_links.py) | Obsidian 链接检查器（查找缺失的笔记、标题和附件） |
| [`example-vault/알고리즘/`](example-vault/알고리즘) | 用一门虚构的算法课填好的示例，可以用 Obsidian 打开 |
| [`docs/usage-examples.md`](docs/usage-examples.md) | 各命令的对话流程 |
| [`docs/FAQ.md`](docs/FAQ.md) | 常见问题 |

## 核心原则

- **以讲义为准。** 幻灯片上没有的内容会标注 "교재 보충"（教材补充）。
- **绝不覆盖你的笔记。** Claude 只补充缺失的部分，并尽量少改动。
- **保持幻灯片顺序。** 不打乱分组，附录幻灯片单独成组。
- **讲解绝不单薄。** 每个概念都按 动机 → 直觉 → 定义/公式 → 数值示例 → 局限 的顺序展开。

## ⚠️ 不要上传讲义

教授的讲义以及转录课程内容的笔记都是受版权保护的作品。如果你把库备份到 GitHub，请使用本仓库的 [`.gitignore`](.gitignore)，并且不要推送到公开仓库。本仓库中的所有示例都是新编写的虚构课程。

## 参与贡献

欢迎新增命令、补充其他类型课程的规则，以及改进模板。请先阅读 [`CONTRIBUTING.md`](CONTRIBUTING.md)，用 issue 模板之一（Bug Report / Enhancement Request / Common Issue）提交 issue，然后再发 PR。每个 PR 都会自动检查指令文件是否同步、示例库链接是否有效，以及是否上传了讲义。

## 许可证

[MIT](LICENSE)
