#!/usr/bin/env python3
import re
import shutil
import markdown
from pathlib import Path

SRC        = Path("/home/hp/Documents/1_Doc/Projects/ai-research-unit/ai-research-unit/systems-analysis")
DEPLOY     = Path("/home/hp/Documents/1_Doc/Projects/ai-research-unit/ai-research-unit-deploy/systems-analysis")
DEPLOY_ART = DEPLOY / "articles"

ARTICLES_DIR   = SRC / "articles"
TEMPLATE       = (SRC / "articles" / "article_template.html").read_text()
INDEX_TEMPLATE = (SRC / "index_template.html").read_text()

def parse_frontmatter(text):
    meta = {"title": "", "coordinate": ""}
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, _, val = line.partition(":")
                    meta[key.strip()] = val.strip()
            return meta, parts[2].strip()
    first_line = text.splitlines()[0] if text.splitlines() else ""
    m = re.match(r"#\s*__(.+?)\s*—\s*(.+?)__", first_line)
    if m:
        meta["coordinate"] = m.group(1).strip()
        meta["title"]      = m.group(2).strip()
        return meta, "\n".join(text.splitlines()[1:]).strip()
    return meta, text

def strip_title_line(text):
    lines = text.splitlines()
    if lines and re.match(r"#\s*__(.+?)__", lines[0]):
        return "\n".join(lines[1:]).strip()
    return text

def label_from_stem(stem):
    return stem.replace("-", " ").replace("_", " ").title()

def build_nav_index(articles):
    items = []
    items.append('<li><a href="disclaimer.html">Disclaimer</a></li>')
    for f in articles:
        items.append(f'<li><a href="articles/{f.stem}.html">{label_from_stem(f.stem)}</a></li>')
    items.append('<li><a href="contact.html">Contact</a></li>')
    return "\n      ".join(items)

def build_nav_article(articles, current_stem=None):
    items = []
    items.append('<li><a href="../disclaimer.html">Disclaimer</a></li>')
    for f in articles:
        active = ' class="active"' if f.stem == current_stem else ""
        items.append(f'<li><a href="{f.stem}.html"{active}>{label_from_stem(f.stem)}</a></li>')
    items.append('<li><a href="../contact.html">Contact</a></li>')
    return "\n      ".join(items)

articles = sorted(ARTICLES_DIR.glob("*.md"))
if not articles:
    print("No md files found in articles/. Add some and re-run.")
    exit(0)

DEPLOY.mkdir(parents=True, exist_ok=True)
DEPLOY_ART.mkdir(parents=True, exist_ok=True)

src_assets = SRC / "assets"
deploy_assets = DEPLOY / "assets"
if src_assets.exists():
    if deploy_assets.exists():
        shutil.rmtree(deploy_assets)
    shutil.copytree(src_assets, deploy_assets)
    print("Copied assets/")

for f in articles:
    raw = f.read_text()
    meta, body_md = parse_frontmatter(raw)
    body_md = strip_title_line(body_md)
    body_html = markdown.markdown(body_md, extensions=["extra", "toc"])
    html = (TEMPLATE
        .replace("{title}",      meta.get("title", label_from_stem(f.stem)))
        .replace("{coordinate}", meta.get("coordinate", ""))
        .replace("{nav}",        build_nav_article(articles, current_stem=f.stem))
        .replace("{body}",       body_html)
    )
    (DEPLOY_ART / f"{f.stem}.html").write_text(html)
    print(f"Built: articles/{f.stem}.html")

def build_root_page(md_path, out_name, articles):
    if md_path.exists():
        raw = md_path.read_text()
        meta, body_md = parse_frontmatter(raw)
        body_md = strip_title_line(body_md)
        body_html = markdown.markdown(body_md, extensions=["extra", "toc"])
        html = (INDEX_TEMPLATE
            .replace("{nav}",         build_nav_index(articles))
            .replace("{index_items}", body_html)
        )
        (DEPLOY / out_name).write_text(html)
        print(f"Built: {out_name}")
    else:
        print(f"Warning: {md_path.name} not found at {md_path}")

build_root_page(SRC / "index.md",      "index.html",      articles)
build_root_page(SRC / "disclaimer.md", "disclaimer.html", articles)
build_root_page(SRC / "contact.md",    "contact.html",    articles)

print("Done.")
