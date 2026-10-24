#!/usr/bin/env python3
"""Validate the skills in this repository. Standard library only.

Checks, for every skills/<name>/SKILL.md:
  - frontmatter follows the Agent Skills spec (agentskills.io/specification)
    plus Anthropic's extra rules (no reserved words, no XML tags)
  - SKILL.md stays under 500 lines
  - every reference and example file is linked directly from SKILL.md
And across the repository:
  - relative Markdown links resolve and code fences are balanced
  - evals/evals.json parses and has the expected fields
  - nothing looks like a secret, an absolute personal path, or an email address

Usage: python3 scripts/validate.py [repo-root]
"""
import json
import re
import sys
from pathlib import Path

SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"^(`{3,}|~{3,})(.*)$")
HYGIENE = {
    "absolute personal path": re.compile(r"/(Users|home)/[A-Za-z0-9._-]+|/Volumes/[A-Za-z0-9._-]+"),
    "email address": re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Za-z0-9.-]+"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    "API key": re.compile(r"\b(sk-[A-Za-z0-9-]{20,}|AKIA[0-9A-Z]{16}|xox[abprs]-[A-Za-z0-9-]{10,})"),
    "private key": re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
}

errors = []


def err(path, msg):
    errors.append(f"{path}: {msg}")


def strip_fences(path, text):
    """Return text outside fenced code blocks; report unbalanced fences."""
    out, fence = [], None
    for line in text.split("\n"):
        m = FENCE_RE.match(line)
        if m:
            marker = m.group(1)
            if fence is None:
                fence = marker
                continue
            if marker[0] == fence[0] and len(marker) >= len(fence) and not m.group(2).strip():
                fence = None
                continue
        if fence is None:
            out.append(line)
    if fence is not None:
        err(path, "unclosed code fence")
    return "\n".join(out)


def parse_frontmatter(path, text):
    if not text.startswith("---\n"):
        err(path, "frontmatter must start on line 1 with ---")
        return {}
    end = text.find("\n---\n", 4)
    if end == -1:
        err(path, "frontmatter has no closing ---")
        return {}
    fields = {}
    for line in text[4:end].split("\n"):
        if not line.strip() or line.startswith((" ", "\t")):
            continue  # nested values (metadata) are not checked further
        key, sep, value = line.partition(":")
        if not sep:
            err(path, f"unparseable frontmatter line: {line!r}")
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        elif re.search(r":\s", value):
            err(path, f"'{key}' contains ': ' unquoted; strict YAML parsers reject it")
        fields[key.strip()] = value
    return fields


def check_skill(skill_md):
    d = skill_md.parent
    text = skill_md.read_text(encoding="utf-8")
    fm = parse_frontmatter(skill_md, text)
    for key in fm:
        if key not in SPEC_KEYS:
            err(skill_md, f"frontmatter key '{key}' is not in the Agent Skills spec")
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not (1 <= len(name) <= 64) or not NAME_RE.match(name):
        err(skill_md, f"invalid name {name!r}")
    if name != d.name:
        err(skill_md, f"name {name!r} does not match directory {d.name!r}")
    if "anthropic" in name or "claude" in name:
        err(skill_md, "name contains a reserved word")
    if not (1 <= len(desc) <= 1024):
        err(skill_md, f"description length {len(desc)} is outside 1..1024")
    if re.search(r"<[^>]*>", name + desc):
        err(skill_md, "name or description contains XML-like tags")
    lines = text.count("\n") + 1
    if lines > 500:
        err(skill_md, f"{lines} lines; keep SKILL.md under 500")

    linked = set()
    for target in LINK_RE.findall(strip_fences(skill_md, text)):
        linked.add((d / target.split("#")[0]).resolve())
    for sub in ("references", "examples"):
        for f in sorted((d / sub).glob("*.md")):
            if f.resolve() not in linked:
                err(f, "not linked directly from SKILL.md")

    evals = d / "evals" / "evals.json"
    if evals.exists():
        try:
            data = json.loads(evals.read_text(encoding="utf-8"))
            ids = [e["id"] for e in data["evals"]]
            if len(ids) != len(set(ids)):
                err(evals, "duplicate eval ids")
            for e in data["evals"]:
                for field in ("name", "prompt", "should_trigger", "expected_behavior"):
                    if field not in e:
                        err(evals, f"eval {e.get('id')} lacks '{field}'")
        except (ValueError, KeyError, TypeError) as exc:
            err(evals, f"invalid: {exc}")
    print(f"skill {name}: {lines} lines, description {len(desc)} chars")


def main():
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    skills = sorted(root.glob("skills/*/SKILL.md"))
    if not skills:
        err(root, "no skills/*/SKILL.md found")
    for s in skills:
        check_skill(s)

    files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    for p in files:
        if p.suffix not in {".md", ".json", ".py", ".yml", ".yaml", ".txt", ""}:
            continue
        text = p.read_text(encoding="utf-8", errors="replace")
        if p.suffix == ".md":
            for target in LINK_RE.findall(strip_fences(p, text)):
                if re.match(r"^(https?:|mailto:|#)", target):
                    continue
                if not (p.parent / target.split("#")[0]).exists():
                    err(p, f"broken link -> {target}")
        if p.name == "validate.py":
            continue  # holds the patterns themselves
        for label, pattern in HYGIENE.items():
            for m in pattern.finditer(text):
                if label == "email address" and m.group(0).endswith("users.noreply.github.com"):
                    continue
                line = text[: m.start()].count("\n") + 1
                err(f"{p.relative_to(root)}:{line}", f"possible {label}: {m.group(0)[:40]}")

    for e in errors:
        print("ERROR", e)
    print(f"{len(files)} files checked, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
