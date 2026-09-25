---
name: handoff
description: >-
  Installs an untracked HANDOFF/ directory into the current git repository.
  It holds STATE.md, BLOCKING.md, HUMAN.md, and log.jsonl, plus the kickoff,
  state, blocking, and human skills. Lists HANDOFF/ in .git/info/exclude.
  Use when the user says /handoff.
ja: 現在の git リポジトリ直下に、git で追跡しない HANDOFF/ を置く。中身は STATE.md、BLOCKING.md、HUMAN.md、log.jsonl と、kickoff、state、blocking、human のスキル。.git/info/exclude に /HANDOFF/ を足す。/handoff と言うときに使う。
disable-model-invocation: true
triggers: ["user"]
---

# handoff

現在の git リポジトリに、手渡し用のディレクトリを置く。既存ファイルは上書きしない。`git add` もコミットもしない。`.gitignore` は変更しない。

置く場所はリポジトリ直下の `HANDOFF/` だけ。中身は `STATE.md`、`BLOCKING.md`、`HUMAN.md`、`log.jsonl`。`docs/` やリポジトリ直下の同名ファイルは作らない。`.git/info/exclude` には `/HANDOFF/` を足す。

## 役割

`install.py` が置くファイル。既存は上書きしない。

- `HANDOFF/STATE.md` — 今と次。完了済みは書かない。次のセッションはここだけ見て着手する。
- `HANDOFF/BLOCKING.md` — 作業を終えるのを妨げる項目。`なし` でないあいだ実装を始めない。
- `HANDOFF/HUMAN.md` — 人間がやる項目。エージェントは実行しない。
- `HANDOFF/log.jsonl` — 経緯の追記。実装中は読まない。レビューのときだけ読む。
- `.cursor/rules/handoff.mdc` — 常時適用。上の4つの置き場と書き方。
- `.cursor/skills/kickoff/SKILL.md` — `/kickoff`。「次」の1件に範囲を固定して着手する。
- `.cursor/skills/state/SKILL.md` — `/state`。今と次を表示する。引数があれば次だけを置き換える。
- `.cursor/skills/blocking/SKILL.md` — `/blocking`。妨げを表示する。引数があればファイル全体を置き換える。
- `.cursor/skills/human/SKILL.md` — `/human`。人間がやる項目を表示する。引数があれば足し、完了した項目は消す。

この SKILL.md があるディレクトリで、次を実行する。

```bash
python3 install.py
```

標準出力をそのまま返す。終了コードが 0 でなければ、出た文を返して止まる。
