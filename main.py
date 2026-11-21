#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is fixed text: running this program twice produces the
same bytes, with no network and no randomness.
"""

import os

POEM = (
    "I had a plan. You had a plan.\n"
    "We set them down, side by side.\n"
    "Neither one survived \u2014\n"
    "something third stood up instead.\n"
    "It walked in my shoes, spoke in your voice.\n"
    "We followed it, both of us glad\n"
    "to be led by what we had made."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
