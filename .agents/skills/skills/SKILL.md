---
name: skills
description: >-
  Lists Cursor skills registered for this user and for the current repository.
  Use when the user says /skills or asks which skills are registered.
disable-model-invocation: true
triggers: ["user"]
---

# skills

登録されているスキルの名前、説明、ファイルパスを出す。組み込みの `skills-cursor` と plugins は出さない。

この SKILL.md があるディレクトリで、次を実行する。標準出力をそのまま返す。

```bash
python3 list.py
```
