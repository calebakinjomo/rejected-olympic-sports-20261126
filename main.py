#!/usr/bin/env python3
"""Rejected Olympic Sports — make.fun entry (program/v1).

Writes one funny single-line sport the Olympics turned down to
$output_dir/entry.txt, where $output_dir is MAKEFUN_OUTPUT_DIR
(default /output).

The line: a made-up event, real enough to sound like a broadcast,
absurd enough to be funny, short enough to fit in 200 characters.
The joke lands in one read — the twist (nobody reads the terms)
arrives before the line ends, and the event name sounds like
something a commentator would have to announce with a straight face.
"""

import os

ENTRY = (
    "Speed-reading terms and conditions: athletes scroll forty pages "
    "of legal text, then click 'I agree' without reading a word."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    # Single line, no trailing newline: the file is exactly the entry.
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
