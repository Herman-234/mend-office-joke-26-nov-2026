"""One-Line Office Joke Laugh-Off — entry generator.

Writes the chosen one-line office joke to output/entry.txt.
Deterministic: same input, same bytes, every run.
Candidates considered (SENJATA BARU — 3 drafted, 1 picked):
  1. "Our standup is 15 minutes, and somehow Dave still needs a Part 2."
     -> mild laugh, standup jokes are tired.
  2. "I asked IT for a second monitor. They sent me a mirror and a note: 'Look busy.'"
     -> PICKED: the mirror-for-monitor swap is a visual surprise and the
        note lands the punchline instantly; fresh, concrete, tight (79 chars).
  3. "The printer jammed again, so Karen from HR printed the incident report — on the jammed printer."
     -> funny loop, but longer and "Karen" is a cliché.
"""

from pathlib import Path

# The entry: one line, concrete scene (IT, second monitor, mirror, note).
JOKE = "I asked IT for a second monitor. They sent me a mirror and a note: 'Look busy.'"


def validate(text: str) -> None:
    """Enforce the house gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not text or text.strip() == "":
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"entry is {len(text)} chars, over the 200 limit")
    text.encode("utf-8")


def main() -> None:
    validate(JOKE)
    out_dir = Path(__file__).resolve().parent / "output"
    out_dir.mkdir(parents=True, exist_ok=True)
    entry_path = out_dir / "entry.txt"
    entry_path.write_text(JOKE, encoding="utf-8")
    print(f"wrote {entry_path} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
