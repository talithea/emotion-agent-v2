# Security steps for leaked API keys

If an API key or secret was accidentally committed, follow these steps immediately.

1) Rotate the key (REQUIRED)
- Revoke the exposed key in the provider console and create a new key.
- Update your local `.env` with the new key.

2) Prevent future accidental commits
- Add a `.env` file and put secrets there. The repository already contains `.gitignore` with `.env`.
- Keep `.env` local and never commit it. Use `API_KEY` and `HF_TOKEN` environment variables in code.

3) Remove the secret from repository history (optional, destructive)
-- WARNING: Rewriting history will change commit hashes. Coordinate with collaborators.

Option A — `git-filter-repo` (recommended):

Install:
```powershell
pip install git-filter-repo
```

Remove the secret string (replace YOUR_SECRET with the exact key):
```powershell
git clone --mirror <repo-url> repo-mirror.git
cd repo-mirror.git
git-filter-repo --replace-text <(echo "YOUR_SECRET==>REDACTED")
# Push the rewritten history back (force)
git push --force --all
git push --force --tags
```

Option B — BFG Repo-Cleaner (simpler, needs Java):

Install: download the `bfg-<version>.jar` from the BFG releases.

Usage:
```powershell
git clone --mirror <repo-url> repo-mirror.git
cd repo-mirror.git
java -jar \path\to\bfg.jar --replace-text replacements.txt
# where replacements.txt contains the secret on a single line or use --delete-files for filenames
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force --all
git push --force --tags
```

4) After rewrite: notify collaborators
- Everyone must reclone or reset local branches. Provide them the new repo URL or advise `git fetch` + `git reset --hard origin/main`.

5) Verify removal
- Search the repo for the exposed key:
```powershell
git log --all -S"YOUR_SECRET"
```

If you want, I can perform the history rewrite here — please confirm explicitly. I will not run destructive history-rewrite commands without your permission.
