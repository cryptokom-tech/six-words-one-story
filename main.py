"""Six Words, One Story — make.fun bounty entry.

Writes a single original six-word story to /output/entry.txt.
The story is fixed text, written by this program at run time.
"""

import os
import sys

STORY = "Grandma's last voicemail still says hello."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = STORY.strip()
    words = text.split()
    if not text or len(text) > 60 or len(words) != 6:
        print("entry must be exactly six words, 1-60 characters",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    # Six words, one whole story: a grandchild keeps the voicemail
    # because it is the last place her voice still says hello.
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
