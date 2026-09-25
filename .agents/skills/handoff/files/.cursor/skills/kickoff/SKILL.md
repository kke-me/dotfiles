---
name: kickoff
description: >-
  Reads AGENTS.md and HANDOFF/STATE.md, locks the session to the single next
  task, and starts it. Use when the user says /kickoff or asks to start from
  HANDOFF/STATE.md.
ja: AGENTS.md と HANDOFF/STATE.md を読み、次の作業1件に範囲を固定して着手する。/kickoff と言うとき、または HANDOFF/STATE.md から作業を始めたいときに使う。
disable-model-invocation: true
---

# kickoff

作業を始める前に範囲を固定する。`HANDOFF/log.jsonl` は読まない。`AGENTS.md`、スキル、`docs/` にセッションログを書かない。

## 置く場所

手渡しファイルはリポジトリ直下の `HANDOFF/` だけに置く。`docs/` とリポジトリ直下には置かない。

- `HANDOFF/STATE.md`
- `HANDOFF/BLOCKING.md`
- `HANDOFF/HUMAN.md`
- `HANDOFF/log.jsonl`

ファイルが無ければ、下の初期内容で作る。git リポジトリなら `.git/info/exclude` に `/HANDOFF/` を足す。ステージしない。

## 読むもの

1. `AGENTS.md`
2. `HANDOFF/STATE.md`
3. `HANDOFF/BLOCKING.md`
4. `HANDOFF/HUMAN.md`

`HANDOFF/STATE.md` の初期内容:

```markdown
# 今

なし

# 次

なし
```

`HANDOFF/BLOCKING.md` と `HANDOFF/HUMAN.md` の初期値は `なし` の 1 行。

## 着手の条件

1. `HANDOFF/BLOCKING.md` が `なし` でないなら、その内容を伝えて止まる。
2. 「次」が人間待ちなら、`HANDOFF/HUMAN.md` を伝えて止まる。人間待ちかどうかは `HANDOFF/HUMAN.md` にその項目があるかで決める。
3. `HANDOFF/STATE.md` の「次」が `なし`、空、または未記載なら、何をするかを 1 行で聞いて止まる。範囲を自分で作らない。

## 開始

1. 「次」の文を、このセッションの範囲としてユーザーに 1 文で返す。
2. `HANDOFF/STATE.md` の「今」をその文に置き換える。「次」は、開始時点で分かっている後続があればそれ、無ければ `なし`。100 行未満を保つ。完了済みの節は作らない。
3. 範囲をタスクに分け、最初のタスクから着手する。

## 終了前

1. 次のエージェントがログを読まずに着手できる一文を「次」に書く。続きが無ければ `なし`。
2. 終了を妨げている項目ができたときだけ `HANDOFF/BLOCKING.md` をその項目に置き換える。解消したら `なし` に戻す。
3. 人間がやる項目ができたときだけ `HANDOFF/HUMAN.md` にその項目を書く。エージェントはそれを実行しない。
4. 経緯を残す必要があるときだけ、`HANDOFF/log.jsonl` に JSON を 1 行足す。`{"at":"<ISO>","next":"<次の一文>"}`。実装中にこのファイルを読み返さない。
