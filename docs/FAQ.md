# FAQ

**English** | [한국어](FAQ.ko.md)

### Should I use Claude Projects or Claude Code?
- **Claude Projects** (claude.ai): paste the contents of `INSTRUCTIONS.md` into Project instructions and connect your course folder as project knowledge.
- **Claude Code**: put `CLAUDE.md` at your vault root and run Claude Code from that folder; the instructions are loaded automatically. It is the better fit for work that creates and edits note files directly (skeletons, exam summaries, ELI5).

### Can I use any course abbreviation?
Yes. The abbreviations you write in the "수강 과목" (courses) table become the commands as they are. You can list several, such as `운체` and `OS`.

### What about scanned PDFs or slides that are only images?
Because of the "그림뿐인 슬라이드도 확인한다" (check image-only slides too) principle, Claude renders those pages as images and explains them. It does not skip a page just because no text can be extracted.

### One chapter has two files.
Claude asks which file you mean first. If this happens often, write it down in the course exceptions line of the instructions.

### Korean text is garbled in the ELI5 HTML.
Check that the file starts with `<!doctype html>` and `<meta charset="utf-8">`. The instructions include this rule, but a file you edited by hand may have lost them.

### Can I upload my lecture materials to GitHub too?
No. Your professors' lecture materials are copyrighted and must not be redistributed. This repo's `.gitignore` blocks PDFs and PPTs inside `강의자료/`. Use the same `.gitignore` when you back up your vault to a public repository.

### What if I have past exams from seniors (족보)?
Write their location in the "시험 자료" (exam materials) line of the instructions, and exam summaries will follow their format. Without them, summaries use a "일반 시험 형식" (general exam format) and say so.

### I want to read a group explanation again later.
Say `저장해줘` (save it) after a group explanation, or `{abbreviation} {chapter} 전부` (all), and Claude saves it as a note in `클코 설명/`. The notes are chained with `← / 다음 →` links, so you can page through them in order in Obsidian.

### Does it work for proof-based courses such as math?
Write `증명 과목` (proof course) in the exceptions line of the course table. You then get examples and counterexamples instead of numeric examples, an exam-ready proof template for each theorem, and a "does the converse hold, and under what conditions?" summary.

### How do I use exam reviews from sites like Everytime?
Give Claude the screenshots and say `기출 분석` (past-exam analysis). Claude marks them as unofficial, links each item to the matching lecture, and tells you separately about topics that are not in the lecture materials you have.

### A heading link does not open in Obsidian.
Headings that contain `:` `|` `#` `^` `[` `]` break links. The "Obsidian 링크 규칙" (Obsidian link rules) in the instructions prevent this, but for notes you edited by hand, run `python3 tools/check_links.py {course folder}` from the vault root to check.
