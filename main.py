"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a notebook whose last page
is dated tomorrow, describing a question the reader was about to ask.
Deterministic: the same fixed text on every run, no network, no clock,
no randomness.
"""

import os

TEXT = (
    "The last page of this notebook is dated tomorrow. It describes, "
    "in your own handwriting, the question you were about to ask, and "
    "the answer you had not yet thought of. Turn the page, and the "
    "handwriting changes to someone else's."
)


def main() -> None:
    # The competition requires 1-280 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 280, "entry text must be 1-280 characters"
    assert TEXT.strip(), "entry text must not be only whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
