#!/usr/bin/env bash
#
# commit.sh — run this from YOUR OWN terminal in the IceCapade folder.
# (Not from the Cowork sandbox: that mount can create files but not delete
#  them, so git's lock/temp files pile up there. Your terminal deletes fine.)
#
# Commits AND pushes to 'origin' by default, so the remote is always current.
#
# Usage:
#   ./commit.sh "commit message"                     # commit tracked changes + push
#   ./commit.sh "commit message" lyx/ notes.txt      # also add these paths, + push
#   ./commit.sh "commit message" --tag V.1.1         # move/create a tag, + push
#   ./commit.sh "commit message" --no-push           # commit only, don't push
#   (flags and paths can be combined in any order)
#
set -euo pipefail
cd "$(dirname "$0")"

# --- 1. Clear anything the sandbox left behind and couldn't remove ---
rm -f .git/index.lock .git/HEAD.lock .git/config.lock 2>/dev/null || true
rm -f .git/refs/tags/*.lock .git/refs/heads/*.lock 2>/dev/null || true
find .git/objects -name 'tmp_obj_*' -delete 2>/dev/null || true
rm -f .__deltest_root .git/__deltest_git 2>/dev/null || true   # stray test files

# --- 2. Parse args: first bare word = message, other bare words = paths ---
MSG=""; TAG=""; PUSH=1; PATHS=()
while [ $# -gt 0 ]; do
  case "$1" in
    --tag)     TAG="${2:?--tag needs a name}"; shift 2;;
    --no-push) PUSH=0; shift;;
    --push)    PUSH=1; shift;;   # accepted for compatibility; push is the default
    -h|--help)
      echo 'Usage: ./commit.sh "message" [path ...] [--tag NAME] [--no-push]'; exit 0;;
    *) if [ -z "$MSG" ]; then MSG="$1"; else PATHS+=("$1"); fi; shift;;
  esac
done
if [ -z "$MSG" ]; then
  echo 'Need a commit message. Usage: ./commit.sh "message" [path ...] [--tag NAME] [--no-push]'
  exit 1
fi

# --- 3. Stage ---
if [ ${#PATHS[@]} -gt 0 ]; then
  git add -- "${PATHS[@]}"
else
  git add -u          # only already-tracked changes; won't sweep in stray files
fi

# --- 4. Commit ---
if git diff --cached --quiet; then
  echo "Nothing new staged; skipping commit."
else
  git commit -m "$MSG"
  echo "Committed $(git rev-parse --short HEAD)"
fi

# --- 5. Tag (optional; -f moves an existing tag) ---
if [ -n "$TAG" ]; then
  git tag -f "$TAG" -m "$TAG"
  echo "Tag $TAG -> $(git rev-parse --short HEAD)"
fi

# --- 6. Push (default; disable with --no-push) ---
if [ "$PUSH" -eq 1 ]; then
  if git remote | grep -q .; then
    git push origin HEAD
    [ -n "$TAG" ] && git push -f origin "$TAG"
    echo "Pushed to origin — remote is up to date."
  else
    echo "No remote configured yet — see REMOTE_SETUP.md. Skipping push."
  fi
fi

echo "--- recent history ---"
git --no-pager log --oneline -3
echo "Done."
