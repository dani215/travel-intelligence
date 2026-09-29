# Publishing and maintenance

This repository is the source package for the `travel-intelligence` Agent Plugins 1.0 plugin.

## Package layout

The repository root is the plugin root. It contains `plugin.json` and `skills/travel-intelligence/SKILL.md`; compatible clients discover the skill at that fixed location. Installation and marketplace registration remain client-specific.

## Before publishing a change

1. Run `python scripts/validate_plugin.py .`.
2. Review the capability index when promoting a safe, reusable capability.
3. Keep credentials, private travel data, browser exports, and API keys out of the repository.
4. Update the semantic version in `plugin.json` for a release.
5. Commit the change and push it to `main`.

Changes involving booking, payment, private data, permissions, external tools, or autonomous actions must not be added silently.
