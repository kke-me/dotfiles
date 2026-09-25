# dotfiles

Cursor / Claude Code / Devin で共有する Agent Skill の正本。

手順は [docs/agent-skills.md](docs/agent-skills.md)。

pstack のコマンドと、いまのモデル割り当ては [pstack/README.md](pstack/README.md)。

## 登録されている Skill

`/skills` を、このリポジトリをカレントにして実行した personal の一覧。出る文は各 `SKILL.md` の `ja`。`description` はエージェント向けに英語のまま。今開いている別リポジトリの Skill は、そこでもう一度 `/skills` を実行すると repo の節に出る。

- `/handoff`。現在の git リポジトリ直下に、git で追跡しない HANDOFF/ を置く。中身は STATE.md、BLOCKING.md、HUMAN.md、log.jsonl と、kickoff、state、blocking、human のスキル。.git/info/exclude に /HANDOFF/ を足す。/handoff と言うときに使う。
- `/natural-japanese`。仕事の日本語を読みやすく書く・直す。議事録、レポート、ガイド、企画、メール、チャットの説明を書くときに使う。/natural-japanese と言うときも使う。
- `/pr-summary`。Git差分やユーザーが提示した変更内容を分析し、一定のフォーマットで日本語のPR概要を作成する。PR本文を準備するときに明示的に使用する。
- `/skills`。このユーザーと、今開いているリポジトリに登録されているスキルを一覧する。/skills と言うとき、または登録済みのスキルを確認したいときに使う。
