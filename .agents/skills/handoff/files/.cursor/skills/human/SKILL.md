---
name: human
description: >-
  Shows or sets handoff/HUMAN.md, the list of tasks only the human may do. Use
  when the user says /human.
disable-model-invocation: true
---

# human

`handoff/HUMAN.md` を扱う。リポジトリ直下や `docs/` には書かない。人間がやる項目だけを置く。エージェントはここに書いた項目を実行しない。`handoff/log.jsonl` は読まない。

ファイルが無ければ `なし` の 1 行で `handoff/HUMAN.md` を作る。git リポジトリなら `.git/info/exclude` に `/handoff/` を足し、ステージしない。

引数が無ければ、ファイルの内容をそのまま返す。

引数があれば、その項目を書く。ファイルが `なし` だけなら、その項目だけにする。ユーザーが完了を告げた項目は消す。残らなければ `なし` の 1 行にする。
