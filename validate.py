#!/usr/bin/env python3
"""Enforce this repository's own rules.

The README claims every number resolves to a source and that no em dashes appear.
This script is what makes those claims checkable rather than aspirational.

Usage:  python3 validate.py          exit 0 if clean, 1 if not
"""
import re
import sys
import pathlib

ROOT = pathlib.Path(__file__).parent
REGISTRY = ROOT / "references.md"
CITE = re.compile(r"\[([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)\]")
LINK = re.compile(r"\]\((?!https?://|#)([^)]+)\)")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
REQUIRED = {
    "skill": ["name", "description", "version", "last_validated", "freshness", "references_used"],
    "research": ["title", "file", "last_validated", "freshness", "references_used"],
}
FRESHNESS = {"stable", "drift-watch", "volatile"}
# Documented key-format examples, not real citations.
PLACEHOLDERS = {"Author-Year", "Org-Topic-Year", "Key-Year"}

errors, warnings = [], []


def md_files():
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


# ---------------------------------------------------------------- registry
registry_keys = set()
for line in REGISTRY.read_text(encoding="utf-8").splitlines():
    if line.startswith("| `["):
        m = CITE.search(line)
        if m:
            registry_keys.add(m.group(1))
if not registry_keys:
    errors.append("references.md: no citation keys parsed from the registry table")

# ---------------------------------------------------------------- per file
for path in md_files():
    rel = path.relative_to(ROOT)
    text = path.read_text(encoding="utf-8")

    # Em dashes: a hard rule, not a preference.
    if "—" in text:
        errors.append(f"{rel}: {text.count('—')} em dash(es)")

    # Every cited key must resolve. references.md itself defines them.
    if path != REGISTRY:
        for key in set(CITE.findall(text)) - PLACEHOLDERS:
            if key not in registry_keys:
                errors.append(f"{rel}: cites [{key}], which is not in references.md")

    # Relative links must point at something that exists.
    for target in LINK.findall(text):
        if not (path.parent / target.split("#")[0]).resolve().exists():
            errors.append(f"{rel}: broken link -> {target}")

    # Frontmatter contract for skills and research files.
    kind = "skill" if path.name == "SKILL.md" else "research" if rel.parts[0] == "research" else None
    if kind:
        fm = FRONTMATTER.search(text)
        if not fm:
            errors.append(f"{rel}: missing frontmatter")
            continue
        block = fm.group(1)
        for field in REQUIRED[kind]:
            if not re.search(rf"^{field}:", block, re.MULTILINE):
                errors.append(f"{rel}: frontmatter missing '{field}'")
        fresh = re.search(r"^freshness:\s*(\S+)", block, re.MULTILINE)
        if fresh and fresh.group(1) not in FRESHNESS:
            errors.append(f"{rel}: freshness '{fresh.group(1)}' not in {sorted(FRESHNESS)}")

        # Declared references_used should actually be cited in the body, and vice versa.
        declared = set(re.findall(r"[\[\s]([A-Z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)+)[,\]\s]",
                                  re.search(r"^references_used:.*$", block, re.MULTILINE).group(0))) \
            if re.search(r"^references_used:.*$", block, re.MULTILINE) else set()
        body = text[fm.end():]
        cited = set(CITE.findall(body)) - PLACEHOLDERS
        for key in declared - cited:
            warnings.append(f"{rel}: declares [{key}] in references_used but never cites it")
        for key in cited - declared:
            warnings.append(f"{rel}: cites [{key}] but omits it from references_used")

    # Skills must carry the documented body sections.
    if path.name == "SKILL.md":
        for heading in ("## TL;DR", "## Before starting", "## Anti-patterns",
                        "## Output format", "## References", "## Related skills"):
            if heading not in text:
                errors.append(f"{rel}: missing required section '{heading}'")

# ---------------------------------------------------------------- report
for w in warnings:
    print(f"warn  {w}")
for e in errors:
    print(f"FAIL  {e}")

print(f"\n{len(md_files())} files checked · {len(registry_keys)} citation keys · "
      f"{len(errors)} error(s) · {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
