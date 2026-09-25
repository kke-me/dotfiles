# Skill は `.agents/skills/` に1つだけ置く

Cursor、Claude Code、Devin で同じ Skill を使うときの正本は、このリポジトリの `.agents/skills/`。形式は [Agent Skills](https://agentskills.io) の `SKILL.md`。3つのツールは同じファイルを読み、探しに行くディレクトリだけが違う。

初めての端末は「新しい端末では clone してから install.sh」までやれば使える。Skill の追加、Devin、同期しないものは、必要になった章だけ開く。用語は末尾にある。このファイルと `.bin/install.sh` が食い違ったら、`install.sh` を正にする。

## ツールごとの置き場所

| ツール | 読む場所 | 届け方 |
|---|---|---|
| Cursor | `~/.agents/skills/` と、プロジェクトの `.agents/skills/` | `install.sh` が `~/.agents` をこのリポジトリへ symlink する |
| Claude Code | `~/.claude/skills/` と、プロジェクトの `.claude/skills/` | `install.sh` が `~/.claude/skills` を `~/.agents/skills` へ symlink する。`~/.agents` 自体は読まない |
| Devin | 接続したリポジトリの `.agents/skills/` | このリポジトリを Devin に接続する。ホームは見ない |

`~/.cursor/skills/` に同じ Skill を置かない。Cursor は `~/.agents/skills/` を直接読むので、両方にあると同名が2回出る。`~/.cursor/skills-cursor/` は Cursor 本体の Skill なので、足さないし symlink もしない。

## 新しい端末では clone してから install.sh

```sh
git clone git@github.com:kke-me/dotfiles.git ~/Documents/dev/dotfiles
~/Documents/dev/dotfiles/.bin/install.sh
```

`install.sh` が張るリンクは4つ。`~/.claude` 本体は消さない。パスが実ディレクトリなら `~/.dotbackup/` へ退避してから張り替える。

1. `~/.agents` → このリポジトリの `.agents`
2. `~/.claude/skills` → `~/.agents/skills`
3. `~/.cursor/rules/pstack-sync.mdc` → `pstack/pstack-sync.mdc`
4. `~/.cursor/rules/natural-japanese.mdc` → `cursor/natural-japanese.mdc`

確認する。

```sh
readlink ~/.agents
readlink ~/.claude/skills
readlink ~/.cursor/rules/natural-japanese.mdc
ls ~/.agents/skills
```

期待する状態は次のとおり。

```text
~/.agents -> ~/Documents/dev/dotfiles/.agents
~/.claude/skills -> ~/.agents/skills
~/.agents/skills/<skill-name>/SKILL.md
```

Cursor で `/skills` を打つと、個人スキルと、今開いているリポジトリのスキルが出る。別のリポジトリへ手渡し用のファイルを置くときは `/handoff` を1回使う。できるのはリポジトリ直下の `HANDOFF/` で、中身は `STATE.md`、`BLOCKING.md`、`HUMAN.md`、`log.jsonl`。`.git/info/exclude` に `/HANDOFF/` が足され、git では追跡しない。`docs/` には置かない。

## 2回目以降は git pull でファイルが追従する

symlink の先は `git pull` で入れ替わる。既にあるリンクの張り直しは要らない。`install.sh` が新たに張るリンクが増えたときだけ、その端末で `install.sh` をもう一度実行する。`natural-japanese` のルールを足したときはこちらに当たる。

## Skill を足すときは名前をディレクトリと揃える

置く場所は次の形。

```text
.agents/skills/<skill-name>/SKILL.md
```

`name` は小文字、数字、ハイフンだけ。ディレクトリ名と一致させる。`description` はエージェントがスキルを選ぶ英語。`/skills` が出す日本語は `ja`。`ja` が無ければ `description` が出る。

```markdown
---
name: skill-name
description: What it does, and when to use it. Third person, with the trigger words.
ja: 何をするかと、いつ使うか。
---

# 手順
```

コミットして push し、他の端末で `git pull` する。

明示したときだけ動かしたい Skill は、次の2つを両方書く。Cursor と Claude Code は上の行を見る。Devin は下の行を見る。

```yaml
disable-model-invocation: true
triggers: ["user"]
```

Devin は同時に有効にできる Skill が1つだけなので、Skill の本文から別の Skill を呼ぶ手順は書かない。本文では Claude 専用の `${CLAUDE_SKILL_DIR}` や、実行時に展開される動的コマンドを使わない。スクリプトを同梱するときは、Skill ディレクトリからの相対パスで書く。

### natural-japanese は upstream の写し

[coji/natural-japanese](https://github.com/coji/natural-japanese) の `skills/natural-japanese` を、コミット `9a78a42` の時点でこのリポジトリに置いてある。こちらで足したのは `ja` と、リポジトリ直下から移した `LICENSE`。上げ直すときは upstream の同じパスでディレクトリを置き換え、`ja` と `LICENSE` は残す。`scripts/__pycache__` は入れない。`uv` は同梱していない。lint を回す端末では別に入れる。Cursor では `cursor/natural-japanese.mdc` が、日本語の文章の前にこの Skill を読ませる。

## そのリポジトリでしか意味がない手順は、そこに置く

起動、テスト、デプロイのように、そのリポジトリでしか使わない手順は、各リポジトリの `.agents/skills/` に置く。dotfiles に置くのは、端末が違っても自分に付いてくる Skill だけ。

そのプロジェクトを Claude Code でも開くなら、リポジトリの中に相対 symlink を1つ足す。リンク先はリポジトリの外にしない。Devin やクラウドの作業環境は `$HOME` を持ってこないので、ホームへの symlink は切れる。

```sh
mkdir -p .claude
ln -sfn ../.agents/skills .claude/skills
```

## Devin は接続したリポジトリしか見ない

組織の接続リポジトリに `kke-me/dotfiles` を追加する。Devin は `.agents/skills/*/SKILL.md` をインデックスし、セッションの開始時から名前と description を見る。前の章で相対 symlink をリポジトリ内に留めたのは、ホームを持ってこない環境でもリンクが切れないようにするため。

## Rules と MCP は、この symlink では揃わない

Skill 以外は、ツールごとに形式が違う。

- Cursor Rules、Claude の `CLAUDE.md` と rules、Devin の Knowledge と Playbook。pstack のモデル割り当て `pstack-models.mdc` もここには含まれない。例外は `install.sh` が `~/.cursor/rules/` へ張る2つ。`pstack/pstack-sync.mdc` は、表の生成を [pstack/sync-models.py](../pstack/sync-models.py) に任せるルール。`cursor/natural-japanese.mdc` は、日本語の文章を書くとき [natural-japanese](https://github.com/coji/natural-japanese) をクイックで読ませるルール
- MCP。Claude は JSON、他のツールは別ファイル
- hooks と、サブエージェントの定義

Playbook は Devin の UI にある、組織で共有するプロンプトの雛形。リポジトリに紐づく手順は Skill に書き、リポジトリに依らない雛形は Playbook に残す。

## 用語

| 用語 | ここでは |
|---|---|
| Skill | `SKILL.md` を持つ作業手順。エージェントが名前と description を見て開く |
| 正本 | 編集する実体。このリポジトリの `.agents/skills/` |
| `ja` | `/skills` が一覧に出す日本語。`description` はエージェントが選ぶとき用で、英語のまま残す |
| Playbook | Devin の UI 上の雛形。Skill とは別に置く |
