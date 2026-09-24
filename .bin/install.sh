#!/usr/bin/env bash
set -ue

# Cursor は ~/.agents/skills、Claude Code は ~/.claude/skills を読む。
# 正本はリポジトリの .agents/skills。~/.claude 本体は置き換えない。

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd -P)"
agents="$HOME/.agents"
claude_skills="$HOME/.claude/skills"

backup_existing() {
  local path="$1"
  local name="$2"
  if [ -L "$path" ]; then
    command rm -f "$path"
  elif [ -e "$path" ]; then
    command mkdir -p "$HOME/.dotbackup"
    command mv "$path" "$HOME/.dotbackup/${name}.bak"
  fi
}

backup_existing "$agents" "agents"
command ln -sfn "$root/.agents" "$agents"

command mkdir -p "$HOME/.claude"
backup_existing "$claude_skills" "claude-skills"
command ln -sfn "$agents/skills" "$claude_skills"

command echo "linked $agents -> $root/.agents"
command echo "linked $claude_skills -> $agents/skills"
