#!/usr/bin/env python3
"""Obsidian 위키링크 검사기.

사용법: python3 tools/check_links.py {과목 폴더 또는 vault 폴더}

폴더 안 모든 .md의 [[노트]], [[노트#헤딩]], [[파일.pdf#page=N]] 링크를 확인한다.
- 없는 노트나 헤딩은 오류로 센다 (종료 코드 1).
- 없는 첨부(PDF·이미지)는 경고만 한다. 강의자료는 .gitignore로 빠져 있을 수 있기 때문이다.
- 없는 .canvas는 오류로 센다.
- 같은 이름의 노트가 여러 개면 "모호함" 경고를 내고, 헤딩은 후보 중 하나에만 있어도 통과시킨다.
노트 이름은 Obsidian처럼 vault 전체에서 대소문자 구분 없이 찾는다.
한글 파일명은 NFC로 맞춰 비교한다 (macOS에서 받은 NFD 파일명 대비).
vault 루트는 위로 올라가며 처음 만나는 .obsidian 폴더나 CLAUDE.md가 있는 곳이다.
못 찾으면 대상 폴더를 루트로 보고 경고한다. 이때 [[학기/과목/개념]] 같은 경로 링크는 틀리게 나올 수 있다.
대상 폴더가 없거나 .md가 하나도 없으면 종료 코드 2로 끝난다.
"""
import pathlib
import re
import sys
import unicodedata
from typing import Optional

ATTACH = re.compile(r"\.(pdf|png|jpe?g|gif|svg|webp|html)$", re.I)
LINK = re.compile(r"!?\[\[([^\]|\\]+?)(?:\\?\|[^\]]*)?\]\]")
CODE_OR_LINK = re.compile(r"`[^`\n]*`|" + LINK.pattern)
CANVAS = re.compile(r"\.canvas$", re.I)
HEADING = re.compile(r"^#{1,6} +(.*?)\s*$")


def vault_root(start: pathlib.Path) -> Optional[pathlib.Path]:
    for p in [start, *start.parents]:
        if (p / ".obsidian").is_dir() or (p / "CLAUDE.md").is_file():
            return p
    return None


def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def key(name: str) -> str:
    return nfc(name).casefold()


def strip_fences(text: str) -> str:
    return re.sub(r"```.*?```", "", text, flags=re.S)


def links(text: str):
    """코드 블록과 인라인 코드 밖의 링크 대상만 돌려준다. 링크 안의 `코드`는 그대로 둔다."""
    for m in CODE_OR_LINK.finditer(strip_fences(text)):
        if m.group(1) is not None:
            yield m.group(1)


def headings(path: pathlib.Path, cache: dict) -> set:
    if path not in cache:
        lines = nfc(strip_fences(path.read_text(encoding="utf-8"))).split("\n")
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
        rel = p.relative_to(root).with_suffix("").as_posix()
        for k in {key(p.stem), key(rel)}:
            notes.setdefault(k, []).append(p)
    files = set()
    for p in root.rglob("*"):
        if p.is_file():
            files.add(key(p.name))
            files.add(key(p.relative_to(root).as_posix()))
    cache, errors, warnings = {}, [], []

    for md in sorted(target.rglob("*.md")):
        for raw in links(md.read_text(encoding="utf-8")):
            name, _, head = nfc(raw).partition("#")
            where = f"{md.relative_to(target)}: [[{raw}]]"
            if ATTACH.search(name) or CANVAS.search(name):
                if key(name) not in files and key(pathlib.PurePosixPath(name).name) not in files:
                    if CANVAS.search(name):
                        errors.append(f"파일 없음  {where}")
                    else:
                        warnings.append(f"첨부 없음  {where}")
                continue
            dests = notes.get(key(name), []) if name else [md]
            if not dests:
                errors.append(f"노트 없음  {where}")
                continue
            if len(dests) > 1:
                warnings.append(f"모호함     {where} (같은 이름 {len(dests)}개, 경로로 링크하세요)")
            if head and not head.startswith("^") and not any(head in headings(d, cache) for d in dests):
                errors.append(f"헤딩 없음  {where}")

    for line in warnings + errors:
        print(line)
    print(f"\n오류 {len(errors)}개, 경고 {len(warnings)}개")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
