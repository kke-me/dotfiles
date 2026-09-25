---
name: kickoff
description: >-
  Reads AGENTS.md and handoff/STATE.md, locks the session to the single next
  task, and starts it. Use when the user says /kickoff or asks to start from
  handoff/STATE.md.
ja: AGENTS.md と handoff/STATE.md を読み、次の作業1件に範囲を固定して着手する。/kickoff と言うとき、または handoff/STATE.md から作業を始めたいときに使う。
disable-model-invocation: true
---

# kickoff

作業を始める前に範囲を固定する。`handoff/log.jsonl` は読まない。`AGENTS.md`、スキル、`docs/` にセッションログを書かない。

## 置く場所

手渡しファイルはリポジトリ直下の `handoff/` だけに置く。`docs/` とリポジトリ直下には置かない。

- `handoff/STATE.md`
- `handoff/BLOCKING.md`
- `handoff/HUMAN.md`
- `handoff/log.jsonl`

ファイルが無ければ、下の初期内容で作る。git リポジトリなら `.git/info/exclude` に `/handoff/` を足す。ステージしない。

## 読むもの

1. `AGENTS.md`
2. `handoff/STATE.md`
3. `handoff/BLOCKING.md`
4. `handoff/HUMAN.md`

`handoff/STATE.md` の初期内容:

```markdown
# 今

なし

# 次

なし
```

`handoff/BLOCKING.md` と `handoff/HUMAN.md` の初期値は `なし` の 1 行。

## 着手の条件

1. `handoff/BLOCKING.md` が `なし` でないなら、その内容を伝えて止まる。
2. 「次」が人間待ちなら、`handoff/HUMAN.md` を伝えて止まる。人間待ちかどうかは `handoff/HUMAN.md` にその項目があるかで決める。
3. `handoff/STATE.md` の「次」が `なし`、空、または未記載なら、何をするかを 1 行で聞いて止まる。範囲を自分で作らない。

## 開始

1. 「次」の文を、このセッションの範囲としてユーザーに 1 文で返す。
2. `handoff/STATE.md` の「今」をその文に置き換える。「次」は、開始時点で分かっている後続があればそれ、無ければ `なし`。100 行未満を保つ。完了済みの節は作らない。
3. 範囲をタスクに分け、最初のタスクから着手する。

## 終了前

1. 次のエージェントがログを読まずに着手できる一文を「次」に書く。続きが無ければ `なし`。
2. 終了を妨げている項目ができたときだけ `handoff/BLOCKING.md` をその項目に置き換える。解消したら `なし` に戻す。
3. 人間がやる項目ができたときだけ `handoff/HUMAN.md` にその項目を書く。エージェントはそれを実行しない。
4. 経緯を残す必要があるときだけ、`handoff/log.jsonl` に JSON を 1 行足す。`{"at":"<ISO>","next":"<次の一文>"}`。実装中にこのファイルを読み返さない。
