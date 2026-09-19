#!/usr/bin/env python3
import re
import shutil
import markdown
from pathlib import Path

SRC        = Path("/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit")
DEPLOY     = Path("/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit-deploy")
DEPLOY_ART = DEPLOY / "articles"

ARTICLES_DIR   = SRC / "articles"
TEMPLATE       = (SRC / "articles" / "article_template.html").read_text()
INDEX_TEMPLATE = (SRC / "index_template.html").read_text()




# ── NEW: math protection helpers ──────────────────────────────────────────
# Python-Markdown mangles LaTeX: it eats "_", "^", "\\", and "&" inside
# formulas, wraps display math in <p> tags, and escapes backslashes.
# We mask math regions with placeholders before Markdown runs, then put
# the original text back afterwards. KaTeX then renders it client-side.
MATH_RE = re.compile(
    r'(\$\$.*?\$\$|\$[^$\n]+?\$)',
    re.DOTALL
)

def protect_math(md_text):
    """Replace math blocks with placeholders before Markdown conversion."""
    store = []
    def repl(m):
        store.append(m.group(0))
        return f"\x00MATH{len(store)-1}\x00"
    return MATH_RE.sub(repl, md_text), store

def restore_math(html_text, store):
    """Put math blocks back into the rendered HTML."""
    for i, chunk in enumerate(store):
        html_text = html_text.replace(f"\x00MATH{i}\x00", chunk)
    return html_text

def md_to_html(md_text):
    """Markdown → HTML with math regions preserved verbatim."""
    protected, store = protect_math(md_text)
    html = markdown.markdown(protected, extensions=["extra", "toc"])
    return restore_math(html, store)
# ──────────────────────────────────────────────────────────────────────────


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

def heading_title(text):
    """Title from the article's first H1 heading.

    Headings appear in three shapes across the corpus: `# Title`,
    `# __Title__`, and `# __Coordinate — Title__` (the last is handled
    by parse_frontmatter and never reaches here). Returns "" if the
    text opens with something other than a heading.
    """
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            return s.lstrip("#").strip().strip("_*").strip()
        break
    return ""


# ── CHANGED: Disclaimer now comes *before* Contact, both at the end ──
def build_nav_index(articles):
    items = []
    items.append('<li><a href="maths.html">Maths</a></li>')
    items.append('<li><a href="physics.html">Physics</a></li>')
    items.append('<li><a href="disclaimer.html">Disclaimer</a></li>')
    items.append('<li><a href="contact.html">Contact</a></li>')
    return "\n      ".join(items)

def build_nav_article(articles, current_stem=None):
    items = []
    items.append('<li><a href="../maths.html">Maths</a></li>')
    items.append('<li><a href="../physics.html">Physics</a></li>')
    items.append('<li><a href="../disclaimer.html">Disclaimer</a></li>')
    items.append('<li><a href="../contact.html">Contact</a></li>')
    return "\n      ".join(items)
# ─────────────────────────────────────────────────────────────────────


def article_sort_key(p):
    name = p.stem.lower()
    if "framework" in name:
        group = 0
    elif "module" in name:
        group = 1
    else:
        group = 2
    return (group, name)

articles = sorted(ARTICLES_DIR.glob("*.md"), key=article_sort_key)
nav_articles = [p for p in articles if "zexample" not in p.stem.lower()]
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
    # parse_frontmatter always defines "title" (default ""), so .get()'s
    # default never fires — fall back explicitly. Read the heading before
    # strip_title_line removes it.
    title = meta.get("title") or heading_title(body_md) or label_from_stem(f.stem)
    body_md = strip_title_line(body_md)

    body_html = md_to_html(body_md)

    html = (TEMPLATE
        .replace("{title}",      title)
        .replace("{coordinate}", meta.get("coordinate", ""))
        .replace("{nav}",        build_nav_article(nav_articles, current_stem=f.stem))
        .replace("{body}",       body_html)
    )
    (DEPLOY_ART / f"{f.stem}.html").write_text(html)
    print(f"Built: articles/{f.stem}.html")

# ── NEW: prune orphaned article HTML ──────────────────────────────────────
# We only ever write files into the deploy dir, never delete, so a renamed
# or removed source md leaves its old .html behind — still served, still
# indexable, and silently diverging from the current article. Drop any
# deployed article page that no longer has a matching source.
built = {f"{f.stem}.html" for f in articles}
for stale in DEPLOY_ART.glob("*.html"):
    if stale.name not in built:
        stale.unlink()
        print(f"Removed orphan: articles/{stale.name}")
# ──────────────────────────────────────────────────────────────────────────

def build_root_page(md_path, out_name, articles):
    if md_path.exists():
        raw = md_path.read_text()
        meta, body_md = parse_frontmatter(raw)
        body_md = strip_title_line(body_md)

        body_html = md_to_html(body_md)

        html = (INDEX_TEMPLATE
            .replace("{nav}",         build_nav_index(articles))
            .replace("{index_items}", body_html)
        )
        (DEPLOY / out_name).write_text(html)
        print(f"Built: {out_name}")
    else:
        print(f"Warning: {md_path.name} not found at {md_path}")

build_root_page(SRC / "index.md",      "index.html",      nav_articles)
build_root_page(SRC / "maths.md", "maths.html", nav_articles)
build_root_page(SRC / "physics.md", "physics.html", nav_articles)
build_root_page(SRC / "disclaimer.md", "disclaimer.html", nav_articles)
build_root_page(SRC / "contact.md",    "contact.html",    nav_articles)

print("Done.")

