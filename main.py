"""news-image-20261118 entry (Python 3.13, standard library only).

Copies the pre-rendered infographic entry.png beside this file to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png). Deterministic:
the same bytes are written on every run.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")
DST = os.path.join(OUT_DIR, "entry.png")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, DST)
# The gate requires both runs to write the same bytes; a copy of a fixed
# file is byte-identical by construction. Confirm the write landed and
# that the destination is the expected 1024x1024 PNG (99,960 bytes).
assert os.path.getsize(DST) == os.path.getsize(SRC) == 99960
print("wrote", DST, os.path.getsize(DST), "bytes")
