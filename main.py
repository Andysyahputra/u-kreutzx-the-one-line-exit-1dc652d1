#!/usr/bin/env python3
"""The One-Line Exit.

Writes the funniest single-line resignation letter to /output/entry.txt.

The letter is assembled from its two halves — the formal resignation and
the surprise turn — so the joke's structure stays visible in the code,
then validated against the competition gate (1-140 chars, one line, UTF-8)
before anything is written to disk.
"""

from pathlib import Path

# The formal opening, as a real resignation letter would start it.
OPENING = "I hereby resign, effective immediately"

# The turn: the punchline the reader did not expect.
TURN = "the office plant has been promoted above me, and frankly, it earned it."

ENTRY = f"{OPENING} \u2014 {TURN}"

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 140


def validate(text: str) -> str:
    """Enforce the gate: one non-empty line of 1-140 characters."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # raises if not encodable as UTF-8
    return text


def main() -> None:
    line = validate(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
