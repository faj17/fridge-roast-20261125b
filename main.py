#!/usr/bin/env python3
"""Fridge Roast entry.

Writes one line roasting a smart fridge to /output/entry.txt
(1-200 characters, UTF-8, not only whitespace). Standard library
only, no network, no input.

The roast is built from three fragments: the setup (a firmware
update bricks the ice maker), the turn (the fridge then pushes a
notification), and the punch (the notification declares the upgrade
a success). ``assemble`` joins them into the single line; ``validate``
checks the entry gate before anything is written.
"""

from pathlib import Path

SETUP = "My fridge's firmware update bricked the ice maker,"
TURN = "then it pushed a notification:"
PUNCH = "'Upgrade successful.'"

OUTPUT_PATH = Path("/output/entry.txt")


def assemble() -> str:
    """Join the three module fragments into one roast line."""
    return f"{SETUP} {TURN} {PUNCH}"


def validate(roast: str) -> str:
    """Check the roast meets the entry gate before it is written.

    Must be 1-200 characters, a single line, UTF-8-encodable, and
    more than whitespace. Raises ValueError otherwise.
    """
    if not 1 <= len(roast) <= 200:
        raise ValueError(f"roast must be 1-200 characters, got {len(roast)}")
    if "\n" in roast or "\r" in roast:
        raise ValueError("roast must be a single line")
    if any(ord(ch) < 32 and ch not in ("\t",) for ch in roast):
        raise ValueError("roast must not contain control characters")
    if not roast.strip():
        raise ValueError("roast must not be only whitespace")
    roast.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return roast


def main() -> None:
    roast = validate(assemble())
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(roast, encoding="utf-8")


if __name__ == "__main__":
    main()
