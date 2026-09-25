#!/usr/bin/env python3
"""Rewrite the model table in pstack/README.md from pstack-models.mdc."""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

README = Path(__file__).resolve().parent / "README.md"
RULE = Path.home() / ".cursor" / "rules" / "pstack-models.mdc"
START = "<!-- models:start -->"
END = "<!-- models:end -->"

GLOSS = {
    "feature, refactoring": "機能追加、リファクタ",
    "bug-fix": "バグ修正",
    "perf-issue": "速度の一回きりの修正",
    "hillclimb": "指標を測りながらの改善",
    "judgment and prose": "判断と文章",
    "hardest tasks": "一番難しい実装",
    "how explorer": "`/how` の調査",
    "how explainer": "`/how` の説明",
    "why investigators": "`/why` の調査",
    "why synthesizer": "`/why` のまとめ",
    "reflect tooling": "`/reflect` のツール側",
    "reflect judgment, divergent, synthesizer": "`/reflect` の判断",
    "arena runners": "`/arena` の候補。エントリの数が体の数",
    "arena cross-judge pool": "親と別ファミリーを1つ選ぶ",
    "swarm workers": "`/swarm` の作業者",
    "architect runners": "`/architect` の並列。エントリの数が体の数",
    "interrogate reviewers": "`/interrogate` のレビューア。エントリの数が体の数",
}


def parse(text: str) -> tuple[str, list[tuple[str, str]]]:
    parts = text.split("---", 2)
    body = parts[2] if len(parts) >= 3 else text
    budget = ""
    roles: list[tuple[str, str]] = []
    for raw in body.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") and not line.startswith("# budget:"):
            continue
        if line.startswith("# budget:"):
            budget = line.split(":", 1)[1].strip()
            continue
        if ":" not in line:
            continue
        role, models = line.split(":", 1)
        roles.append((role.strip(), models.strip()))
    if not budget or not roles:
        sys.exit("pstack-models.mdc has no budget or roles")
    return budget, roles


def models_cell(models: str) -> str:
    return ", ".join(f"`{item.strip()}`" for item in models.split(",") if item.strip())


def uses_parent(roles: list[tuple[str, str]]) -> bool:
    aliases = {"inherit-parent", "auto"}
    for _, models in roles:
        for item in models.split(","):
            if item.strip() in aliases:
                return True
    return False


def block(budget: str, roles: list[tuple[str, str]]) -> str:
    alias = (
        "親と同じモデルにする役割がある。"
        if uses_parent(roles)
        else "今のルールに `inherit-parent` と `auto` は無い。"
    )
    rows = [
        "| 役割 | モデル | 使うところ |",
        "| --- | --- | --- |",
    ]
    for role, models in roles:
        gloss = GLOSS.get(role, "（未記載）")
        rows.append(f"| {role} | {models_cell(models)} | {gloss} |")
    body = "\n".join(
        [
            f"この表の予算は `{budget}`。{date.today().isoformat()} に `~/.cursor/rules/pstack-models.mdc` から生成した。",
            "",
            alias,
            "",
            "## 役割",
            "",
            *rows,
        ]
    )
    return f"{START}\n{body}\n{END}\n"


def main() -> None:
    if not RULE.is_file():
        sys.exit(f"missing {RULE}")
    text = README.read_text(encoding="utf-8")
    start = text.find(START)
    end = text.find(END)
    if start < 0 or end < 0 or end < start:
        sys.exit("README is missing models markers")
    end = end + len(END)
    if end < len(text) and text[end] == "\n":
        end += 1
    budget, roles = parse(RULE.read_text(encoding="utf-8"))
    updated = text[:start] + block(budget, roles) + text[end:]
    if updated == text:
        print("unchanged")
    else:
        README.write_text(updated, encoding="utf-8")
        print(f"updated {README}")


if __name__ == "__main__":
    main()
