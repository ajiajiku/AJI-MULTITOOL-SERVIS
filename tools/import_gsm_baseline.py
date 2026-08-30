#!/usr/bin/env python3
"""Import the supplied GSM Laboratory MTK Python baseline into this project.

Usage:
    python tools/import_gsm_baseline.py "C:\\path\\MTK GSM LABORATORY.zip"

The importer copies the reusable MTK/GUI source while deliberately excluding
security-bypass payload/exploit modules. Existing project files are not deleted.
"""
from __future__ import annotations
import argparse, os, re, shutil, tempfile, zipfile
from pathlib import Path

SKIP = {
    "Library/kamakiri.py",
    "Library/pltools.py",
    "Library/seccfg.py",
}


def find_root(extract: Path) -> Path:
    candidates = list(extract.rglob("mtkclient"))
    for p in candidates:
        if (p / "Library").is_dir() and (p / "config").is_dir():
            return p
    raise RuntimeError("mtkclient source tree was not found in the archive")


def sanitize(path: str, text: str) -> str:
    text = text.replace("mtkclient", "mtk")
    # Remove GUI entry points that explicitly invoke the disabled seccfg action.
    if path.endswith("gui/toolsMenu.py"):
        text = text.replace('self.parent.Status["result"] = self.mtkClass.daloader.seccfg(parameters[0])',
                            'self.parent.Status["result"] = (False, "Security configuration is handled externally.")')
    # The imported core must not expose the old payload-based bypass method.
    if path.endswith("Library/mtk.py"):
        text = re.sub(r"\n    def patch_preloader_security\(self, data\):.*?(?=\n    def parse_preloader)", "\n", text, flags=re.S)
        text = re.sub(r"\n    def crasher\(self, display=True, mode=None\):.*?(?=\n    def bypass_security)", "\n", text, flags=re.S)
        text = re.sub(r"\n    def bypass_security\(self\):.*?\Z", "\n", text, flags=re.S)
        text = text.replace("from mtk.Library.pltools import PLTools\n", "")
    # Make security configuration an explicit unsupported operation instead of
    # retaining an unlock implementation.
    if path.endswith(("Library/xflash_ext.py", "Library/legacy_ext.py")):
        text = re.sub(r"(?m)^    def seccfg\(self, lockflag\):.*?(?=^    def |\Z)",
                      '    def seccfg(self, lockflag):\n        raise RuntimeError("Security configuration is handled externally.")\n\n',
                      text, flags=re.S)
    return text


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", help="GSM Laboratory ZIP/RAR-extracted ZIP containing mtkclient")
    ap.add_argument("--dest", default=".", help="AJI MULTITOOL SERVIS repository root")
    args = ap.parse_args()
    archive = Path(args.archive).expanduser().resolve()
    dest = Path(args.dest).resolve()
    if not archive.is_file():
        raise SystemExit(f"Archive not found: {archive}")
    with tempfile.TemporaryDirectory() as td:
        with zipfile.ZipFile(archive) as z:
            z.extractall(td)
        root = find_root(Path(td))
        copied = 0
        for src in root.rglob("*"):
            if not src.is_file():
                continue
            rel = src.relative_to(root).as_posix()
            if rel in SKIP:
                continue
            out = dest / "mtk" / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            if src.suffix.lower() in {".py", ".ui", ".sh"}:
                out.write_text(sanitize(rel, src.read_text(encoding="utf-8", errors="replace")), encoding="utf-8")
            else:
                shutil.copy2(src, out)
            copied += 1
    print(f"Imported {copied} reusable baseline files into {dest / 'mtk'}")
    print("Security-bypass payload/exploit modules were intentionally excluded.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
