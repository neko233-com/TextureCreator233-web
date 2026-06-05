# gh-cli skill

This repo-local skill provides repeatable gh CLI commands for deployment troubleshooting.

## Prerequisites

1. Install GitHub CLI.
2. Authenticate:

```bash
gh auth login
```

3. Ensure you are in this repository root.

## Configure Cloudflare secrets for GitHub Actions

Set required repository secrets before running the deploy workflow:

```bash
gh secret set CLOUDFLARE_API_TOKEN
gh secret set CLOUDFLARE_ACCOUNT_ID
```

Optional secret if you want a custom project name in scripts:

```bash
gh secret set CLOUDFLARE_PROJECT_NAME
```

## Workflow operations

List workflows:

```bash
gh workflow list
```

Run deploy workflow manually:

```bash
gh workflow run "Cloudflare Pages Deploy"
```

List recent runs for this workflow:

```bash
gh run list --workflow "Cloudflare Pages Deploy" --limit 10
```

Watch latest run live:

```bash
gh run watch
```

View latest run logs:

```bash
gh run view --log
```

## Deployment visibility checks

Check latest commit and branch:

```bash
gh repo view --json defaultBranchRef
gh api repos/{owner}/{repo}/commits/main --jq .sha
```

Check Actions run conclusion quickly:

```bash
gh run list --workflow "Cloudflare Pages Deploy" --json databaseId,headSha,status,conclusion,createdAt --limit 5
```

## Common failure causes

- Missing Cloudflare secrets.
- Wrong Cloudflare Pages project name.
- Workflow disabled in repository settings.
- Branch protection blocking direct push to main.
