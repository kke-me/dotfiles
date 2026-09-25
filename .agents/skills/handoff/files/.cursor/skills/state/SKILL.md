---
name: state
description: >-
  Shows or updates HANDOFF/STATE.md, current work and next work only. Use when
  the user says /state.
ja: HANDOFF/STATE.md の今と次だけを表示する。引数があれば次だけをその文に置き換える。/state と言うときに使う。
disable-model-invocation: true
---

# state

`HANDOFF/STATE.md` だけを扱う。リポジトリ直下や `docs/` には書かない。完了済みは書かない。100 行未満に保つ。`HANDOFF/log.jsonl` は読まない。`AGENTS.md`、スキル、`docs/` にセッションログを書かない。

ファイルが無ければ、次の内容で `HANDOFF/STATE.md` を作る。git リポジトリなら `.git/info/exclude` に `/HANDOFF/` を足し、ステージしない。

```markdown
# 今

なし

# 次

なし
```

引数が無ければ、「今」と「次」をそのまま返す。

引数があれば、その文で「次」だけを置き換える。「今」は変えない。置き換えたあとの「今」と「次」を返す。
