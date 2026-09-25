#!/usr/bin/env python3
"""List Cursor skills the user registered, plus skills in the current repo."""

from __future__ import annotations

import subprocess
from pathlib import Path


def field(path: Path, key: str) -> str:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    if end < 0:
        return ""
    lines = text[3:end].splitlines()
    chunks: list[str] = []
    capturing = False
    prefix = f"{key}:"
    for line in lines:
        if capturing:
            if line.startswith((" ", "\t")):
                chunks.append(line.strip())
                continue
            break
        if line.startswith(prefix):
            rest = line.split(":", 1)[1].strip()
            if rest in {">-", ">", "|"}:
                capturing = True
                continue
            return rest.strip("\"'")
    return " ".join(chunks)


def listing(path: Path) -> str:
    return field(path, "ja") or field(path, "description")


def registered(root: Path) -> list[tuple[str, str, Path]]:
    if not root.is_dir():
        return []
    found: list[tuple[str, str, Path]] = []
    for child in sorted(root.iterdir(), key=lambda p: p.name):
        skill = child / "SKILL.md"
        if child.is_dir() and skill.is_file():
            found.append((child.name, listing(skill), skill))
    return found


def git_root() -> Path | None:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        return None
    return Path(result.stdout.strip())


def show(title: str, rows: list[tuple[str, str, Path]]) -> None:
    print(title)
    if not rows:
        print("  (none)")
        return
    for name, desc, path in rows:
        print(f"  /{name}")
        if desc:
            print(f"    {desc}")
        print(f"    {path}")


def dedupe(rows: list[tuple[str, str, Path]]) -> list[tuple[str, str, Path]]:
    seen: set[Path] = set()
    kept: list[tuple[str, str, Path]] = []
    for name, desc, path in rows:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        kept.append((name, desc, path))
    return kept


def main() -> None:
    home = Path.home()
    personal = dedupe(
        registered(home / ".agents" / "skills") + registered(home / ".cursor" / "skills")
    )
    personal_paths = {path.resolve() for _, _, path in personal}
    show("personal", personal)

    root = git_root()
    if root is None:
        show("repo", [])
        return
    repo_rows = [
        row
        for row in dedupe(
            registered(root / ".agents" / "skills") + registered(root / ".cursor" / "skills")
        )
        if row[2].resolve() not in personal_paths
    ]
    show(f"repo {root.name}", repo_rows)


if __name__ == "__main__":
    main()
