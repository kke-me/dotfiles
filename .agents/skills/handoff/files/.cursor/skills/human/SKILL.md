---
name: human
description: >-
  Shows or sets HUMAN.md, the list of tasks only the human may do. Use when
  the user says /human.
disable-model-invocation: true
---

# human

リポジトリ直下の `HUMAN.md` を扱う。人間がやる項目だけを置く。エージェントはここに書いた項目を実行しない。`log.jsonl` は読まない。

ファイルが無ければ `なし` の 1 行で作る。git リポジトリなら `.git/info/exclude` に `/HUMAN.md` を足し、ステージしない。

引数が無ければ、ファイルの内容をそのまま返す。

引数があれば、その項目を書く。ファイルが `なし` だけなら、その項目だけにする。ユーザーが完了を告げた項目は消す。残らなければ `なし` の 1 行にする。
