---
name: blocking
description: >-
  Shows or sets HANDOFF/BLOCKING.md, the barrier that stops the current work.
  Use when the user says /blocking.
ja: HANDOFF/BLOCKING.md を表示する。引数があればファイル全体をその文に置き換える。/blocking と言うときに使う。
disable-model-invocation: true
---

# blocking

`HANDOFF/BLOCKING.md` を扱う。リポジトリ直下や `docs/` には書かない。作業を終えるのを妨げている項目だけを置く。経緯は書かない。`HANDOFF/log.jsonl` は読まない。

ファイルが無ければ `なし` の 1 行で `HANDOFF/BLOCKING.md` を作る。git リポジトリなら `.git/info/exclude` に `/HANDOFF/` を足し、ステージしない。

引数が無ければ、ファイルの内容をそのまま返す。

引数があれば、その文でファイル全体を置き換える。解消の指示なら `なし` の 1 行にする。`なし` でないあいだ、実装は始めない。
