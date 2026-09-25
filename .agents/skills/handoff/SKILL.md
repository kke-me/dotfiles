---
name: handoff
description: >-
  Installs untracked handoff files into the current git repository. Creates
  STATE.md, BLOCKING.md, HUMAN.md, and the kickoff, state, blocking, and human
  skills, then lists them in .git/info/exclude. Use when the user says /handoff.
disable-model-invocation: true
triggers: ["user"]
---

# handoff

現在の git リポジトリに、手渡し用のファイルを置く。既存ファイルは上書きしない。`git add` もコミットもしない。`.gitignore` は変更しない。

この SKILL.md があるディレクトリで、次を実行する。

```bash
python3 install.py
```

標準出力をそのまま返す。終了コードが 0 でなければ、出た文を返して止まる。
