# university_is_dead 🎓

**English** | [한국어](README.ko.md)

**An instruction set and Obsidian note templates for studying university lectures with Claude.**
Add your lecture PDFs, then use short commands such as `운체 3` (OS chapter 3), `다음` (next), or `시험 정리본` (exam summary) to get in-depth explanations in slide order. Claude can also build note skeletons, exam summaries, and ELI5 picture books.

> **Language note:** The instructions, templates, commands, and example vault are written in Korean, and Claude answers in Korean by default. Only the documentation and contributor-facing files have English versions for now.

---

## What it does

| You say | What happens |
|---|---|
| `운체 3` | Shows a map of chapter 3 split into groups, one key question per group, then explains group 1 |
| `운체 3-2` / `다음` | Explains one group in slide order, with formulas, worked numeric examples, and self-check questions |
| `골격 만들어줘` + PDF | Creates an empty note in the form `## Section / ### Slide Title (Korean) / - ` |
| `정리해줘` | Completes your notes from the PDF while keeping what you wrote |
| `시험 정리본` | ★ importance marks, comparison tables, practice problems with grading criteria, and an exam-point Q&A |
| `/eli5 {note}` | An HTML picture book that separates analogies from lecture definitions |
| `저장해줘` / `운체 3 전부` | Saves group explanations as notes in `클코 설명/`, chained with `다음 →` links from first to last |
| `기출 분석` + past exams or exam reviews | Writes per-year problem tables, frequent topics, and priorities to `클코 정리/기출 분석.md` |
| (`증명 과목` in the course exceptions) | Proof templates for each theorem, converse-and-condition tables, and mock exams in the past-exam format |

## 5-minute setup

1. Get this repo: **Use this template** on GitHub, or Code → Download ZIP.
2. Using `example-vault/` as a reference, create a course folder in your Obsidian vault. You can put it inside a semester folder; if you do, write that full path in the course table.
   ```
   (vault root)/
   ├── CLAUDE.md          ← when using Claude Code (step 4)
   ├── templates/         ← copy of this repo's templates/
   ├── tools/             ← copy of this repo's tools/
   └── {course}/
       ├── 강의자료/        ← lecture PDFs (read-only)
       ├── {lecture title}.md  ← weekly notes
       ├── 개념.md          ← concept hub + weekly notes table
       ├── 클코 정리/       ← exam summaries, past-exam analysis
       ├── 클코 설명/       ← saved group explanations
       └── 학습자료/        ← ELI5 HTML
   ```
   Give each lecture PDF the same name as its note (`1주차 정렬 기초.md` ↔ `강의자료/1주차 정렬 기초.pdf`) so that PDF page links resolve.
3. Open `INSTRUCTIONS.md` and fill in your school, courses, and abbreviations in the **"📝 여기만 고치세요"** ("edit only here") block. Write each course folder as a path from the vault root (e.g. `딥러닝/`).
4. Give the instructions to Claude.
   - **Claude Projects**: paste the contents into Project instructions, and upload your course folder and the `templates/` files as project knowledge.
   - **Claude Code**: make the same edits in `CLAUDE.md`, copy `CLAUDE.md`, `templates/`, and `tools/` to your vault root, and run Claude Code from there. The link checker needs Python 3.8 or later.
5. Try `{abbreviation} 1`.

## Repository layout

| Path | Contents |
|---|---|
| [`INSTRUCTIONS.md`](INSTRUCTIONS.md) | The instructions (for Claude Projects) |
| [`CLAUDE.md`](CLAUDE.md) | The same instructions (for Claude Code) |
| [`templates/`](templates) | Empty templates: note skeleton, 개념.md, exam summary, group explanation, past-exam analysis, ELI5 HTML |
| [`tools/check_links.py`](tools/check_links.py) | Obsidian link checker (finds missing notes, headings, and attachments) |
| [`example-vault/알고리즘/`](example-vault/알고리즘) | An example filled in with a fictional Algorithms course. Open it in Obsidian |
| [`docs/usage-examples.md`](docs/usage-examples.md) | Conversation flow for each command |
| [`docs/FAQ.md`](docs/FAQ.md) | Frequently asked questions |

## Core principles

- **The lecture materials are the source of truth.** Anything not on the slides is marked "교재 보충" (textbook supplement).
- **Your notes are never overwritten.** Claude only adds what is missing, with minimal edits.
- **Slide order is kept.** Groups are never mixed, and appendix slides get their own groups.
- **Explanations are never thin.** Each concept goes motivation → intuition → definition/formula → numeric example → limitations.

## ⚠️ Do not upload lecture materials

Your professors' lecture materials, and notes that transcribe lecture content, are copyrighted works. If you back up your vault to GitHub, use this repo's [`.gitignore`](.gitignore) and do not push it to a public repository. Every example in this repo is a newly written, fictional lecture.

## Contributing

New commands, rules for other kinds of courses, and template improvements are all welcome. Read [`CONTRIBUTING.md`](CONTRIBUTING.md), open an issue with one of the issue templates (Bug Report / Enhancement Request / Common Issue), and then send a PR. Every PR is checked automatically for instruction-file sync, example-vault links, and uploaded lecture materials.

## License

[MIT](LICENSE)
