# Private remote setup (one time)

Goal: an offsite, private copy of the whole repo (history + tags) so the
manuscript exists in more than one place and any other machine just clones it.

Do all of this from **your own terminal** in the IceCapade folder — not the
Cowork sandbox (the sandbox can't delete files, so git jams there).

## 1. Create an empty PRIVATE repo

Pick a host (GitHub shown; GitLab/Bitbucket work the same way).

- Web UI: New repository → name it e.g. `IceCapade` → **Private** →
  do NOT add a README, .gitignore, or license (keep it empty).
- Or with the GitHub CLI, from the folder:

      gh repo create IceCapade --private --source=. --remote=origin --push

  (If you use `gh`, it does steps 2–3 for you; skip to "Verify".)

## 2. Point this repo at it

SSH (recommended — no password prompts once your key is set up):

    git remote add origin git@github.com:YOURUSER/IceCapade.git

or HTTPS (will prompt for a Personal Access Token as the password):

    git remote add origin https://github.com/YOURUSER/IceCapade.git

## 3. Push everything, including tags

    git push -u origin main
    git push origin --tags

## Verify

    git remote -v
    git ls-remote --tags origin   # should list the ms-* tags

## Everyday use after this

    ./commit.sh "your message" --push          # commit + push
    ./commit.sh "your message" --tag V.1.1 --push

## On another machine

    git clone git@github.com:YOURUSER/IceCapade.git
    # everything — history and all tags — comes with it.

## Auth notes

- SSH key not set up yet? `ssh-keygen -t ed25519 -C "lenberman@gmail.com"`,
  then add `~/.ssh/id_ed25519.pub` under the host's SSH-keys settings.
- HTTPS uses a Personal Access Token (classic or fine-grained with repo
  scope) in place of a password.
