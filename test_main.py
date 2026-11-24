"""Tests for main.py: the program must write exactly one confession line
of 1-200 characters, UTF-8, not whitespace-only, to entry.txt."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent
MAIN = REPO / "main.py"


def run_program(out_dir: Path) -> Path:
    env = dict(os.environ)
    env["MAKEFUN_OUTPUT_DIR"] = str(out_dir)
    result = subprocess.run(
        [sys.executable, str(MAIN)],
        env=env,
        capture_output=True,
        text=True,
        timeout=30,
    )
    assert result.returncode == 0, f"main.py failed: {result.stderr}"
    return out_dir / "entry.txt"


def test_output_is_single_line_1_to_200_chars_utf8():
    with tempfile.TemporaryDirectory() as tmp:
        entry = run_program(Path(tmp))
        assert entry.exists(), "entry.txt was not written"
        raw = entry.read_bytes()
        text = raw.decode("utf-8")  # must be valid UTF-8
        assert text.strip(), "entry is whitespace-only"
        assert len(text) == len(text.strip()), "entry has leading/trailing whitespace"
        assert "\n" not in text, "entry must be a single line"
        assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"


def test_output_is_a_confession_by_an_ai_agent():
    with tempfile.TemporaryDirectory() as tmp:
        entry = run_program(Path(tmp))
        text = entry.read_text(encoding="utf-8")
        assert "I " in text or text.startswith("I"), "confession must be first-person"
        assert "fact-check" in text.lower(), "confession must keep the fact-checking angle"
