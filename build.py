import json, shutil, os
from pathlib import Path

DATA = Path("assets/minecraft")
VERSION = "v1.4"

def build(version):
    current = Path(version)
    remove_file = current / "remove.json"
    
    for root, _, files in os.walk(current):
        for file in files:
            if file == "remove.json":
                continue

            src = Path(root) / file
            rel = src.relative_to(current)
            dst = DATA / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
            print("Added/Updated:", dst)
    
    if remove_file.exists():
        with open(remove_file, "r", encoding="utf-8") as f:
            remove = json.load(f)
        
        for category, files in remove.items():
            for f_name in files:
                path = DATA / category / f_name
                if path.exists():
                    path.unlink()
                    print("Removed:", path)

build(VERSION)