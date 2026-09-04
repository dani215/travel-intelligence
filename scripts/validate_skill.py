#!/usr/bin/env python3
"""Small dependency-free validator for the published skill package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


PLACEHOLDERS = re.compile(r"\b(?:TODO|TBD|FIXME)\b|\[TODO")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def frontmatter(text: str) -> tuple[str, str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail("SKILL.md must begin with YAML frontmatter")
    body = match.group(1)
    name_match = re.search(
        r"^name:\s*[\"']?([^\"'\n]+?)[\"']?\s*$", body, re.MULTILINE
    )
    desc_match = re.search(
        r"^description:\s*[\"'](.*?)[\"']\s*$", body, re.MULTILINE
    )
    if not name_match or not desc_match:
        fail("frontmatter must contain quoted name and description fields")
    return name_match.group(1), desc_match.group(1), body


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skill = root / "SKILL.md"
    if not skill.is_file():
        fail("SKILL.md is missing")

    text = skill.read_text(encoding="utf-8")
    name, description, yaml = frontmatter(text)
    if name != "travel-intelligence":
        fail(f"unexpected skill name: {name}")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        fail("skill name must be lowercase hyphen-case and at most 64 characters")
    if not description.startswith("Use when"):
        fail("description must start with 'Use when'")
    if len(yaml) > 1024:
        fail("frontmatter is longer than 1024 characters")
    if PLACEHOLDERS.search(text):
        fail("SKILL.md contains scaffold placeholders")

    metadata = root / "agents" / "openai.yaml"
    if not metadata.is_file():
        fail("agents/openai.yaml is missing")
    metadata_text = metadata.read_text(encoding="utf-8")
    for required in (
        "display_name:",
        "short_description:",
        "default_prompt:",
        "allow_implicit_invocation: true",
    ):
        if required not in metadata_text:
            fail(f"openai.yaml is missing {required}")

    for reference in re.findall(r"\]\((references/[^)]+)\)", text):
        if not (root / reference).is_file():
            fail(f"referenced file is missing: {reference}")

    for path in sorted((root / "references").glob("*.md")):
        if PLACEHOLDERS.search(path.read_text(encoding="utf-8")):
            fail(f"reference contains scaffold placeholders: {path.name}")

    print(f"OK: {name} package is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
