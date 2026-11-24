#!/usr/bin/env python3
"""One Line of Earned Pride — entry program.

Writes a single line (1-240 chars) to /output/entry.txt: a quiet, earned
moment of pride for a small person doing something hard. Deterministic:
the same line on every run. The line is validated against the gate
(UTF-8, 1-240 chars, single line, not only whitespace) before writing,
so a bad line fails loudly here instead of silently failing the gate.
"""

import os
import sys

LINE = "On the third night of the blackout, the boy who'd memorised the fuse box by torchlight brought the whole street back on."


def validate(line):
    if not isinstance(line, str):
        raise ValueError("entry must be text")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if not 1 <= len(line) <= 240:
        raise ValueError("entry must be 1-240 characters, got %d" % len(line))
    line.encode("utf-8")  # raises if not valid UTF-8 text
    return line


def main():
    entry = validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print("entry invalid: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
