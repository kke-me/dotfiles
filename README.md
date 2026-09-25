# dotfiles

Cursor / Claude Code / Devin で共有する Agent Skill の正本。

手順は [docs/agent-skills.md](docs/agent-skills.md)。

## 登録されている Skill

`/skills` を、このリポジトリをカレントにして実行した personal の一覧。説明文は各 `SKILL.md` の `description`。今開いている別リポジトリの Skill は、そこでもう一度 `/skills` を実行すると repo の節に出る。

- `/handoff`。Installs untracked handoff files into the current git repository. Creates STATE.md, BLOCKING.md, HUMAN.md, and the kickoff, state, blocking, and human skills, then lists them in .git/info/exclude. Use when the user says /handoff.
- `/pr-summary`。Git差分やユーザーが提示した変更内容を分析し、一定のフォーマットで日本語のPR概要を作成する。PR本文を準備するときに明示的に使用する。
- `/skills`。Lists Cursor skills registered for this user and for the current repository. Use when the user says /skills or asks which skills are registered.
