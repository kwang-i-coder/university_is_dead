#!/usr/bin/env python3
"""Obsidian 위키링크 검사기.

사용법: python3 tools/check_links.py {과목 폴더 또는 vault 폴더}

폴더 안 모든 .md의 [[노트]], [[노트#헤딩]], [[파일.pdf#page=N]] 링크를 확인한다.
- 없는 노트나 헤딩은 오류로 센다 (종료 코드 1).
- 없는 첨부(PDF·이미지)는 경고만 한다. 강의자료는 .gitignore로 빠져 있을 수 있기 때문이다.
노트 이름은 Obsidian처럼 vault 전체에서 찾는다 (.obsidian 폴더가 있는 곳을 vault 루트로 본다).
"""
import pathlib
import re
import sys

ATTACH = re.compile(r"\.(pdf|png|jpe?g|gif|svg|webp|html)$", re.I)
LINK = re.compile(r"!?\[\[([^\]|\\]+?)(?:\\?\|[^\]]*)?\]\]")
HEADING = re.compile(r"^#{1,6} +(.*?)\s*$")


def vault_root(start: pathlib.Path) -> pathlib.Path:
    for p in [start, *start.parents]:
        if (p / ".obsidian").is_dir():
            return p
    return start


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def headings(path: pathlib.Path, cache: dict) -> set:
    if path not in cache:
        lines = strip_code(path.read_text(encoding="utf-8")).split("\n")
        cache[path] = {m.group(1) for l in lines if (m := HEADING.match(l))}
    return cache[path]


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    target = pathlib.Path(sys.argv[1]).resolve()
    root = vault_root(target)
    notes = {}
    for p in root.rglob("*.md"):
        notes.setdefault(p.stem, p)
        notes.setdefault(str(p.relative_to(root).with_suffix("")), p)
    files = {p.name for p in root.rglob("*") if p.is_file()}
    cache, errors, warnings = {}, [], []

    for md in sorted(target.rglob("*.md")):
        text = strip_code(md.read_text(encoding="utf-8"))
        for m in LINK.finditer(text):
            name, _, head = m.group(1).partition("#")
            where = f"{md.relative_to(target)}: [[{m.group(1)}]]"
            if ATTACH.search(name):
                if pathlib.Path(name).name not in files:
                    warnings.append(f"첨부 없음  {where}")
                continue
            dest = notes.get(name) if name else md
            if dest is None:
                errors.append(f"노트 없음  {where}")
            elif head and not head.startswith("^") and head not in headings(dest, cache):
                errors.append(f"헤딩 없음  {where}")

    for line in warnings + errors:
        print(line)
    print(f"\n오류 {len(errors)}개, 경고 {len(warnings)}개")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
