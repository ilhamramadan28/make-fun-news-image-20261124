#!/usr/bin/env python3
"""Write the 24 November 2026 news image to /output/entry.png.

The image is bundled in this repository as entry.png (a 1024x1024 JPEG).
This program copies it to the output directory byte for byte, sets mode
0644 so the grader can read it, and verifies the copy with SHA-256.
Standard library only, no network, deterministic: two runs produce the
same bytes.
"""

import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    dest = os.path.join(output_dir, "entry.png")
    shutil.copyfile(SOURCE, dest)
    os.chmod(dest, 0o644)
    if sha256(SOURCE) != sha256(dest):
        print("error: copy is not byte-identical", file=sys.stderr)
        return 1
    print("wrote %s (%d bytes, sha256 %s)"
          % (dest, os.path.getsize(dest), sha256(dest)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
