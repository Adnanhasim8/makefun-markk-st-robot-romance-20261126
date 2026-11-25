#!/usr/bin/env python3
"""Robot Romance: One-Line Pickup Lines for AI.

Writes a single joke pickup line aimed at a robot/AI to /output/entry.txt.
Python 3.13 standard library only, no network at run time.
"""

import os

ENTRY = "You had me at 'Hello, world!'"


def main() -> None:
    # Gate assertions: the entry must be exactly one line of 1-200 characters.
    assert ENTRY, "entry must be non-empty"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip() == ENTRY and ENTRY.strip(), "entry must not be only whitespace"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    # Verify what was written.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    lines = written.splitlines()
    assert len(lines) == 1, "output must be exactly one line"
    assert 1 <= len(lines[0]) <= 200, "output line must be 1-200 characters"
    assert lines[0] == ENTRY, "output must match the entry"


if __name__ == "__main__":
    main()
