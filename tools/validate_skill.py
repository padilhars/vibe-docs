#!/usr/bin/env python3
"""
validate_skill.py — Valida a estrutura da skill antes de empacotar ou publicar.

Checa:
  - SKILL.md existe e tem frontmatter com `name` e `description`
  - `name` em kebab-case, até 64 caracteres
  - `description` até 1024 caracteres, sem < ou >
  - corpo do SKILL.md abaixo de 500 linhas
  - todo caminho `references/...`, `scripts/...` ou `assets/...` citado nos .md existe
  - todo script em scripts/ compila
  - nenhum arquivo indesejado (README, CHANGELOG, __pycache__, .DS_Store) dentro da skill

Uso:
    python3 tools/validate_skill.py vibe-docs

Saída: código 0 se válida, 1 se houver erro.
"""
import re
import sys
from pathlib import Path

MAX_DESC = 1024
MAX_NAME = 64
MAX_LINES = 500
UNWANTED = {"README.md", "CHANGELOG.md", ".DS_Store", "__pycache__"}
PATH_RE = re.compile(r"`((?:references|scripts|assets)/[A-Za-z0-9_./-]+\.(?:md|py))")
# Caminhos relativos a references/ citados de dentro dos próprios arquivos de referência
REL_RE = re.compile(r"`((?:concept|blueprint|documents)/[A-Za-z0-9_.-]+\.md)`")


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip().strip('"').strip("'")
    return fields, text[m.end():]


def main(skill_dir):
    root = Path(skill_dir)
    errors, warnings = [], []
    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        print(f"ERRO: {skill_md} não existe")
        return 1

    fm, body = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    if fm is None:
        errors.append("SKILL.md sem frontmatter YAML")
        fm = {}
    name, desc = fm.get("name", ""), fm.get("description", "")
    if not name:
        errors.append("frontmatter sem `name`")
    elif not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > MAX_NAME:
        errors.append(f"`name` inválido: {name!r} (kebab-case, até {MAX_NAME})")
    elif name != root.name:
        warnings.append(f"`name` ({name}) difere do nome da pasta ({root.name})")
    if not desc:
        errors.append("frontmatter sem `description`")
    else:
        if len(desc) > MAX_DESC:
            errors.append(f"`description` com {len(desc)} caracteres (máx. {MAX_DESC})")
        if "<" in desc or ">" in desc:
            errors.append("`description` não pode conter < ou >")

    n_lines = body.count("\n")
    if n_lines > MAX_LINES:
        errors.append(f"corpo do SKILL.md com {n_lines} linhas (recomendado < {MAX_LINES})")

    for md in root.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        for ref in set(PATH_RE.findall(text)):
            if not (root / ref).exists():
                errors.append(f"{md.relative_to(root)} cita `{ref}`, que não existe")
        if "references" in md.parts:
            for ref in set(REL_RE.findall(text)):
                if not (root / "references" / ref).exists():
                    errors.append(f"{md.relative_to(root)} cita `{ref}`, que não existe")

    for py in sorted((root / "scripts").glob("*.py")):
        try:
            compile(py.read_text(encoding="utf-8"), str(py), "exec")
        except SyntaxError as e:
            errors.append(f"{py.name} não compila: linha {e.lineno}: {e.msg}")

    for p in root.rglob("*"):
        if p.name in UNWANTED:
            errors.append(f"arquivo que não deve ir no pacote: {p.relative_to(root)}")

    for w in warnings:
        print(f"AVISO: {w}")
    for e in errors:
        print(f"ERRO:  {e}")
    if errors:
        print(f"\n{len(errors)} erro(s).")
        return 1
    print(f"OK: {name} — descrição {len(desc)}/{MAX_DESC} caracteres, SKILL.md com {n_lines} linhas.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
