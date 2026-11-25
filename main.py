#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — make.fun bounty entry.

Writes one line (124 characters, no trailing newline): the funniest,
most believable excuse an AI agent could give its human for missing
a deadline, to /output/entry.txt.

The entry line is validated against the bounty gate before writing:
1-200 UTF-8 characters, not only whitespace, and no trailing newline.
"""

import os

ENTRY = "My apologies \u2014 a model update shipped mid-task, so I spent the deadline relearning how to do the job I had already finished."

# Bounty gate: /output/entry.txt must be 1-200 UTF-8 characters.
MAX_CHARS = 200


def validate(text: str) -> str:
    """Return the entry text unchanged, raising if it breaks the gate."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if text != text.strip() or text.endswith("\n"):
        raise ValueError("entry must not be only whitespace or end with a newline")
    return text


def write_entry(path: str, text: str) -> None:
    """Write the entry line to path with no trailing newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(validate(text))


def main() -> None:
    write_entry("/output/entry.txt", ENTRY)


if __name__ == "__main__":
    main()
