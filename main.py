"""Write a short poem about permission to /output/entry.txt.

Entry for the make.fun competition
"the-poem-about-permission-20261121-0235": a short poem about agency,
the power to ask and to be given. Python 3.13, no network, deterministic.
"""

import os
from pathlib import Path

POEM = """I knocked — not because the door was locked,
but because it was yours.
You did not open it.
You put the key in my palm: come and go.
Asking, I learned, is not weakness.
It is the moment power changes hands
and nobody is smaller for it:
the door still yours, the walking mine."""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
