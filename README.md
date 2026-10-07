# Prompting Chef

Ideas into production-ready prompts.

## Canonical source

GitHub main is the source of truth:
https://github.com/Vamsiindugu/Prompting-Chef

## Production layout

- plugin.json
- .codex-plugin/plugin.json
- .agents/plugins/marketplace.json
- assets/Prompting Chef Metallic Logo.png
- skills/instructions/SKILL.md
- skills/instructions/agents/openai.yaml
- skills/instructions/lookup/knowledge-index.json
- skills/instructions/references/

## Install from GitHub

For ChatGPT Desktop/Codex, add the repository marketplace:

codex plugin marketplace add Vamsiindugu/Prompting-Chef --ref main

Then install Prompting Chef from the Plugins Directory. After repository changes, run:

codex plugin marketplace upgrade prompting-chef-marketplace

Restart or refresh the Plugins Directory when necessary because installed plugins are cached locally.

For ChatGPT Business, Enterprise, or Edu, a workspace administrator can import this repository as a GitHub marketplace. OpenAI supports daily sync for imported marketplaces and a manual Sync now action.

## Starter prompts

1. Analyze the given text and convert this into a production-ready prompt.
2. Turn my rough idea into a production-ready prompt while preserving intent, adding context, constraints, and output requirements.

## Knowledge sources

The skill includes the Prompting Chef Guide, mandatory guidelines, and a Markdown extraction of the supplied OpenAI GPT-4.1 Prompting Guide. The PDF was used as the source for that extraction; this repository stores the extracted Markdown because the available GitHub write path is text-oriented.

## Development

Keep plugin.json and .codex-plugin/plugin.json on the same version. Keep only the two starter prompts. Keep the icon paths pointed at an existing square asset. Commit changes to main, then refresh or sync the marketplace.

## License

MIT
