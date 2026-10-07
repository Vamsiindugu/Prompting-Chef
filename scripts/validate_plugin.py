import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
plugin = json.loads((ROOT / 'plugin.json').read_text())
overlay = json.loads((ROOT / '.codex-plugin' / 'plugin.json').read_text())
market = json.loads((ROOT / '.agents' / 'plugins' / 'marketplace.json').read_text())
ui = plugin['extensions']['com.openai']['interface']
assert plugin['name'] == 'prompting-chef'
assert plugin['version'] == '0.15.0'
assert overlay['name'] == plugin['name']
assert overlay['version'] == plugin['version']
assert len(ui['defaultPrompt']) == 2
assert all(len(p) <= 128 for p in ui['defaultPrompt'])
for field in ('composerIcon', 'logo'):
    asset = ROOT / ui[field].replace('./', '', 1)
    assert asset.is_file(), f'Missing asset: {asset}'
assert (ROOT / 'skills/instructions/SKILL.md').is_file()
assert (ROOT / 'skills/instructions/lookup/knowledge-index.json').is_file()
entry = market['plugins'][0]
assert entry['name'] == plugin['name']
assert entry['source']['source'] == 'url'
print('Prompting Chef validation passed.')