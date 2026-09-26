#!/usr/bin/env python3
import re
import shutil
import markdown
from pathlib import Path

SRC        = Path("/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit")
DEPLOY     = Path("/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit-deploy")

TEMPLATE       = (SRC / "article_template.html").read_text()
INDEX_TEMPLATE = (SRC / "index_template.html").read_text()

# The corpus is split into two independent collections, each with its own
# source folder, its own deploy folder, and its own menu page. A slug belongs
# to exactly one collection — the menus are disjoint — so an article's file
# location is determined by which menu links it.
COLLECTIONS = [
    {"name": "maths",   "src": SRC / "articles_maths",   "deploy": DEPLOY / "articles_maths"},
    {"name": "physics", "src": SRC / "articles_physics", "deploy": DEPLOY / "articles_physics"},
]




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

TABLE_RE = re.compile(r"<table>.*?</table>", re.DOTALL)

# Markdown requires a header row, so a table that has none (the bare
# Mermin-Peres square) comes through with a fully empty <thead>. Drop it, or it
# renders as a shaded band above the data.
EMPTY_THEAD_RE = re.compile(
    r"<thead>\s*<tr>\s*(?:<th[^>]*>\s*</th>\s*)+</tr>\s*</thead>", re.DOTALL)

def drop_empty_thead(html_text):
    return EMPTY_THEAD_RE.sub("", html_text)

def wrap_tables(html_text):
    """Wrap each table in its own scroll container.

    A <table> cannot clip its own overflow, and setting display:block on it does
    not reliably contain the scroll in Chrome (the anonymous table box escapes),
    so wide tables would widen the whole page. A wrapper div does contain it.
    """
    html_text = drop_empty_thead(html_text)
    return TABLE_RE.sub(lambda m: f'<div class="table-scroll">{m.group(0)}</div>', html_text)

def md_to_html(md_text):
    """Markdown → HTML with math regions preserved verbatim."""
    protected, store = protect_math(md_text)
    html = markdown.markdown(protected, extensions=["extra", "toc"])
    return wrap_tables(restore_math(html, store))
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
    # The article's first H1 is its *visible* title: the templates render
    # {title} only inside <head>, so the on-page heading comes from the body.
    # Two consequences, both load-bearing:
    #   * the H1 is never removed from the body — stripping it makes the page
    #     render with no title at all;
    #   * the line is located by scanning past leading blank lines, so an
    #     article that opens with `# __Title__` builds exactly like one that
    #     opens with a blank line first.
    # {title} must be the *whole* heading, subtitle included: for the
    # `__Title — Subtitle__` form the two halves are recorded separately, but
    # the tab title keeps both.
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"#\s*__(.+?)__\s*$", s)
        if m:
            inner = m.group(1).strip()
            meta["title"] = inner
            halves = re.split(r"\s+—\s+", inner, 1)
            if len(halves) == 2:
                meta["coordinate"] = halves[0].strip()
        break
    return meta, text

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

articles = []
for coll in COLLECTIONS:
    coll["articles"] = sorted(coll["src"].glob("*.md"), key=article_sort_key)

if not any(c["articles"] for c in COLLECTIONS):
    print("No md files found in articles_maths/ or articles_physics/. Add some and re-run.")
    exit(0)

DEPLOY.mkdir(parents=True, exist_ok=True)
for coll in COLLECTIONS:
    coll["deploy"].mkdir(parents=True, exist_ok=True)

src_assets = SRC / "assets"
deploy_assets = DEPLOY / "assets"
if src_assets.exists():
    if deploy_assets.exists():
        shutil.rmtree(deploy_assets)
    shutil.copytree(src_assets, deploy_assets)
    print("Copied assets/")

for name in ("robots.txt", ".nojekyll", ".gitlab-ci.yml"):
    if (SRC / name).exists():
        shutil.copy(SRC / name, DEPLOY / name)
        print(f"Copied {name}")

# nav_articles is only used for the {nav} placeholder, which renders the same
# four links on every page regardless of the current article, so the pool it is
# drawn from does not matter.
nav_articles = [p for coll in COLLECTIONS for p in coll["articles"]
                if "zexample" not in p.stem.lower()]

for coll in COLLECTIONS:
    if not coll["articles"]:
        print(f"Warning: no md files in {coll['src'].name}/")
        continue
    for f in coll["articles"]:
        raw = f.read_text()
        meta, body_md = parse_frontmatter(raw)
        # parse_frontmatter always defines "title" (default ""), so .get()'s
        # default never fires — fall back explicitly.
        title = meta.get("title") or heading_title(body_md) or label_from_stem(f.stem)

        body_html = md_to_html(body_md)

        html = (TEMPLATE
            .replace("{title}",      title)
            .replace("{coordinate}", meta.get("coordinate", ""))
            .replace("{nav}",        build_nav_article(nav_articles, current_stem=f.stem))
            .replace("{body}",       body_html)
        )
        (coll["deploy"] / f"{f.stem}.html").write_text(html)
        print(f"Built: {coll['src'].name}/{f.stem}.html")

# ── prune orphaned article HTML ───────────────────────────────────────────
# We only ever write files into the deploy dir, never delete, so a renamed
# or removed source md leaves its old .html behind — still served, still
# indexable, and silently diverging from the current article. Drop any
# deployed article page that no longer has a matching source. This also
# removes pages left in a collection by a file that moved to the other one.
for coll in COLLECTIONS:
    built = {f"{f.stem}.html" for f in coll["articles"]}
    for stale in coll["deploy"].glob("*.html"):
        if stale.name not in built:
            stale.unlink()
            print(f"Removed orphan: {coll['src'].name}/{stale.name}")
# ──────────────────────────────────────────────────────────────────────────

# ── prune the pre-split deploy directory ──────────────────────────────────
# Before the split every page was written to <deploy>/articles/. Those pages
# are now superseded by the two per-collection directories, and leaving them
# would publish each article twice at the old URL.
legacy_art = DEPLOY / "articles"
if legacy_art.is_dir():
    shutil.rmtree(legacy_art)
    print("Removed legacy deploy directory: articles/")
# ──────────────────────────────────────────────────────────────────────────

def build_root_page(md_path, out_name, articles):
    if md_path.exists():
        raw = md_path.read_text()
        meta, body_md = parse_frontmatter(raw)

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

# ── Convention check (non-fatal) ──────────────────────────────────────────────
# Reports shared symbols given conflicting definitions across articles — the class of
# defect the ordering rules cannot see. Never fails the build; the report is advisory.
_conv = SRC / "_reserve" / "convention_check.py"
if _conv.exists():
    try:
        import subprocess, sys
        _r = subprocess.run([sys.executable, str(_conv)], capture_output=True, text=True)
        print(_r.stdout.strip() or _r.stderr.strip())
    except Exception as _e:
        print(f"convention check skipped: {_e}")

print("Done.")

