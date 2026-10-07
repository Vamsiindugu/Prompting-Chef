# Prompting Chef GitHub sync

GitHub main is canonical.

Personal/local development:

codex plugin marketplace add Vamsiindugu/Prompting-Chef --ref main
codex plugin marketplace upgrade prompting-chef-marketplace

Workspace distribution:
Import the repository from Workspace settings > Plugins > Add > Import marketplace. Leave Path empty because the marketplace file is at the repository root, and select main as the branch. OpenAI supports daily sync for imported GitHub marketplaces and a manual Sync now action.

A normal GitHub connection is repository access. The marketplace is the plugin distribution mechanism.
