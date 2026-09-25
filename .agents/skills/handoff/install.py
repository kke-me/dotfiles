#!/usr/bin/env python3
"""Place handoff files in a git repo and keep them out of the index."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

FILES = Path(__file__).resolve().parent / "files"
EXCLUDE_LINES = (
    "/HANDOFF/",
    ".cursor/rules/handoff.mdc",
    ".cursor/skills/kickoff",
    ".cursor/skills/state",
    ".cursor/skills/blocking",
    ".cursor/skills/human",
)


def repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        sys.exit(result.stderr.strip() or "not a git repository")
    return Path(result.stdout.strip())


def place(repo: Path) -> list[str]:
    notes: list[str] = []
    for src in sorted(FILES.rglob("*")):
        if not src.is_file():
            continue
        rel = src.relative_to(FILES)
        dest = repo / rel
        if dest.exists():
            notes.append(f"skip {rel}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(src.read_bytes())
        notes.append(f"create {rel}")
    return notes


def exclude(repo: Path) -> list[str]:
    path = repo / ".git" / "info" / "exclude"
    path.parent.mkdir(parents=True, exist_ok=True)
    text = path.read_text(encoding="utf-8") if path.exists() else ""
    existing = set(text.splitlines())
    added = [line for line in EXCLUDE_LINES if line not in existing]
    if not added:
        return []
    suffix = "" if text.endswith("\n") or text == "" else "\n"
    path.write_text(text + suffix + "\n".join(added) + "\n", encoding="utf-8")
    return added


def main() -> None:
    repo = repo_root()
    for note in place(repo):
        print(note)
    added = exclude(repo)
    if added:
        print("exclude " + ", ".join(added))
    else:
        print("exclude unchanged")
    print(repo)


if __name__ == "__main__":
    main()
