#!/usr/bin/env python3
"""Validate Developer Wall profile files using only the standard library."""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

PROFILE_DIR = Path(__file__).resolve().parents[1] / "_data" / "profiles"
FIELDS = {
    "name": 60,
    "github": 39,
    "favorite_language": 40,
    "fun_fact": 180,
}
USERNAME = re.compile(r"^(?!-)(?!.*--)[A-Za-z0-9-]{1,39}(?<!-)$")


def error(path: Path, message: str) -> str:
    return f"::error file={path.as_posix()}::{message}"


def validate(directory: Path = PROFILE_DIR) -> list[str]:
    problems: list[str] = []
    seen: dict[str, Path] = {}
    if not directory.exists():
        return [error(directory, "Profile directory is missing")]

    for item in sorted(directory.rglob("*")):
        relative = item.relative_to(directory)
        if item.is_dir():
            problems.append(error(item, "Subdirectories are not allowed in _data/profiles"))
        elif item.name == ".gitkeep":
            continue
        elif item.suffix.lower() != ".json":
            problems.append(error(item, "Only lowercase .json profile files are allowed"))
        elif item.parent != directory:
            continue
        else:
            try:
                data = json.loads(item.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError) as exc:
                problems.append(error(item, f"Invalid JSON/UTF-8: {exc}"))
                continue
            if not isinstance(data, dict):
                problems.append(error(item, "Profile must be one JSON object"))
                continue
            keys = set(data)
            expected = set(FIELDS)
            if keys != expected:
                missing = sorted(expected - keys)
                extra = sorted(keys - expected)
                detail = []
                if missing:
                    detail.append("missing: " + ", ".join(missing))
                if extra:
                    detail.append("unexpected: " + ", ".join(extra))
                problems.append(error(item, "Use exactly the four profile fields (" + "; ".join(detail) + ")"))
                continue
            for field, limit in FIELDS.items():
                value = data[field]
                if not isinstance(value, str):
                    problems.append(error(item, f"{field} must be a string"))
                    continue
                if not value.strip():
                    problems.append(error(item, f"{field} cannot be empty"))
                if len(value) > limit:
                    problems.append(error(item, f"{field} is {len(value)} characters; maximum is {limit}"))
                if any(unicodedata.category(ch) in {"Cc", "Cs"} for ch in value):
                    problems.append(error(item, f"{field} contains a control character"))

            handle = data.get("github")
            if not isinstance(handle, str):
                continue
            if not USERNAME.fullmatch(handle):
                problems.append(error(item, "github must look like a valid GitHub username without @"))
            if item.stem != item.stem.lower():
                problems.append(error(item, "Filename must be lowercase"))
            if item.stem.lower() != handle.lower():
                problems.append(error(item, "Filename must match the github value"))
            key = handle.lower()
            if key in seen:
                problems.append(error(item, f"Duplicate GitHub username; also used in {seen[key].name}"))
            else:
                seen[key] = item
    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("\n".join(problems))
        print(f"Profile validation failed with {len(problems)} problem(s).")
        return 1
    count = len(list(PROFILE_DIR.glob("*.json")))
    print(f"Profile validation passed ({count} profile(s)).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
