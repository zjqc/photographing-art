# restore_nef.py
from pathlib import Path

for f in Path(".").iterdir():
    name_lower = f.name.lower()
    if f.is_file() and name_lower.endswith("-n.jpg"):
        # 去掉后缀 -N.jpg（6 个字符），再加回 .NEF
        base = f.name[:-6]           # 去掉 "-N.jpg"
        new_name = f.with_name(base + ".NEF")
        f.rename(new_name)
