#!/usr/bin/env python3
"""Build ``guide.html`` from 35 chapters and 13 public excerpts.

The guide shell and About block live in ``guide.template.html``.  Use
``--bootstrap-template`` once to extract that shell from the legacy embedded
guide, then use the ordinary build for every source change.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "guide.template.html"
OUTPUT = ROOT / "guide.html"
PLACEHOLDER = "{{MD_KO}}"
TEXTAREA_RE = re.compile(
    r'(<textarea id="md-source-ko"[^>]*>\n?)(.*?)(\n?</textarea>)', re.DOTALL
)


def source_files() -> list[Path]:
    chapters = sorted(ROOT.glob("chapter_*.md"))
    excerpts = sorted((ROOT / "excerpts").glob("excerpt_*.md"))
    if len(chapters) != 35 or len(excerpts) != 13:
        raise RuntimeError(
            f"expected 35 chapters and 13 excerpts, found {len(chapters)} and {len(excerpts)}"
        )
    return chapters + excerpts


def escape_textarea(text: str) -> str:
    return text.replace("</textarea>", "&lt;/textarea&gt;")


def bootstrap_template() -> None:
    if TEMPLATE.exists():
        raise RuntimeError(f"template already exists: {TEMPLATE}")
    shell = OUTPUT.read_text(encoding="utf-8")
    match = TEXTAREA_RE.search(shell)
    if not match:
        raise RuntimeError("Korean Markdown textarea not found in guide.html")
    first_chapter = re.search(r"(?m)^#\s+Ch\.?\s*1\b", match.group(2))
    if not first_chapter:
        raise RuntimeError("first chapter heading not found in embedded Markdown")
    about = match.group(2)[: first_chapter.start()]
    replacement = match.group(1) + about + PLACEHOLDER + match.group(3)
    template = shell[: match.start()] + replacement + shell[match.end() :]
    TEMPLATE.write_text(template, encoding="utf-8")
    print(f"Bootstrapped {TEMPLATE}")


def build() -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count(PLACEHOLDER) != 1:
        raise RuntimeError(f"template must contain exactly one {PLACEHOLDER}")
    sources = [path.read_text(encoding="utf-8").rstrip() for path in source_files()]
    markdown = "\n\n".join(sources) + "\n"
    html = template.replace(PLACEHOLDER, escape_textarea(markdown))
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"Built {OUTPUT}")
    print(f"  source units: {len(sources)}")
    print(f"  Markdown: {len(markdown):,} chars")
    print(f"  HTML: {len(html):,} chars")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bootstrap-template", action="store_true")
    args = parser.parse_args()
    if args.bootstrap_template:
        bootstrap_template()
    build()


if __name__ == "__main__":
    main()
