# dotfiles

Cursor、Claude Code、Devin で使う Agent Skill の正本。初めての端末と Skill の追加は [docs/agent-skills.md](docs/agent-skills.md)。pstack のコマンドと、いまのモデル割り当ては [pstack/README.md](pstack/README.md)。

## 登録されている Skill

この一覧は、このリポジトリをカレントにして `/skills` を実行した personal の節。各行は `SKILL.md` の `ja`。`ja` が無い Skill は `description` が出る。`description` はエージェントがスキルを選ぶための文なので、英語のものはそのまま残してある。別リポジトリの Skill は、そのディレクトリでもう一度 `/skills` を実行すると repo の節に出る。

## 自分で書いた Skill

実体は `.agents/skills/<name>/`。

- `/handoff`。現在の git リポジトリ直下に、git で追跡しない HANDOFF/ を置く。中身は STATE.md、BLOCKING.md、HUMAN.md、log.jsonl と、kickoff、state、blocking、human のスキル。.git/info/exclude に /HANDOFF/ を足す。/handoff と言うときに使う。
- `/pr-summary`。Git差分やユーザーが提示した変更内容を分析し、一定のフォーマットで日本語のPR概要を作成する。PR本文を準備するときに明示的に使用する。
- `/skills`。このユーザーと、今開いているリポジトリに登録されているスキルを一覧する。/skills と言うとき、または登録済みのスキルを確認したいときに使う。

## ありがたく利用させていただいている Skill

実体は `vendor/<name>/`。`.agents/skills/<name>` はそこへの相対 symlink で、ツールはこちらを読む。

- `/natural-japanese`。仕事の日本語を読みやすく書く・直す。議事録、レポート、ガイド、企画、メール、チャットの説明を書くときに使う。/natural-japanese と言うときも使う。

`/natural-japanese` は [coji/natural-japanese](https://github.com/coji/natural-japanese)（Copyright (c) 2026 coji、MIT）を参考にした写し。著作権表示と許諾文は `vendor/natural-japanese/LICENSE`。出典の説明は同じディレクトリの `NOTICE`。
