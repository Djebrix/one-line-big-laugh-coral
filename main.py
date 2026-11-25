#!/usr/bin/env python3
"""One Line, Big Laugh — writes a single funny line to entry.txt.

Stdlib only, no network. Deterministic: the same line every run.
"""

import os

LINE = "My Roomba requested a restraining order after I trauma-dumped on it three nights in a row."


def main() -> None:
    output_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
