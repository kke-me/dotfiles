---
name: kickoff
description: >-
  Reads AGENTS.md and STATE.md, locks the session to the single next task, and
  starts it. Use when the user says /kickoff or asks to start from STATE.md.
disable-model-invocation: true
---

# kickoff

作業を始める前に範囲を固定する。`log.jsonl` は読まない。`AGENTS.md`、スキル、`docs/` にセッションログを書かない。

## 読むもの

リポジトリ直下の次だけを読む。

1. `AGENTS.md`
2. `STATE.md`
3. `BLOCKING.md`
4. `HUMAN.md`

ファイルが無ければ、次の中身で作る。git リポジトリなら `.git/info/exclude` に `/STATE.md`、`/BLOCKING.md`、`/HUMAN.md`、`/log.jsonl` を足す。ステージしない。

```markdown
# 今

なし

# 次

なし
```

`BLOCKING.md` と `HUMAN.md` の初期値は `なし` の 1 行。

## 着手の条件

1. `BLOCKING.md` が `なし` でないなら、その内容を伝えて止まる。
2. 「次」が人間待ちなら、`HUMAN.md` を伝えて止まる。人間待ちかどうかは `HUMAN.md` にその項目があるかで決める。
3. `STATE.md` の「次」が `なし`、空、または未記載なら、何をするかを 1 行で聞いて止まる。範囲を自分で作らない。

## 開始

1. 「次」の文を、このセッションの範囲としてユーザーに 1 文で返す。
2. `STATE.md` の「今」をその文に置き換える。「次」は、開始時点で分かっている後続があればそれ、無ければ `なし`。100 行未満を保つ。完了済みの節は作らない。
3. 範囲をタスクに分け、最初のタスクから着手する。

## 終了前

1. 次のエージェントがログを読まずに着手できる一文を「次」に書く。続きが無ければ `なし`。
2. 終了を妨げている項目ができたときだけ `BLOCKING.md` をその項目に置き換える。解消したら `なし` に戻す。
3. 人間がやる項目ができたときだけ `HUMAN.md` にその項目を書く。エージェントはそれを実行しない。
4. 経緯を残す必要があるときだけ、`log.jsonl` に JSON を 1 行足す。`{"at":"<ISO>","next":"<次の一文>"}`。実装中にこのファイルを読み返さない。
