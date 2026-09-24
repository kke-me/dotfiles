# Agent Skill の共有

Cursor、Claude Code、Devin で同じ Skill を使う。正本はこのリポジトリの `.agents/skills/` だけで、コピーは置かない。

Skill の形式は [Agent Skills](https://agentskills.io) の `SKILL.md` で、3ツールとも同じファイルを読める。読みに行くディレクトリだけが違う。

| ツール | 読む場所 | このリポジトリでの届け方 |
|---|---|---|
| Cursor | `~/.agents/skills/`、プロジェクトの `.agents/skills/` | `install.sh` が `~/.agents` をこのリポジトリへ symlink する |
| Devin | 接続リポジトリ内の `.agents/skills/` | このリポジトリを Devin に接続する。ホームディレクトリは見ない |
| Claude Code | `~/.claude/skills/`、プロジェクトの `.claude/skills/` | `install.sh` が `~/.claude/skills` だけを `~/.agents/skills` へ symlink する。`.agents/skills` 自体は読まない |

`~/.cursor/skills/` にも同じ実体を置かない。Cursor は `~/.agents/skills/` を直接読むので、両方にあると同名 Skill が二重に出る。`~/.cursor/skills-cursor/` は Cursor 本体の Skill なので、追加も symlink もしない。

## 新しい端末

```sh
git clone git@github.com:kke-me/dotfiles.git ~/Documents/dev/dotfiles
~/Documents/dev/dotfiles/.bin/install.sh
```

`install.sh` は次をする。

1. リポジトリ直下のドットファイルを `$HOME` へ symlink する。`.agents` もここに含まれる。
2. `~/.claude` は消さない。`~/.claude/skills` が実ディレクトリなら `~/.dotbackup/claude-skills.bak` へ退避してから、`~/.agents/skills` への symlink に置き換える。

確認:

```sh
readlink ~/.agents
readlink ~/.claude/skills
ls ~/.agents/skills
```

期待する状態:

```text
~/.agents -> ~/Documents/dev/dotfiles/.agents
~/.claude/skills -> ~/.agents/skills
~/.agents/skills/<skill-name>/SKILL.md
```

更新は `git pull` だけ。symlink の先が変わるので、リンクの張り直しは不要。

## Skill を足す

```text
.agents/skills/<skill-name>/SKILL.md
```

`name` はディレクトリ名と一致させる。小文字・数字・ハイフンのみ。

```markdown
---
name: skill-name
description: 何をするかと、いつ使うか。三人称で、トリガーになる語を入れる。
---

# 手順
```

コミットして push し、他の端末で `git pull` する。

明示したときだけ動かしたい Skill は、次の2つを両方書く。Cursor と Claude Code は上、Devin は下を見る。

```yaml
disable-model-invocation: true
triggers: ["user"]
```

Devin は同時に有効にできる Skill が1つだけなので、Skill から別 Skill を呼ぶ手順は書かない。

本文では Claude 専用の `${CLAUDE_SKILL_DIR}` や動的コマンド展開を使わない。スクリプトを同梱するときは、Skill ディレクトリからの相対パスで書く。

## プロジェクト固有の Skill

そのリポジトリでしか意味がない手順（起動方法、テスト、デプロイ）は、各リポジトリの `.agents/skills/` に置く。ここ（dotfiles）には、端末が違っても自分に付いてくる Skill だけを置く。

そのプロジェクトを Claude Code でも開くなら、リポジトリ内に相対 symlink を1つ足す。

```sh
mkdir -p .claude
ln -sfn ../.agents/skills .claude/skills
```

リンク先はリポジトリの外にしない。Devin やクラウド上の作業環境は `$HOME` を持ってこないので、ホームへの symlink は切れる。

## Devin

組織の接続リポジトリに `kke-me/dotfiles` を追加する。Devin は接続リポジトリの `.agents/skills/*/SKILL.md` をインデックスし、セッション開始時から名前と description を見る。

このリポジトリにはシェル設定も入っている。Skill 以外を Devin に読ませたくなくなったら、`.agents/skills/` だけを別リポジトリへ切り出し、`install.sh` のリンク先をそちらに変える。それまでは分けない。

## 同期しないもの

Skill 以外の設定は形式が違うので、この仕組みでは揃えない。

- Cursor Rules、Claude の `CLAUDE.md` / rules、Devin の Knowledge と Playbook
- MCP。Claude は JSON、他ツールは別ファイル
- hooks、サブエージェント定義

Playbook は Devin の UI 上にある組織共通のプロンプト雛形。リポジトリの手順は Skill、リポジトリに依存しない雛形は Playbook。
