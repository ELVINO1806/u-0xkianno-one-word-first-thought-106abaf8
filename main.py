#!/usr/bin/env python3
"""One Word, First Thought — make.fun entry.

Writes exactly one word to /output/entry.txt:
    petrichor — the smell of first rain on dry earth.
"""

import os

WORD = "petrichor"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
