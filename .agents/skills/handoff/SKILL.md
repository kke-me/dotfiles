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

この SKILL.md があるディレクトリで、次を実行する。

```bash
python3 install.py
```

標準出力をそのまま返す。終了コードが 0 でなければ、出た文を返して止まる。
