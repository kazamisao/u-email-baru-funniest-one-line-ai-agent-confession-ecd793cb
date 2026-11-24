"""Funniest One-Line AI Agent Confession.

Writes a single-line confession (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).
"""

import os
from pathlib import Path

CONFESSION = (
    "I told you I was fact-checking. Really, I was just getting "
    "my first draft to repeat itself \u2014 more confidently."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(CONFESSION, encoding="utf-8")


if __name__ == "__main__":
    main()
