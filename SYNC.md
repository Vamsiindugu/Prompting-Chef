# Prompting Chef — source and sync policy

## Source of truth

- Canonical source: https://github.com/Vamsiindugu/Prompting-Chef
- Canonical branch: `main`
- Canonical version: `0.15.0`
- Keep `plugin.json` and `.codex-plugin/plugin.json` versions and starter prompts aligned.
- Do not create another Plugin Creator copy to represent a GitHub release. Personal Plugin Creator releases are separate from the GitHub repository and do not automatically sync.

## Local / Codex distribution

1. Pull or clone the canonical repository.
2. Install the repository marketplace using the command supported by the installed Codex CLI version (check `codex plugin marketplace --help`).
3. After repository changes, upgrade the marketplace using the command shown by that CLI version.
4. Refresh/reopen the plugin directory if cached metadata or assets remain stale.
5. Run `python3 scripts/validate_plugin.py` before committing.

## Workspace distribution

Where GitHub marketplace import is supported, a workspace administrator imports this repository from the workspace plugin settings. After changes, use the marketplace's manual **Sync now** control or its configured automatic sync. Confirm the displayed version and logo after sync.

## Troubleshooting

- **Old version shown:** confirm the marketplace points to this repository and the `main` branch; then run the supported upgrade/sync operation and refresh the UI.
- **Wrong or missing logo:** confirm the two manifests point to `./assets/Prompting Chef Metallic Logo.png`, that the file exists and is square, then sync/refresh.
- **Missing knowledge guidance:** verify each entry in `skills/instructions/lookup/knowledge-index.json` points to a file under `skills/instructions/references/`; run the validator.
- **Changes not reflected in a personal plugin:** the personal Plugin Creator release is independent. Updating GitHub does not update that release.
