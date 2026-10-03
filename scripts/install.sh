#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="${CODEX_HOME:-$HOME/.codex}/skills"
FORCE=0

usage() {
  cat <<'EOF'
usage: ./scripts/install.sh [--force] all
       ./scripts/install.sh [--force] <skill> [<skill> ...]

Installs bundled skills into ${CODEX_HOME:-$HOME/.codex}/skills.
Existing skill directories stay unchanged by default. Use --force to replace them.
EOF
}

if [[ $# -eq 0 ]]; then
  usage
  exit 2
fi

if [[ "${1:-}" == "--force" ]]; then
  FORCE=1
  shift
fi

if [[ $# -eq 0 ]]; then
  usage
  exit 2
fi

mkdir -p "$DEST"

if [[ "$1" == "all" ]]; then
  if [[ $# -ne 1 ]]; then
    echo "error: 'all' cannot be combined with named skills" >&2
    exit 2
  fi
  mapfile -t SKILLS < <(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort)
else
  SKILLS=("$@")
fi

for skill in "${SKILLS[@]}"; do
  src="$ROOT/skills/$skill"
  dst="$DEST/$skill"

  if [[ ! -f "$src/SKILL.md" ]]; then
    echo "error: unknown skill: $skill" >&2
    exit 1
  fi

  if [[ -e "$dst" ]]; then
    if [[ "$FORCE" -ne 1 ]]; then
      echo "error: $dst already exists (use --force to replace)" >&2
      exit 1
    fi
    rm -rf "$dst"
  fi

  cp -R "$src" "$dst"
  echo "installed $skill -> $dst"
done
