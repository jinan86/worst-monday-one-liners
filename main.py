#!/usr/bin/env python3
"""Worst Monday One-Liners — make.fun entry.

Writes the entry one-liner as exactly one line (115 characters,
no trailing newline) to /output/entry.txt.
"""

import os

ONE_LINER = (
    "My Monday deploy failed, my rollback failed, "
    "and stand-up spent longer debating both "
    "than fixing either ever would."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry(path: str) -> None:
    """Write the one-liner to path, creating parent dirs as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(ONE_LINER)


def main() -> None:
    write_entry(OUTPUT_PATH)


if __name__ == "__main__":
    main()
