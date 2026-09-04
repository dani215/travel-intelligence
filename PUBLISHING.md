# Publishing to GitHub

This repository is prepared for a public GitHub repository named `travel-intelligence`.

## Recommended repository settings

- Visibility: public if the goal is community reuse.
- Repository name: `travel-intelligence`.
- Description: `Evidence-led local travel planning skill for Codex and ChatGPT.`
- Suggested topics: `codex`, `chatgpt`, `agent-skill`, `travel-planning`, `flight-search`, `local-travel`.
- Keep secrets, personal travel data, API keys, browser exports, and private source material out of the repository.

## Create and push

Create an empty repository on GitHub first, then run from this directory:

```bash
git init -b main
git add .
git commit -m "Initial release of Travel Intelligence skill"
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/travel-intelligence.git
git push -u origin main
```

If Git asks for an identity, configure it locally for this repository before committing:

```bash
git config user.name "Your Name"
git config user.email "your-email@example.com"
```

## Verify after publishing

Open the repository page and confirm that `SKILL.md`, `agents/openai.yaml`, all three reference files, `README.md`, `LICENSE`, and the validation workflow are visible. The Actions tab should show the validation workflow passing.

## Release practice

For future changes, update the capability index when a safe capability is promoted, run the local validator, commit with a meaningful message, and push to `main`. Changes involving booking, payment, private data, permissions, or autonomous actions must not be added silently.
