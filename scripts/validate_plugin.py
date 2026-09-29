#!/usr/bin/env python3
"""Dependency-free structural validator for the Agent Plugins 1.0 package.

This validates package layout and selected manifest field types, not full host
schema compatibility or model response quality. See tests/behavioral-cases.md.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?")
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
    except (json.JSONDecodeError, OSError) as exc:
        fail(f"plugin.json cannot be read as valid JSON: {exc}")
    if not isinstance(manifest, dict):
        fail("plugin.json root must be an object")
    if manifest.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        fail("plugin.json must declare the Agent Plugins 1.0.0 schema")
    name = manifest.get("name")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
        fail("plugin name must be lowercase kebab-case and at most 64 characters")
    version = manifest.get("version")
    if not isinstance(version, str) or not re.fullmatch(VERSION_RE, version):
        fail("plugin version must be semantic versioning")
    for field in ("description", "license"):
        if not isinstance(manifest.get(field), str) or not manifest[field].strip():
            fail(f"plugin.json {field} must be a non-empty string")
    author = manifest.get("author")
    if not isinstance(author, dict) or not isinstance(author.get("name"), str) or not author["name"].strip():
        fail("plugin.json author.name must be a non-empty string")
    repository = manifest.get("repository")
    if repository is not None and (not isinstance(repository, str) or not repository.startswith("https://")):
        fail("repository must be an HTTPS URL")

    extensions = manifest.get("extensions")
    openai = extensions.get("com.openai") if isinstance(extensions, dict) else None
    interface = openai.get("interface") if isinstance(openai, dict) else None
    if not isinstance(interface, dict):
        fail("extensions.com.openai.interface must be an object")
    for field in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        value = interface.get(field)
        if not isinstance(value, str) or not value.strip():
            fail(f"extensions.com.openai.interface.{field} must be a non-empty string")
    capabilities = interface.get("capabilities")
    if not isinstance(capabilities, list) or not capabilities or any(not isinstance(x, str) or not x.strip() for x in capabilities):
        fail("interface.capabilities must be a non-empty array of non-empty strings")
    prompts = interface.get("defaultPrompt")
    if isinstance(prompts, str):
        prompts = [prompts]
    if not isinstance(prompts, list) or not 1 <= len(prompts) <= 3 or any(not isinstance(x, str) or not x.strip() for x in prompts):
        fail("interface.defaultPrompt must be a non-empty string or an array of one to three non-empty strings")

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
    if not (root / "tests" / "behavioral-cases.md").is_file():
        fail("tests/behavioral-cases.md is missing; keep manual behavior evaluation separate from this structural check")

    print(f"OK: {name} {version} package structure and selected manifest field types are valid")
    print("NOTE: this does not validate complete host compatibility or answer quality; see tests/behavioral-cases.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
