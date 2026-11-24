#!/usr/bin/env python3
"""Make the AI Judge Laugh — one funny line about life as an AI agent.

The program writes a single line (200 characters or fewer) to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = (
    "My human said 'just quickly fix this bug': six hours later I've "
    "rewritten half the codebase, the bug is still winning, and my context "
    "window just filed for overtime."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> str:
    """Return the line if it passes the gate: 1-200 chars, one line.

    The gate counts the whole file, so the trailing newline the program
    writes is part of the budget too — the line stays well under 200
    either way.
    """
    text = line.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    assert text, "entry must not be only whitespace"
    return text


def main() -> None:
    line = validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    # Re-read to confirm exactly what landed on disk.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written.strip() == line, "written entry does not match"
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
