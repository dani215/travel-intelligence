#!/usr/bin/env python3
"""Dependency-free structural validator for the Agent Plugins 1.0 package."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDERS = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[TODO")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    manifest_path = root / "plugin.json"
    if not manifest_path.is_file():
        fail("root plugin.json is missing")
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"plugin.json is invalid JSON: {exc}")

    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        fail("plugin.json must declare the Agent Plugins 1.0.0 schema")
    name = manifest.get("name", "")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        fail("plugin name must be lowercase kebab-case and at most 64 characters")
    version = manifest.get("version", "")
    if not re.fullmatch(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?", version):
        fail("plugin version must be semantic versioning")
    for field in ("description", "author", "license"):
        if not manifest.get(field):
            fail(f"plugin.json is missing {field}")
    if manifest.get("repository") and not manifest["repository"].startswith("https://"):
        fail("repository must be an HTTPS URL")

    interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "defaultPrompt"):
        if not interface.get(field):
            fail(f"extensions.com.openai.interface is missing {field}")
    if isinstance(interface.get("defaultPrompt"), list) and len(interface["defaultPrompt"]) > 3:
        fail("interface.defaultPrompt may contain no more than three prompts")

    skill_dir = root / "skills" / name
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.is_file():
        fail(f"expected skill at skills/{name}/SKILL.md")
    text = skill_path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")
    frontmatter = match.group(1)
    if not re.search(r"^name:\s*" + re.escape(name) + r"\s*$", frontmatter, re.MULTILINE):
        fail("skill frontmatter name must match the skill directory")
    description = re.search(r"^description:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not description or len(description.group(1)) > 1024:
        fail("skill frontmatter needs a description under 1024 characters")
    if PLACEHOLDERS.search(text):
        fail("SKILL.md contains scaffold placeholders")
    for reference in re.findall(r"\]\((references/[^)]+)\)", text):
        target = (skill_dir / reference).resolve()
        if skill_dir.resolve() not in target.parents or not target.is_file():
            fail(f"invalid or missing skill reference: {reference}")
    refs = skill_dir / "references"
    if not refs.is_dir():
        fail("skill references directory is missing")
    for path in refs.glob("*.md"):
        if PLACEHOLDERS.search(path.read_text(encoding="utf-8")):
            fail(f"reference contains scaffold placeholders: {path.name}")

    print(f"OK: {name} {version} plugin structure is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
