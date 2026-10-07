# Prompting Chef

**Ideas into production-ready prompts.**

Prompting Chef converts rough text, ideas, requirements, existing prompts, and AI outputs into production-ready prompts.

## Repository is the source of truth

This GitHub repository is the canonical source for the plugin package.

- Plugin manifest: `plugin.json`
- Compatibility manifest: `.codex-plugin/plugin.json`
- Skills: `skills/`
- Plugin icon/logo: `assets/gpt-icon.png`
- GitHub-backed marketplace: `.agents/plugins/marketplace.json`

## Install and keep it in sync with ChatGPT Desktop / Codex

This repository is prepared as a Git-backed marketplace source.

1. Connect GitHub to ChatGPT/Codex.
2. Add this marketplace/repository as a plugin marketplace.
3. Install **Prompting Chef** from the marketplace.
4. Keep the marketplace source on `main` to receive future commits.
5. After changes land in GitHub, refresh/upgrade the marketplace in the client so the installed copy picks up the new files.

For Codex CLI:

```bash
codex plugin marketplace add Vamsiindugu/Prompting-Chef --ref main
codex plugin marketplace upgrade prompting-chef-marketplace
```

For the ChatGPT desktop app, use the Plugins Directory and select the Git-backed marketplace source. The desktop client loads the plugin from the marketplace installation.

## Important GitHub ↔ ChatGPT limitation

GitHub is the canonical source, but a personal ChatGPT plugin does **not** currently follow arbitrary GitHub commits as an always-on personal cloud sync.

There are two supported models:

- **Git-backed local/repo marketplace:** ChatGPT Desktop/Codex can install from this Git source. Refresh/upgrade the marketplace after repository changes.
- **Workspace GitHub marketplace:** Workspace administrators can import this marketplace from GitHub, after which ChatGPT performs daily marketplace synchronization. This is the supported automatic cloud-sync path for workspace-managed plugins.

## Development

Update the plugin by editing the files in this repository. Keep `main` as the release branch for the marketplace entry.

Recommended release process:

1. Edit `skills/` or plugin metadata.
2. Validate the plugin structure.
3. Bump `version` in `plugin.json` and `.codex-plugin/plugin.json`.
4. Commit and push to `main`.
5. Refresh the marketplace in ChatGPT Desktop/Codex, or wait for the next workspace marketplace sync.

## License

MIT
