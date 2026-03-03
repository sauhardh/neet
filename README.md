# For local running of scripts

export AUTHOR=$(git log -1 --pretty=%an)
export COMMIT_MESSAGE=$(git log -1 --pretty=%B)
export COMMIT_SHA=$(git rev-parse HEAD)
export FILES=$(git diff-tree --no-commit-id --name-only -r HEAD)

python scripts/send_to_discord.py
