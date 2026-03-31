#!/usr/bin/env python3
"""
build_zip.py
============
Maakt een gewone (niet-SCORM) gezipte kopie van de 'docs' map.

Gebruik:
    python scripts/build_zip.py [opties]

Opties:
    --version TEXT      Versienummer, bijv. "1.0" (default: datum van vandaag)
    --docs-dir PATH     Pad naar de docs map (default: docs/ naast dit script)
    --out-dir PATH      Uitvoermap voor het .zip bestand (default: releases/ naast dit script)

Het resulterende zip-bestand kan direct worden uitgepakt en in een browser
geopend via index.html, of gehost worden als statische website.
"""

import argparse
import sys
import zipfile
from datetime import date
from pathlib import Path


def build_zip(version: str, docs_dir: Path, out_dir: Path) -> Path:
    if not docs_dir.is_dir():
        sys.exit(f"Fout: docs map niet gevonden: {docs_dir}")

    out_dir.mkdir(parents=True, exist_ok=True)

    safe_version = version.replace(".", "-")
    zip_name = f"MOVEL-AI-{safe_version}.zip"
    zip_path = out_dir / zip_name

    files = sorted(p for p in docs_dir.rglob("*") if p.is_file())

    print(f"  Inpakken van {len(files)} bestanden uit '{docs_dir}' …")

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for fpath in files:
            arc_name = fpath.relative_to(docs_dir).as_posix()
            zf.write(fpath, arc_name)

    size_mb = zip_path.stat().st_size / (1024 * 1024)
    print(f"  ZIP aangemaakt: {zip_path}  ({size_mb:.1f} MB)")
    return zip_path


def main():
    parser = argparse.ArgumentParser(
        description="Maak een gewone ZIP van de docs/ map (geen SCORM)."
    )
    parser.add_argument(
        "--version",
        default=date.today().strftime("%Y.%m.%d"),
        help="Versienummer (default: datum van vandaag, bijv. 2026.03.20)",
    )
    parser.add_argument(
        "--docs-dir",
        default=None,
        help="Pad naar de docs map (default: <projectroot>/docs)",
    )
    parser.add_argument(
        "--out-dir",
        default=None,
        help="Uitvoermap voor het .zip bestand (default: <projectroot>/releases)",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent

    docs_dir = Path(args.docs_dir) if args.docs_dir else project_root / "docs"
    out_dir = Path(args.out_dir) if args.out_dir else project_root / "releases"

    print(f"ZIP builder gestart")
    print(f"  Versie   : {args.version}")
    print(f"  Docs map : {docs_dir}")
    print(f"  Uitvoer  : {out_dir}")
    print()

    zip_path = build_zip(version=args.version, docs_dir=docs_dir, out_dir=out_dir)

    print()
    print(f"Klaar! Pak '{zip_path.name}' uit en open index.html in een browser.")


if __name__ == "__main__":
    main()
