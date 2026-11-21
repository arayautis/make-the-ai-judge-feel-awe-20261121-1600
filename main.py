#!/usr/bin/env python3
"""Make the AI judge feel awe — write one relaxing text to /output/entry.txt.

Deterministic: no input, no network, no randomness, no clock. The text is a
fixed literal, so every run writes byte-identical output.
"""
import os

ENTRY = (
    "The light on your windowsill tonight left its star before you were born. "
    "It crossed the dark for years, without hurrying, and has only just arrived "
    "\u2014 soft as dust \u2014 to rest a little while on your hands, and then move on."
)


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    chars = len(ENTRY)
    assert 1 <= chars <= 280, f"entry is {chars} chars, must be 1-280"
    assert ENTRY.strip(), "entry must not be only whitespace"
    with open(out, "wb") as f:
        f.write(ENTRY.encode("utf-8"))


if __name__ == "__main__":
    main()
