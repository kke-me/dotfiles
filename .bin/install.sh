#!/usr/bin/env bash
set -ue

helpmsg() {
  command echo "Usage: $0 [--help | -h]" 0>&2
  command echo ""
}

link_agent_skills() {
  # ~/.agents は link_to_homedir が dotfiles/.agents へ張る。
  # Claude Code は ~/.claude/skills しか読まないので、そこだけ追加で張る。
  # ~/.claude 自体は sessions 等があるため置き換えない。
  local agents_skills="$HOME/.agents/skills"
  local claude_skills="$HOME/.claude/skills"

  if [ ! -d "$agents_skills" ]; then
    command echo "skip claude skills link: $agents_skills not found"
    return 0
  fi

  command mkdir -p "$HOME/.claude" "$HOME/.dotbackup"

  if [ -L "$claude_skills" ]; then
    command rm -f "$claude_skills"
  elif [ -e "$claude_skills" ]; then
    command mv "$claude_skills" "$HOME/.dotbackup/claude-skills.bak"
  fi

  command ln -sfn "$agents_skills" "$claude_skills"
  command echo "linked $claude_skills -> $agents_skills"
}

link_to_homedir() {
  command echo "backup old dotfiles..."
  if [ ! -d "$HOME/.dotbackup" ];then
    command echo "$HOME/.dotbackup not found. Auto Make it"
    command mkdir "$HOME/.dotbackup"
  fi

  local script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
  local dotdir=$(dirname ${script_dir})
  if [[ "$HOME" != "$dotdir" ]];then
    for f in $dotdir/.??*; do
      [[ `basename $f` == ".git" ]] && continue
      if [[ -L "$HOME/`basename $f`" ]];then
        command rm -f "$HOME/`basename $f`"
      fi
      if [[ -e "$HOME/`basename $f`" ]];then
        command mv "$HOME/`basename $f`" "$HOME/.dotbackup"
      fi
      command ln -snf $f $HOME
    done
  else
    command echo "same install src dest"
  fi
}

while [ $# -gt 0 ];do
  case ${1} in
    --debug|-d)
      set -uex
      ;;
    --help|-h)
      helpmsg
      exit 1
      ;;
    *)
      ;;
  esac
  shift
done

link_to_homedir
link_agent_skills
git config --global include.path "~/.gitconfig_shared"
command echo -e "\e[1;36m Install completed!!!! \e[m"
