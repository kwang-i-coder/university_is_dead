# Usage examples

**English** | [한국어](usage-examples.ko.md)

These conversation flows use the `example-vault/알고리즘` (Algorithms) course. They assume the course table in the instructions contains `| 알고리즘 (알고) | 알고리즘/ | 1주차 정렬 기초.md |`. Commands are in Korean, so each one is followed by its meaning in parentheses. Claude's real answers are much longer (because of the explanation-depth rules).

## 1. Create a note skeleton

> **Me**: 알고리즘 2주차 골격 만들어줘 (강의자료/2주차 분할 정복.pdf)
> (Make the week 2 skeleton for Algorithms.)

Claude lays out the PDF's sections as `##` and slide titles as `###` to create `2주차 분할 정복.md`, then updates the next link in `1주차 정렬 기초.md` and the "주차별 필기" (weekly notes) table in `개념.md`.
→ Result: [`example-vault/알고리즘/2주차 분할 정복.md`](../example-vault/알고리즘/2주차%20분할%20정복.md)

## 2. Study a chapter

> **Me**: 알고 2
> (Algorithms, chapter 2.)

Since this is the first time, Claude shows the group map once and explains group 1.

| Group | Topic | Slides | Key question |
|---|---|---|---|
| 1 | Divide and conquer and recurrences | p.2–6 | Why does splitting a problem make it faster? |
| 2 | Merge Sort | p.7–12 | How do you merge two sorted arrays? |
| 3 | Quick Sort | p.13–19 | How does the choice of pivot change performance? |

> **Me**: 다음
> (Next.)

Claude starts with a single line, `그룹 2/3 · Merge Sort (p.7–12)`, and explains only group 2. The answer ends with self-check questions and a pointer to the next group.

> **Me**: 알고 2-3
> (Algorithms, chapter 2, group 3.)

Claude goes straight to group 3.

## 3. Complete your notes

> **Me**: 1주차 정리해줘
> (Complete my week 1 notes.)

Claude keeps the bullets you filled in and adds only the empty bullets and missing parts, based on the PDF.

## 4. Exam summary

> **Me**: 1주차 시험 정리본
> (Week 1 exam summary.)

→ Result: [`클코 정리/L1-정렬기초.md`](../example-vault/알고리즘/클코%20정리/L1-정렬기초.md)

## 5. ELI5 picture book

> **Me**: /eli5 1주차 정렬 기초

→ Result: [`학습자료/1주차 정렬 기초.html`](../example-vault/알고리즘/학습자료/1주차%20정렬%20기초.html)

## 6. Save a group explanation

> **Me**: 알고 1-1 … (after the explanation) 저장해줘
> (Save it.)

Claude saves the group it just explained as `클코 설명/L01-1 정렬 문제와 안정성.md` and adds links to it at the top of `1주차 정렬 기초.md` and in `개념.md`. To create a whole chapter at once, say `알고 1 전부` (all of chapter 1).
→ Result: [`클코 설명/L01-1 정렬 문제와 안정성.md`](../example-vault/알고리즘/클코%20설명/L01-1%20정렬%20문제와%20안정성.md)

## 7. Past-exam analysis and proof courses

> **Me**: 기출 분석 (강의자료/기출/ 폴더)
> (Analyze the past exams in the 강의자료/기출/ folder.)

Claude writes `클코 정리/기출 분석.md` with a table linking each year's problems to lecture pages, the frequent topics within the exam scope, and a priority list. If you give it screenshots of students' exam reviews, it finds the matching lecture for each item and tells you separately about topics that are not in the materials you have.

If you write `증명 과목` (proof course) in the course exceptions, exam summaries switch to verbatim definitions, an exam-ready proof for each theorem, converse-and-condition tables, and mock exams in the past-exam format.
