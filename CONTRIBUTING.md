# Contributing

Thanks for your interest in university_is_dead. This repo collects instructions and templates that people have refined while studying their own courses. Everything is welcome, from a small typo fix to a new command.

## Workflow

1. **Open an issue first.** Pick one of the issue templates (blank issues are disabled).
   - **Bug Report**: you followed the instructions, but Claude behaved differently
   - **Enhancement Request**: a new command, rule, template, or support for a new kind of course
   - **Common Issue**: questions, feedback, or documentation improvements
2. **Fork and create a branch.** Name the branch after what it does, in English kebab-case. Examples: `add-proof-course-mode`, `fix-skeleton-heading-links`.
3. **Make your changes and check them locally.** See "Rules" and "How to check" below.
4. **Send a PR.** Fill in the PR template and link the issue with `Fixes #<issue number>`. The automated check must pass before the PR can be merged.

## Rules

### Write commits, PRs, and branch names in English
Commit messages, PR titles and descriptions, branch names, and review comments are written in English. The product content (the instructions, templates, and example vault) stays in Korean for now.

### Edit both instruction files together
`INSTRUCTIONS.md` (for Claude Projects) and `CLAUDE.md` (for Claude Code) differ only in the notice at the top. Everything from `## 📝 여기만 고치세요` to the end must be identical. If you edit only one of them, the automated check fails.

### Do not upload lecture materials or real lecture notes
Professors' slides, PDFs, original past exams, and notes that transcribe real lectures are copyrighted works.
- Write examples as **newly made-up lectures**, like the fictional Algorithms course in `example-vault/`.
- If you want to share an approach that worked well for your course, bring only the rules and templates, and replace the content with a fictional example.
- In issues, too, describe the situation in words instead of attaching slide screenshots.

### Keep rules short and actionable
- Make "what, when, and how" clear. Example: "Do not use `:` in headings (it breaks Obsidian heading links)."
- Add one line on why the rule is needed, so others can judge whether it fits their situation.
- For rules that are closer to personal preference, propose them as options (a course exception or a command) instead of changing the defaults.

### Update the docs when you add a command or rule
- The "What it does" table in `README.md` and the "무엇을 할 수 있나" table in `README.ko.md`
- The conversation flows in `docs/usage-examples.md` and `docs/usage-examples.ko.md`
- If needed, the empty templates in `templates/` and the examples in `example-vault/`

The README, FAQ, and usage examples each have an English file and a Korean `.ko.md` file. When you change one, update the other in the same PR.

The README is also translated into Chinese, Japanese, Spanish, Vietnamese, and Portuguese (`README.zh-CN.md`, `README.ja.md`, `README.es.md`, `README.vi.md`, `README.pt-BR.md`). The English README is authoritative. Update the translations too if you can; if not, say so in the PR so they can be updated later.

## How to check

```bash
# 1. The rule sections of the two instruction files are identical
diff <(sed -n '/^## 📝/,$p' CLAUDE.md) <(sed -n '/^## 📝/,$p' INSTRUCTIONS.md)

# 2. The link checker's unit tests pass
python3 -m unittest discover tests

# 3. No links in the example vault are broken (0 errors expected; "missing attachment" warnings are fine)
python3 tools/check_links.py example-vault
```

When you open a PR, GitHub Actions runs the same checks automatically and also makes sure that no PDFs, PPTs, or images are inside a `강의자료/` (lecture materials) folder.

## Commit messages

Describe what you changed in one line. Examples: `Add proof-course mode to instructions`, `Fix heading link rule in skeleton template`.
