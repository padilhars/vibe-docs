#!/usr/bin/env python3
"""
build_skill.py — Empacota a skill em dist/<nome>.skill.

O .skill é um zip cuja raiz é a pasta da skill. Arquivos ocultos e caches
ficam de fora. O zip é determinístico (datas fixas, ordem alfabética), para
que o mesmo conteúdo gere sempre o mesmo arquivo.

Uso:
    python3 tools/build_skill.py [pasta-da-skill] [pasta-de-saida]
    (padrão: vibe-docs dist)
"""
import sys
import zipfile
from pathlib import Path

SKIP_DIRS = {"__pycache__", ".git"}
FIXED_DATE = (2020, 1, 1, 0, 0, 0)


def build(skill_dir="vibe-docs", out_dir="dist"):
    src = Path(skill_dir).resolve()
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    target = out / f"{src.name}.skill"
    files = sorted(
        p for p in src.rglob("*")
        if p.is_file()
        and not any(part.startswith(".") or part in SKIP_DIRS for part in p.relative_to(src).parts)
    )
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            info = zipfile.ZipInfo(f"{src.name}/{p.relative_to(src).as_posix()}", FIXED_DATE)
            info.external_attr = (0o755 if p.suffix == ".py" else 0o644) << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, p.read_bytes())
    print(f"{target} — {len(files)} arquivos, {target.stat().st_size / 1024:.1f} KB")
    return target


if __name__ == "__main__":
    build(*sys.argv[1:3])
