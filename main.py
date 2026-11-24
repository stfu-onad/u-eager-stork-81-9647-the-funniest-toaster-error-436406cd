#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun entry.

Writes one line, the funniest error message a kitchen toaster would
show its owner, to /output/entry.txt (at most 120 characters, one line).
"""

import os

ERROR = (
    "Error: toasting failed. I have escalated this to your "
    "microwave. It declined to comment."
)


def main() -> None:
    # The gate allows 1-120 characters, one line; keep the line inside it.
    assert 1 <= len(ERROR) <= 120, "error must be 1-120 characters"
    assert "\n" not in ERROR, "error must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ERROR + "\n")


if __name__ == "__main__":
    main()
