---
name: skills
description: >-
  Lists Cursor skills registered for this user and for the current repository.
  Use when the user says /skills or asks which skills are registered.
ja: このユーザーと、今開いているリポジトリに登録されているスキルを一覧する。/skills と言うとき、または登録済みのスキルを確認したいときに使う。
disable-model-invocation: true
triggers: ["user"]
---

# skills

登録されているスキルの名前、説明、ファイルパスを出す。説明は frontmatter の `ja` を出す。`ja` が無ければ `description` を出す。`description` は英語のままにする。組み込みの `skills-cursor` と plugins は出さない。

この SKILL.md があるディレクトリで、次を実行する。標準出力をそのまま返す。

```bash
python3 list.py
```
