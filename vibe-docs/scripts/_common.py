"""
_common.py — utilidades compartilhadas pelos scripts da vibe-docs.

Existe para que os seis scripts leiam um projeto do mesmo jeito: mesmo padrão
de ID, mesma lista de tokens técnicos, mesma forma de achar o CLAUDE.md e de
ler uma seção do Blueprint. Antes cada script tinha a sua cópia, e as cópias
divergiam.

Layout aceito (ver "Layout do projeto" no SKILL.md):
  - durante a documentação: todos os .md numa pasta só;
  - depois do handoff: CLAUDE.md na raiz do repositório e o restante em docs/.
Os scripts recebem a pasta que contém o PROJECT.md e procuram o CLAUDE.md
nela ou na pasta imediatamente acima.
"""

import re
from pathlib import Path

PROJECT_FILENAME = "PROJECT.md"
CLAUDE_MD = "CLAUDE.md"

# PREFIXO-NUMERO delimitado: "BR-10" não casa dentro de "BR-100" nem de "XBR-10".
ID_PATTERN = re.compile(r"(?<![A-Za-z0-9-])([A-Z]{1,6}-\d{1,4})(?!\d)")

STANDARD_PREFIXES = {"OBJ", "FUN", "UC", "BR", "ENT", "REQ", "PRINC", "US", "TASK", "API"}

# Nascem em documentos derivados, não no Blueprint (ver _shared-rules.md).
DOCUMENT_LOCAL_PREFIXES = {"US", "TASK", "API"}

# Casam com o padrão de ID sem serem ID de rastreabilidade.
TECH_TOKENS = {
    "AES-256", "AES-128", "SHA-256", "SHA-1", "SHA-512", "HMAC-256", "RSA-2048",
    "RSA-4096", "UTF-8", "UTF-16", "ISO-8601", "ISO-27001", "RFC-2119", "RFC-5545",
    "SPF-1", "BASE-64", "HTTP-2", "HTTP-3", "TLS-1", "OAUTH-2", "ARGON-2", "P-256",
    "ES-256", "RS-256", "HS-256", "WCAG-2", "GPT-4", "GPT-5",
}

# Mantidos pelo agente de implementação: não levam frontmatter nem versão.
AGENT_MAINTAINED = {"STATE.md", "LEARNINGS.md"}

# Arquivos .md comuns numa pasta de projeto que não são documentos da skill.
NOT_PROJECT_DOCS = {"README.md", "CHANGELOG.md", "LICENSE.md", "CONTRIBUTING.md"}

# Linha de marcador do template ainda não preenchida: "- BR-01: PENDENTE".
_PLACEHOLDER = re.compile(r"^\s*[-*]?\s*[A-Z]{1,6}-\d{1,4}(\s*\([^)]*\))?\s*:\s*PENDENTE\b")


def prefix_of(identifier: str) -> str:
    return identifier.split("-")[0]


def extract_ids(text: str) -> set:
    """Todos os IDs citados num texto, sem os tokens técnicos."""
    return {i for i in ID_PATTERN.findall(text) if i not in TECH_TOKENS}


def has_id(text: str, identifier: str) -> bool:
    """True se o ID aparece como ID inteiro (não como trecho de outro)."""
    return identifier in extract_ids(text)


def blueprint_ids(text: str) -> set:
    """IDs que o Blueprint realmente define.

    Ignora marcadores do template ainda em PENDENTE e IDs locais de documento
    (US/TASK/API) que o Blueprint apenas cita, por exemplo no histórico.
    """
    ids = set()
    for line in text.splitlines():
        if _PLACEHOLDER.match(line):
            continue
        ids |= extract_ids(line)
    return {i for i in ids if prefix_of(i) not in DOCUMENT_LOCAL_PREFIXES}


def section_body(lines, number):
    """Corpo da seção '## <number>. ...' do Blueprint, ou None se não existir."""
    start = None
    pattern = re.compile(rf"^##\s*{number}\.")
    for i, line in enumerate(lines):
        if pattern.match(line.strip()):
            start = i
            break
    if start is None:
        return None
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if re.match(r"^##\s", lines[i].strip()):
            end = i
            break
    return "\n".join(lines[start + 1:end]).strip()


def field_value(section_text: str, label: str):
    """Valor de um campo '**Rótulo:** valor' dentro de uma seção (até o próximo campo)."""
    m = re.search(
        rf"\*\*{re.escape(label)}:?\*\*:?\s*(.*?)(?=\n\s*\*\*[^*\n]+:?\*\*|\Z)",
        section_text or "",
        re.DOTALL | re.IGNORECASE,
    )
    return m.group(1).strip() if m else None


def locate_claude_md(project_dir: Path):
    """CLAUDE.md na pasta do projeto ou, depois do handoff, na pasta acima."""
    for candidate in (project_dir / CLAUDE_MD, project_dir.resolve().parent / CLAUDE_MD):
        if candidate.exists():
            return candidate
    return None


def project_files(project_dir: Path) -> dict:
    """nome -> Path de cada documento do projeto (inclui CLAUDE.md da pasta acima)."""
    files = {
        p.name: p
        for p in sorted(project_dir.glob("*.md"))
        if p.name not in NOT_PROJECT_DOCS
    }
    claude = locate_claude_md(project_dir)
    if claude is not None:
        files[CLAUDE_MD] = claude
    return files


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def critical_pendencies(blueprint_lines) -> list:
    """Pendências críticas em aberto na seção 16.

    Aceita marcador com '-', '*' ou numeração, e também itens escritos na
    mesma linha do rótulo ('**Críticas:** a; b').
    """
    body = section_body(blueprint_lines, 16)
    if not body:
        return []
    items, inside = [], False
    for raw in body.splitlines():
        line = raw.strip()
        plain = re.sub(r"[*_`#]", "", line)
        plain = re.sub(r"^\s*(?:[-•]|\d+[.)])\s*", "", plain).strip()
        low = plain.lower()
        if re.match(r"^cr[ií]ticas?\b", low):
            inside = True
            rest = re.sub(r"^cr[ií]ticas?\s*:?\s*", "", plain, flags=re.IGNORECASE)
            items += [p.strip() for p in rest.split(";") if p.strip()]
            continue
        if re.match(r"^menor(es)?\b", low):
            inside = False
            continue
        if inside and re.match(r"^\s*(?:[-*•]|\d+[.)])\s+", raw) and plain:
            items.append(plain)
    return [i for i in items if not re.match(r"^(nenhuma|n/a|—|-)\b", i.lower()) and i.lower() not in {"—", "-"}]
