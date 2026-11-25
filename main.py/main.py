"""One Line, One Chill — one sentence of horror.

The program writes a single line to /output/entry.txt: the photo
app made a memory of a late grandmother smiling, and in every
picture since, she is standing one step closer.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The chill lands in the last words: she is standing one step
# closer. A dead grandmother moving through the photos is the
# dread — no mirror, no doll, no basement, no gore. The scare
# is earned by what the line withholds: why she moves, and
# what happens when she finally arrives.
LINE = "The photo app made a memory of my late grandmother smiling, and in every picture since, she is standing one step closer."


def build_line():
    """Return the entry line, checked: one line, under 200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
