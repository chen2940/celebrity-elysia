#!/usr/bin/env bash
# =============================================================================
# celebrity-elysia — one-line installer (bash / macOS-Linux)
#
#   curl -fsSL https://raw.githubusercontent.com/chen2940/celebrity-elysia/main/install.sh | bash
#
# Optional args (passed to tools/install.py), e.g.:
#   ... | bash -s -- --host claude-code,workbuddy --force
# =============================================================================
set -euo pipefail

REPO="chen2940/celebrity-elysia"
BRANCH="main"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "$TMP_DIR"' EXIT

echo "==> Downloading celebrity-elysia (${BRANCH}) from GitHub ..."
if command -v curl >/dev/null 2>&1; then
  curl -fsSL "https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz" -o "${TMP_DIR}/skill.tar.gz"
else
  wget -q "https://github.com/${REPO}/archive/refs/heads/${BRANCH}.tar.gz" -O "${TMP_DIR}/skill.tar.gz"
fi

echo "==> Extracting ..."
tar -xzf "${TMP_DIR}/skill.tar.gz" -C "${TMP_DIR}"
SKILL_SRC="${TMP_DIR}/celebrity-elysia-${BRANCH}"

if [ ! -f "${SKILL_SRC}/SKILL.md" ]; then
  echo "!! Downloaded archive does not look like a skill repo (no SKILL.md)." >&2
  exit 1
fi

PY=""
for candidate in python3 python; do
  if command -v "${candidate}" >/dev/null 2>&1; then
    PY="${candidate}"
    break
  fi
done

if [ -z "${PY}" ]; then
  echo "!! Python 3 is required. Install it, then run again." >&2
  exit 1
fi

echo "==> Installing (python: ${PY}) ..."
"${PY}" "${SKILL_SRC}/tools/install.py" --source "${SKILL_SRC}" "$@"

echo "==> Done."
