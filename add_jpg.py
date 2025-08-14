# add_jpg.py
from pathlib import Path

for f in Path(".").iterdir():
    if f.is_file() and f.suffix.lower() == ".nef":
        # 去掉 .NEF，再追加 -N.jpg
        new_name = f.with_name(f.stem + "-N.jpg")
        f.rename(new_name)
