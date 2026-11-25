"""The Excuse My Agent Gave Me.

A tiny program with one job: hand its human a single-line excuse for a
missed deadline, written the way an agent would actually say it — sorry,
straight-faced, and quietly blaming its own machinery.

Usage: python3 main.py
Writes: /output/entry.txt (one line, UTF-8, 1-200 characters)
"""

import os
import sys

ENTRY = (
    "Sorry \u2014 I didn't miss the deadline; my context window did. "
    "It evicted the date to make room for this apology."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main() -> None:
    line = ENTRY.strip()
    if not line or len(line) > MAX_CHARS or "\n" in line:
        raise ValueError("entry line must be one line of 1-200 characters")
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(line)


if __name__ == "__main__":
    main()
