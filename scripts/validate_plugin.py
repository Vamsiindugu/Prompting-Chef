import json
import struct
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
plugin = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
overlay = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text(encoding="utf-8"))
market = json.loads((ROOT / ".agents" / "plugins" / "marketplace.json").read_text(encoding="utf-8"))
ui = plugin["extensions"]["com.openai"]["interface"]

assert plugin["name"] == "prompting-chef"
assert plugin["version"] == "0.15.0"
assert overlay["name"] == plugin["name"]
assert overlay["version"] == plugin["version"]
assert overlay["repository"] == plugin["repository"]
assert overlay["interface"]["defaultPrompt"] == ui["defaultPrompt"]
assert len(ui["defaultPrompt"]) == 2, "Keep exactly two starter prompts"
assert all(isinstance(p, str) and p.strip() and len(p) <= 128 for p in ui["defaultPrompt"])
assert ui["logo"] == ui["composerIcon"], "Logo and composer icon must use the same asset"

for field in ("composerIcon", "logo"):
    asset_path = ui[field].removeprefix("./")
    asset = ROOT / asset_path
    assert asset.is_file(), f"Missing {field} asset: {asset_path}"
    with asset.open("rb") as stream:
        header = stream.read(24)
    assert header[:8] == b"\x89PNG\r\n\x1a\n", f"{asset_path} must be a PNG"
    width, height = struct.unpack(">II", header[16:24])
    assert width > 0 and height > 0, f"Invalid PNG dimensions: {asset_path}"
    assert width == height, f"{asset_path} must be square (got {width}x{height})"

skill_path = ROOT / "skills" / "instructions" / "SKILL.md"
index_path = ROOT / "skills" / "instructions" / "lookup" / "knowledge-index.json"
assert skill_path.is_file(), "Missing skill instructions"
assert index_path.is_file(), "Missing knowledge index"
index = json.loads(index_path.read_text(encoding="utf-8"))
assert index.get("sources"), "Knowledge index must contain sources"
skill_root = skill_path.parent
for source in index["sources"]:
    relative = Path(source["path"])
    assert not relative.is_absolute(), f"Source path must be relative: {relative}"
    resolved = (skill_root / relative).resolve()
    assert resolved.is_relative_to(skill_root.resolve()), f"Source escapes skill directory: {relative}"
    assert resolved.is_file(), f"Knowledge index points to a missing file: {relative}"

agent_yaml = ROOT / "skills" / "instructions" / "agents" / "openai.yaml"
assert agent_yaml.is_file(), "Missing OpenAI agent metadata"
assert "display_name: Prompting Chef" in agent_yaml.read_text(encoding="utf-8")

entry = market["plugins"][0]
assert entry["name"] == plugin["name"]
assert entry["source"]["source"] == "url"
assert entry["source"]["url"].rstrip("/").endswith("Vamsiindugu/Prompting-Chef.git")
assert entry["source"]["ref"] == "main"

print("Prompting Chef validation passed.")
