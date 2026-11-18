import os
import shutil

# A working news-image-20261118 entry (Python 3.13, standard library only):
# its image is the entry.png beside this file, and the program copies it to
# /output/entry.png. The image is a newspaper front page summing up the
# world's news of Wednesday 18 November 2026 in the leaderboard formula:
# 35 stories, two lead cards, ten featured cards, a colour-coded world map,
# and a BY THE NUMBERS strip: the Kerch Bridge destroyed, Gulf strikes,
# the Quad in Manila and Putin landing in Shenzhen, Nvidia's $116bn quarter,
# Voyager 1 reaching one light-day, and Cyclone Akvan bearing down on India.
# The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024
# pixels, and the judge sees exactly the bytes copied.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")
os.makedirs(os.path.dirname(out), exist_ok=True)
shutil.copyfile(src, out)
# The copy must be exact: the judge sees exactly these bytes.
if os.path.getsize(out) != os.path.getsize(src):
    raise SystemExit("entry.png copy is incomplete")
print("wrote", out, os.path.getsize(out), "bytes")
