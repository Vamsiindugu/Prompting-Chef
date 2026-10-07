# GitHub → ChatGPT synchronization

## What is automatic

For a workspace-managed GitHub marketplace, OpenAI supports daily marketplace synchronization. A workspace administrator imports the marketplace repository and can also trigger **Sync now**.

For personal ChatGPT accounts, GitHub repository access lets ChatGPT read repository content, but it is not itself a plugin deployment channel. A personal plugin does not automatically republish itself from arbitrary GitHub commits.

## Recommended setup for this repository

### Personal development / ChatGPT Desktop

Use the repository itself as a Git-backed marketplace source:

```bash
codex plugin marketplace add Vamsiindugu/Prompting-Chef --ref main
codex plugin marketplace upgrade prompting-chef-marketplace
```

Install Prompting Chef from the Plugins Directory in ChatGPT Desktop.

After changing the repository:

```bash
git pull
codex plugin marketplace upgrade prompting-chef-marketplace
```

Then restart/refresh the ChatGPT Desktop plugin directory as needed.

### Workspace automatic sync

If this plugin is managed inside a ChatGPT Business/Enterprise/Edu workspace:

1. Admin Console → Plugins → Add → Import marketplace.
2. Source: `https://github.com/Vamsiindugu/Prompting-Chef`
3. Path: leave empty because `.agents/plugins/marketplace.json` is at the repository root.
4. Branch: `main`.
5. Authorize GitHub.
6. Review the imported Prompting Chef plugin and set the desired installation policy.

OpenAI documents daily sync for newly imported GitHub marketplaces. The admin can also use **Sync now**.

## Keeping versions clean

Every functional release should bump the version in both manifests:

- `plugin.json`
- `.codex-plugin/plugin.json`

Use semantic versions such as `0.14.4`, `0.15.0`, etc.

## Do not treat GitHub app access as deployment

The standard GitHub connection in ChatGPT provides on-demand repository retrieval. It does not create a plugin deployment/sync relationship by itself.
