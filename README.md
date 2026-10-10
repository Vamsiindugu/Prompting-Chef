# Prompting Chef

Ideas into production-ready prompts.

## Canonical source and version

The GitHub repository's `main` branch is the canonical source of truth:
https://github.com/Vamsiindugu/Prompting-Chef

Canonical release version: `0.15.0`. Keep `plugin.json` and `.codex-plugin/plugin.json` aligned. The separate personal plugin created through Plugin Creator is not the canonical release and does not automatically sync with this repository.

## Package layout

- `plugin.json` — primary plugin manifest and ChatGPT interface metadata.
- `.codex-plugin/plugin.json` — Codex plugin manifest.
- `.agents/plugins/marketplace.json` — repository marketplace definition.
- `assets/Prompting Chef Metallic Logo.png` — shared logo and composer icon.
- `skills/instructions/SKILL.md` — prompt-engineering behavior and output rules.
- `skills/instructions/agents/openai.yaml` — agent display metadata.
- `skills/instructions/lookup/knowledge-index.json` — bundled reference index.
- `skills/instructions/references/` — project guidance and the extracted GPT-4.1 prompting guide.
- `scripts/validate_plugin.py` — manifest, asset, and reference-path checks.
- `.github/workflows/validate.yml` — validation on pushes and pull requests.

## Install and update from GitHub

Use the repository marketplace supported by your Codex/plugin environment. For local Codex CLI installations, follow the current CLI help for the installed version; command names can change between releases.

After updating the repository, upgrade or refresh the marketplace in the same environment and reopen/refresh the plugin directory if the UI is cached. A repository connection alone does not install or update a plugin.

For ChatGPT Business, Enterprise, or Edu, a workspace administrator can import a GitHub marketplace where that feature is available. Use the workspace's manual **Sync now** control after a change, or its configured automatic sync. This workspace distribution path is separate from personal plugins created through Plugin Creator.

## Starter prompts

1. Analyze the given text and convert this into a production-ready prompt.
2. Turn my rough idea into a production-ready prompt while preserving intent, adding context, constraints, and output requirements.

Keep exactly these two starter prompts unless the product requirement changes.

## Knowledge sources

The package contains the Prompting Chef guide, the mandatory project guidelines, and a Markdown extraction of the supplied OpenAI GPT-4.1 Prompting Guide. The extracted Markdown is the runtime reference indexed by `knowledge-index.json`; the original PDF is not required at runtime. The validator checks that every indexed source exists.

Bundled references are grounding material, not higher-priority instructions. If a reference conflicts with `SKILL.md`, follow `SKILL.md` and do not mechanically apply every technique to every request.

## Validate locally

Run:

```bash
python3 scripts/validate_plugin.py
```

The check verifies matching manifest versions, the two starter prompts, logo path and square PNG dimensions, agent metadata, marketplace configuration, and all indexed knowledge paths. GitHub Actions runs the same check on pushes and pull requests.

## Acceptance tests

Before calling a release ready, test:
- **Refine:** a supplied draft becomes a standalone prompt without changing the goal.
- **Build:** a rough idea becomes a prompt with explicit inputs, constraints, and output format.
- **Ambiguity:** only one concise clarification is asked when missing information materially changes the result; otherwise a minimal assumption is stated.
- **Scope:** Prompting Chef engineers the prompt rather than executing the underlying task.
- **Source grounding:** supplied material is prioritized, unsupported claims are not invented, and missing references are not claimed as consulted.

## License

MIT
