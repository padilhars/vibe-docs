#!/usr/bin/env python3
"""
build_site.py — Gera o site (GitHub Pages) a partir de site/ e docs/.

- site/ é copiado como está (página inicial e assets).
- Cada arquivo de docs/ listado em NAV vira _site/docs/<nome>.html, com o
  mesmo visual da página inicial, menu das três trilhas e anterior/próxima.
- Links entre arquivos de docs/ viram links entre páginas; links para a skill
  ou para arquivos da raiz do repositório passam a apontar para o GitHub.

Uso:
    pip install markdown
    python3 tools/build_site.py [pasta-de-saida]     (padrão: _site)
"""
import html
import re
import shutil
import sys
import unicodedata
from pathlib import Path

import markdown

REPO = "https://github.com/padilhars/vibe-docs"
ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"

# Trilhas e ordem das páginas. Edite aqui para mudar o menu.
NAV = [
    ("Manual do usuário", [
        "instalacao.md", "guia-de-uso.md", "conceitos.md",
        "documentos.md", "handoff-claude-code.md", "faq.md",
    ]),
    ("Guia do administrador", ["guia-do-admin.md"]),
    ("Documentação técnica", ["arquitetura-da-skill.md", "scripts.md", "ci-e-release.md"]),
]
EXTRA_LINKS = [("Contribuindo", f"{REPO}/blob/main/CONTRIBUTING.md"),
               ("Changelog", f"{REPO}/blob/main/CHANGELOG.md")]


def slugify(value, separator="-"):
    """Mesmo formato das âncoras do GitHub: minúsculas, sem pontuação, espaço vira hífen."""
    value = unicodedata.normalize("NFC", value).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.U)
    return re.sub(r"\s", separator, value)


def title_of(text):
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else "Documentação"


def rewrite_links(text, src):
    """Ajusta destinos de links Markdown para o site publicado."""
    def fix(m):
        label, target = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            return m.group(0)
        path, _, anchor = target.partition("#")
        anchor = f"#{anchor}" if anchor else ""
        resolved = (src.parent / path).resolve()
        try:
            rel = resolved.relative_to(DOCS)
            if rel.suffix == ".md":
                return f"[{label}]({rel.with_suffix('.html').as_posix()}{anchor})"
        except ValueError:
            pass
        rel_repo = resolved.relative_to(ROOT).as_posix()
        kind = "tree" if resolved.is_dir() else "blob"
        return f"[{label}]({REPO}/{kind}/main/{rel_repo}{anchor})"
    return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", fix, text)


def render(text):
    md = markdown.Markdown(
        extensions=["tables", "fenced_code", "toc", "sane_lists"],
        extension_configs={"toc": {"slugify": slugify}},
    )
    out = md.convert(text)
    out = re.sub(r"<table>", '<div class="table-wrap"><table>', out)
    out = out.replace("</table>", "</table></div>")
    # links externos abrem em nova aba
    out = re.sub(r'<a href="(https?://[^"]+)"', r'<a href="\1" target="_blank" rel="noopener"', out)
    return out


def nav_html(current, titles):
    parts = []
    for track, files in NAV:
        items = "".join(
            f'<li><a href="{f[:-3]}.html"{" aria-current=page" if f == current else ""}>'
            f"{html.escape(titles[f])}</a></li>" for f in files)
        parts.append(f'<p class="nav-track">{html.escape(track)}</p><ul>{items}</ul>')
    extra = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{n} ↗</a></li>' for n, u in EXTRA_LINKS)
    parts.append(f'<p class="nav-track">Projeto</p><ul>{extra}</ul>')
    return "".join(parts)


def page(title, body, current, titles, prev_next, track):
    nav = nav_html(current, titles)
    pn = ""
    if prev_next:
        prev, nxt = prev_next
        a = f'<a class="pn prev" href="{prev[:-3]}.html"><small>Anterior</small>{html.escape(titles[prev])}</a>' if prev else "<span></span>"
        b = f'<a class="pn next" href="{nxt[:-3]}.html"><small>Próxima</small>{html.escape(titles[nxt])}</a>' if nxt else "<span></span>"
        pn = f'<nav class="prevnext" aria-label="Navegação entre páginas">{a}{b}</nav>'
    edit = f'{REPO}/edit/main/docs/{current}' if current else f"{REPO}/tree/main/docs"
    crumb = f'<p class="crumb">{html.escape(track)}</p>' if track else ""
    return TEMPLATE.format(
        title=html.escape(title), nav=nav, body=body, prevnext=pn, edit=edit, crumb=crumb,
        index_current=' aria-current="page"' if current is None else "")


def build(out_dir="_site"):
    out = ROOT / out_dir
    if out.exists():
        shutil.rmtree(out)
    shutil.copytree(SITE, out)
    (out / "docs").mkdir(exist_ok=True)

    order = [f for _, files in NAV for f in files]
    missing = [f for f in order if not (DOCS / f).exists()]
    if missing:
        sys.exit(f"Arquivos listados em NAV que não existem: {missing}")
    unlisted = sorted(p.name for p in DOCS.glob("*.md") if p.name not in order + ["index.md"])
    if unlisted:
        print(f"AVISO: fora do menu: {unlisted}")

    titles = {f: title_of((DOCS / f).read_text(encoding="utf-8")) for f in order}
    track_of = {f: t for t, files in NAV for f in files}

    for i, f in enumerate(order):
        src = DOCS / f
        body = render(rewrite_links(src.read_text(encoding="utf-8"), src))
        prev_next = (order[i - 1] if i > 0 else None, order[i + 1] if i + 1 < len(order) else None)
        (out / "docs" / f"{f[:-3]}.html").write_text(
            page(titles[f], body, f, titles, prev_next, track_of[f]), encoding="utf-8")

    idx = DOCS / "index.md"
    body = render(rewrite_links(idx.read_text(encoding="utf-8"), idx))
    (out / "docs" / "index.html").write_text(
        page("Documentação", body, None, titles, None, None), encoding="utf-8")
    (out / ".nojekyll").write_text("")
    print(f"{out.relative_to(ROOT)}/ — página inicial + {len(order) + 1} páginas de documentação")


TEMPLATE = """<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title} · Vibe-Docs</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@112..125,500..800&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="../assets/docs.css">
</head>
<body>
<header class="top">
  <div class="top-inner">
    <a class="brand" href="../index.html">
      <svg width="20" height="20" viewBox="0 0 22 22" aria-hidden="true"><rect x="1" y="1" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M1 15h20M8 15v6M14 15v6" stroke="currentColor" stroke-width="1.2"/><path d="M5 5h12M5 9h8" stroke="currentColor" stroke-width="1.6"/></svg>
      VIBE-DOCS
    </a>
    <nav class="top-nav" aria-label="Site">
      <a href="index.html"{index_current}>Documentação</a>
      <a href="https://github.com/padilhars/vibe-docs/releases/latest/download/vibe-docs.skill">Baixar</a>
      <a href="https://github.com/padilhars/vibe-docs" target="_blank" rel="noopener">GitHub</a>
    </nav>
  </div>
</header>
<div class="layout">
  <aside class="side">
    <details class="side-menu" open>
      <summary>Menu da documentação</summary>
      <nav aria-label="Documentação">{nav}</nav>
    </details>
  </aside>
  <main class="doc">
    {crumb}
    <article class="prose">
{body}
    </article>
    {prevnext}
    <p class="edit"><a href="{edit}" target="_blank" rel="noopener">Editar esta página no GitHub</a></p>
  </main>
</div>
<script>
  // No celular o menu começa recolhido; no desktop, aberto.
  var m = document.querySelector('.side-menu');
  if (m && window.matchMedia('(max-width: 860px)').matches) m.open = false;
</script>
</body>
</html>
"""

if __name__ == "__main__":
    build(*sys.argv[1:2])
