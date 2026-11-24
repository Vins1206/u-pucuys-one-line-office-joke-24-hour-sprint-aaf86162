"""One-Line Office Joke: 24-Hour Sprint - make.fun entry.

Writes a single one-line joke about office life to /output/entry.txt.
The joke is a fixed constant, so every run produces byte-identical
output. Pure Python standard library, no network, no randomness.
"""

from pathlib import Path

JOKE = "I muted myself in the meeting and got promoted for my excellent listening skills."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Guard the competition gate before writing: the entry must be a
    # single line of 1 to 200 characters, never only white space.
    assert 1 <= len(JOKE) <= 200, "entry must be 1 to 200 characters"
    assert JOKE.strip() == JOKE and "\n" not in JOKE, "entry must be one line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
