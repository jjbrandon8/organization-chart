#!/usr/bin/env python3
"""Create the 9 functional areas of an organization as empty folders.

Usage:
  python create_org_chart.py --dest PATH --lang es|en [--zip]

Only creates folders. Never creates, changes or deletes files. Safe to run twice.
"""
import argparse
import shutil
import sys
import zipfile
from pathlib import Path

AREAS = {
    "es": [
        "01-direccion",
        "02-administracion",
        "03-finanzas",
        "04-talento-humano",
        "05-comercial",
        "06-operaciones",
        "07-logistica-compras",
        "08-tecnologia",
        "09-legal",
    ],
    "en": [
        "01-management",
        "02-administration",
        "03-finance",
        "04-human-resources",
        "05-sales-marketing",
        "06-operations",
        "07-logistics-procurement",
        "08-technology",
        "09-legal",
    ],
}


def zip_folders(dest: Path) -> Path:
    """Zip dest with its empty folders (shutil.make_archive would drop them)."""
    archive = dest.with_suffix(".zip")
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr(f"{dest.name}/", "")
        for folder in sorted(p for p in dest.iterdir() if p.is_dir()):
            z.writestr(f"{dest.name}/{folder.name}/", "")
    return archive


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--dest", required=True, help="Absolute path of the folder that holds the areas")
    p.add_argument("--lang", choices=sorted(AREAS), default="en", help="Language of the folder names")
    p.add_argument("--zip", action="store_true", help="Also write <dest>.zip (for environments without a disk)")
    a = p.parse_args()

    dest = Path(a.dest).expanduser().resolve()
    created, existing = [], []
    for name in AREAS[a.lang]:
        folder = dest / name
        (existing if folder.is_dir() else created).append(name)
        folder.mkdir(parents=True, exist_ok=True)

    print(f"dest: {dest}")
    print(f"created: {len(created)}")
    for name in existing:
        print(f"already existed: {name}")
    if a.zip:
        print(f"zip: {zip_folders(dest)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
