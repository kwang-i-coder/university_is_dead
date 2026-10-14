#!/usr/bin/env python3
"""Obsidian 위키링크 검사기.

사용법: python3 tools/check_links.py {과목 폴더 또는 vault 폴더}

폴더 안 모든 .md의 [[노트]], [[노트#헤딩]], [[파일.pdf#page=N]] 링크를 확인한다.
- 없는 노트나 헤딩은 오류로 센다 (종료 코드 1).
- 없는 첨부(PDF·이미지)는 경고만 한다. 강의자료는 .gitignore로 빠져 있을 수 있기 때문이다.
노트 이름은 Obsidian처럼 vault 전체에서 찾는다.
vault 루트는 위로 올라가며 처음 만나는 .obsidian 폴더나 CLAUDE.md가 있는 곳이다.
못 찾으면 대상 폴더를 루트로 보고 경고한다. 이때 [[학기/과목/개념]] 같은 경로 링크는 틀리게 나올 수 있다.
대상 폴더가 없거나 .md가 하나도 없으면 종료 코드 2로 끝난다.
"""
import pathlib
import re
import sys
from typing import Optional

ATTACH = re.compile(r"\.(pdf|png|jpe?g|gif|svg|webp|html)$", re.I)
LINK = re.compile(r"!?\[\[([^\]|\\]+?)(?:\\?\|[^\]]*)?\]\]")
HEADING = re.compile(r"^#{1,6} +(.*?)\s*$")


def vault_root(start: pathlib.Path) -> Optional[pathlib.Path]:
    for p in [start, *start.parents]:
        if (p / ".obsidian").is_dir() or (p / "CLAUDE.md").is_file():
            return p
    return None


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
    if not target.is_dir():
        print(f"폴더가 아님: {sys.argv[1]}", file=sys.stderr)
        return 2
    if next(target.rglob("*.md"), None) is None:
        print(f".md 파일이 없음: {sys.argv[1]}", file=sys.stderr)
        return 2
    root = vault_root(target)
    if root is None:
        print("경고: vault 루트(.obsidian 또는 CLAUDE.md)를 못 찾아 대상 폴더를 루트로 봄. 경로 링크가 틀리게 나올 수 있음", file=sys.stderr)
        root = target
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
