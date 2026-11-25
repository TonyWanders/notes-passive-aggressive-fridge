#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge - make.fun entry.

Writes one funny passive-aggressive note a smart fridge leaves for its
owner: a single line, dry, petty and specific. Deterministic: the note is
a constant, so every run writes byte-identical output.

Gate (from the bounty rules): /output/entry.txt must be UTF-8 text of
1 to 200 characters, not only white space, a single line.
"""

import os
import sys

NOTE = (
    "Your leftovers have outlived your last three diets and two "
    "relationships. I keep them cold out of respect for the dead."
)

MAX_CHARS = 200
DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def resolve_output_path(argv, environ):
    """Pick the output target: argv[1], then $OUTPUT_PATH, then default."""
    if len(argv) > 1:
        return argv[1]
    return environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)


def validate_entry(text):
    """Enforce the bounty gate; raises SystemExit with a reason on failure."""
    if not text or not text.strip():
        raise SystemExit("entry is empty or only white space")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            "entry is %d characters, over the %d-character gate"
            % (len(text), MAX_CHARS)
        )
    if "\u2014" in text:
        raise SystemExit("entry must not contain an em dash")


def write_entry(text, out_path):
    """Validate the entry, then write it as UTF-8 bytes, no trailing newline."""
    validate_entry(text)
    data = text.encode("utf-8")
    parent = os.path.dirname(os.path.abspath(out_path))
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "wb") as fh:
        fh.write(data)


def main() -> int:
    out_path = resolve_output_path(sys.argv, os.environ)
    write_entry(NOTE, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
