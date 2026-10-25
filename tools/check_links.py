#!/usr/bin/env python3
"""Obsidian wikilink checker.

Usage: python3 tools/check_links.py {course folder or vault folder}

Checks the [[note]], [[note#heading]], and [[file.pdf#page=N]] links in every .md in the folder.
- A missing note or heading is an error (exit code 1).
- A missing attachment (PDF, image) is only a warning, since lecture materials may be excluded by .gitignore.
- A missing .canvas is an error.
- When several notes share a name, it warns "ambiguous" and accepts a heading found in any of them.
Note names are matched across the whole vault case-insensitively, as Obsidian does.
Korean file names are compared after NFC normalization (macOS may produce NFD names).
The vault root is the first folder, going upward, that contains a .obsidian folder or CLAUDE.md.
If none is found, the target folder is used as the root with a warning; path links such as
[[folder/course/note]] may then be reported wrongly.
Exits with code 2 if the target folder does not exist or contains no .md files.
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
    """Yields link targets outside code blocks and inline code. `code` inside a link is kept as is."""
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
        print(f"not a directory: {sys.argv[1]}", file=sys.stderr)
        return 2
    if next(target.rglob("*.md"), None) is None:
        print(f"no .md files: {sys.argv[1]}", file=sys.stderr)
        return 2
    root = vault_root(target)
    if root is None:
        print("warning: vault root (.obsidian or CLAUDE.md) not found; using the target folder as the root. Path links may be reported wrongly", file=sys.stderr)
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
                        errors.append(f"missing file        {where}")
                    else:
                        warnings.append(f"missing attachment  {where}")
                continue
            dests = notes.get(key(name), []) if name else [md]
            if not dests:
                errors.append(f"missing note        {where}")
                continue
            if len(dests) > 1:
                warnings.append(f"ambiguous           {where} ({len(dests)} notes share this name; link by path)")
            if head and not head.startswith("^") and not any(head in headings(d, cache) for d in dests):
                errors.append(f"missing heading     {where}")

    for line in warnings + errors:
        print(line)
    print(f"\n{len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
