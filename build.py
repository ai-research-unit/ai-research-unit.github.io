#!/usr/bin/env python3
import re
import shutil
import subprocess
import sys
import markdown
from datetime import datetime
from html import escape, unescape
from pathlib import Path
from urllib.parse import quote

SRC        = Path("/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit")
DEPLOY     = Path("/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit-deploy")

# Old URLs kept alive after a rename: (deployed page, alias that copies it).
# The pruner spares the aliases, and no sitemap lists them.
LEGACY_COPIES = [
    ("articles_physics/cosmology-in-the-biquaternion-framework-the-carried-flrw-metric-and-the-missing-source.html",
     "articles_physics/cosmology-under-the-biquaternion-framework-a-research-agenda.html"),
    ("articles_physics/electroweak-theory-in-the-biquaternion-framework-the-u2-reach-and-the-chiral-wall.html",
     "articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html"),
    ("articles_physics/quantum-chromodynamics-in-the-biquaternion-framework-the-dimension-ceiling-and-the-colour-wall.html",
     "articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html"),
    ("articles_physics/the-standard-model-in-the-biquaternion-framework-the-u2-ceiling-and-the-four-unbuilt-sectors.html",
     "articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html"),
    ("articles_physics/quantum-gravity-in-the-biquaternion-framework-the-two-sided-obstruction-and-the-modular-temperature.html",
     "articles_physics/quantum-gravity-under-the-biquaternion-framework-a-research-agenda.html"),
    ("articles_physics/the-einstein-field-equations-in-the-biquaternion-framework-the-linearised-dictionary-and-the-non-linear-gap.html",
     "articles_physics/the-einstein-field-equations-under-the-biquaternion-framework-a-research-agenda.html"),
    ("articles_physics/introduction-to-the-lorentz-group-in-biquaternionic-form.html",
     "articles_physics/ai-describes-the-lorentz-group.html"),
    ("articles_physics/introduction-to-the-lorentz-group-in-biquaternionic-form.html",
     "articles_physics/biquaternions-and-the-lorentz-group.html"),
    ("articles_internal/internal-summary-of-the-biquaternion-particle-physics.html",
     "articles_internal/internal-summary-of-the-biquaternion-particle-physics-and-gauge-fields.html"),
    ("articles_physics/the-lagrangian-and-quantum-chromodynamics-the-triplet-the-octet-and-the-feynman-rules.html",
     "articles_physics/quantum-chromodynamics-and-the-lagrangian-the-triplet-the-octet-and-the-feynman-rules.html"),
]

# One date for the whole site: the moment the last build started. build2.py
# reads it to decide which pages to rebuild. It lives in the source folder,
# never in the deploy folder.
STATE_FILE = SRC / "build_state"

TEMPLATE       = (SRC / "article_template.html").read_text()
INDEX_TEMPLATE = (SRC / "index_template.html").read_text()

# The corpus is split into two independent collections, each with its own
# source folder, its own deploy folder, and its own menu page. A slug belongs
# to exactly one collection — the menus are disjoint — so an article's file
# location is determined by which menu links it.
COLLECTIONS = [
    {"name": "maths",   "src": SRC / "articles_maths",   "deploy": DEPLOY / "articles_maths"},
    {"name": "physics", "src": SRC / "articles_physics", "deploy": DEPLOY / "articles_physics"},
    # Reference area. Drafts here build like the public collections — each md
    # gets its own page, subfolders mirror into the deploy tree — but only the
    # entries listed in maths.md are reachable from the menus. Marked optional so
    # an empty folder is not a warning, and recursive so articles_internal/matrix/
    # can hold a nested archive.
    {"name": "internal", "src": SRC / "articles_internal", "deploy": DEPLOY / "articles_internal",
     "optional": True, "recursive": True},
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

def build_nav_article(articles, current_stem=None, depth=1):
    root = "../" * depth
    items = []
    items.append(f'<li><a href="{root}maths.html">Maths</a></li>')
    items.append(f'<li><a href="{root}physics.html">Physics</a></li>')
    items.append(f'<li><a href="{root}disclaimer.html">Disclaimer</a></li>')
    items.append(f'<li><a href="{root}contact.html">Contact</a></li>')
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

def collect_articles():
    for coll in COLLECTIONS:
        pattern = "**/*.md" if coll.get("recursive") else "*.md"
        coll["articles"] = sorted(coll["src"].glob(pattern), key=article_sort_key)


def nav_pool():
    # The {nav} placeholder renders the same four links on every page regardless
    # of the current article, so the pool it is drawn from does not matter.
    return [p for coll in COLLECTIONS for p in coll["articles"]
            if "zexample" not in p.stem.lower()]


def ensure_dirs():
    DEPLOY.mkdir(parents=True, exist_ok=True)
    for coll in COLLECTIONS:
        coll["deploy"].mkdir(parents=True, exist_ok=True)


INDEX_SOURCE = SRC / "articles_physics" / "introduction-to-the-biquaternion-universe.md"
INDEX_TARGET = SRC / "index.md"

# The landing page is the introduction, but it carries its own H1: the article
# keeps its catalog title, the front page names the claim.
INDEX_TITLE = "AI unifies quantum physics and relativity"

_INDEX_H1 = re.compile(r"^#\s*__.+?__\s*$")


def index_text(source):
    """Copy the introduction, keeping only its H1 replaced by INDEX_TITLE."""
    lines = source.splitlines(keepends=True)
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if _INDEX_H1.match(s):
            lines[i] = f"# __{INDEX_TITLE}__\n"
        break
    return "".join(lines)


def sync_index():
    """Rewrite index.md as a copy of the introduction article.

    The landing page is the introduction, so it is generated and not edited by
    hand: editing index.md is undone by the next build. Only the first heading
    differs (see INDEX_TITLE). The write is skipped when the content already
    matches, so an unchanged article leaves index.md's mtime alone and the
    incremental build in build2.py stays incremental.
    """
    if not INDEX_SOURCE.exists():
        print(f"Warning: {INDEX_SOURCE.relative_to(SRC)} not found — index.md kept as it is.")
        return False
    source = index_text(INDEX_SOURCE.read_text(encoding="utf-8"))
    if INDEX_TARGET.exists() and INDEX_TARGET.read_text(encoding="utf-8") == source:
        return False
    INDEX_TARGET.write_text(source, encoding="utf-8")
    print("Synced: index.md ← articles_physics/introduction-to-the-biquaternion-universe.md")
    return True


def newer_than(path, since):
    """True when `path` exists and was modified after `since` (a datetime)."""
    return path.exists() and path.stat().st_mtime > since.timestamp()


def write_state(moment):
    """Record when this build started, for build2.py.

    The start, not the end: a source edited while the build runs then carries an
    mtime past the record, so the next incremental build still sees it.
    """
    STATE_FILE.write_text(moment.isoformat(timespec="seconds") + "\n")


def read_state():
    """The moment recorded by the last build, or None when unusable."""
    try:
        text = STATE_FILE.read_text().strip()
    except OSError:
        return None
    if not text:
        return None
    try:
        return datetime.fromisoformat(text)
    except ValueError:
        return None


def copy_static(since=None):
    """Mirror the static files into the deploy folder.

    A full build (since is None) replaces assets/ outright, which also drops
    files deleted at the source. An incremental build copies only the files
    whose source is newer than `since`.
    """
    src_assets = SRC / "assets"
    deploy_assets = DEPLOY / "assets"
    if src_assets.exists():
        if since is None:
            if deploy_assets.exists():
                shutil.rmtree(deploy_assets)
            shutil.copytree(src_assets, deploy_assets)
            print("Copied assets/")
        else:
            for f in sorted(src_assets.rglob("*")):
                if not f.is_file():
                    continue
                out = deploy_assets / f.relative_to(src_assets)
                if newer_than(f, since) or not out.exists():
                    out.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(f, out)
                    print(f"Copied assets/{f.relative_to(src_assets)}")

    for name in ("robots.txt", ".nojekyll", ".gitlab-ci.yml"):
        src = SRC / name
        if not src.exists():
            continue
        if since is None or newer_than(src, since) or not (DEPLOY / name).exists():
            shutil.copy(src, DEPLOY / name)
            print(f"Copied {name}")


def menu_order(menu_md, folder):
    """Slugs in the order their links appear in a menu file.

    The menus carry the editorial reading order — sections, then the articles
    that belong to each — which is the order a reader follows. It is not the
    alphabetical order `collect_articles()` uses for building.
    """
    path = SRC / menu_md
    if not path.exists():
        return {}
    order = {}
    for slug in re.findall(rf'href="{folder}/([^"]+)\.html"', path.read_text()):
        order.setdefault(slug, len(order))
    return order


def sitemap_urls():
    """Every public page of the site, as (deploy path, source file) pairs.

    The order is editorial, not alphabetical: the three entry pages, then the
    physics corpus, then the maths corpus, then the two menu pages that index
    them. Inside a collection the order is the menu's. The internal collection
    stays out: no menu links it, and it holds drafts.

    An article that no menu links goes last within its collection, by name, so
    it is still listed.
    """
    root = {out: (SRC / md) for md, out, _ in ROOT_PAGES}
    head = ["index.html", "disclaimer.html", "contact.html"]
    urls = [(out, root[out]) for out in head if out in root]
    for coll in ordered_collections():
        if coll["name"] == "internal":
            continue
        order = menu_order(f"{coll['name']}.md", coll["src"].name)
        last = len(order)
        files = sorted(coll["articles"], key=lambda f: (order.get(f.stem, last), f.stem))
        for f in files:
            rel = f.relative_to(coll["src"]).with_suffix(".html").as_posix()
            urls.append((f"{coll['src'].name}/{rel}", f))
    urls += [(out, src) for out, src in root.items() if out not in head]
    return urls


def write_sitemaps():
    """Write one sitemap per mirror into the source folder, then mirror them.

    A sitemap is only valid for the host that serves it, so the three mirrors
    cannot share one file. The source copies are the reference; the deploy
    folder gets a copy of each so the hosts can serve them.
    """
    urls = sitemap_urls()
    for name, host in SITEMAPS:
        lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                 '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
        for path, src in urls:
            lastmod = datetime.fromtimestamp(src.stat().st_mtime).strftime("%Y-%m-%d")
            lines.append("  <url>")
            lines.append(f"    <loc>{host}/{quote(path)}</loc>")
            lines.append(f"    <lastmod>{lastmod}</lastmod>")
            lines.append("  </url>")
        lines.append("</urlset>")
        out = SRC / name
        out.write_text("\n".join(lines) + "\n", encoding="utf-8")
        if DEPLOY.is_dir():
            shutil.copy(out, DEPLOY / name)
        print(f"Wrote {name} ({len(urls)} urls)")


def menu_sections(menu_md, folder):
    """Sections of a menu file with the slugs each one links, in menu order.

    `menu_order()` flattens the menu; this keeps its `##` boundaries, which are
    the categories the AI overview reproduces.
    """
    path = SRC / menu_md
    if not path.exists():
        return []
    sections = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("## "):
            sections.append((line[3:].strip(), []))
        elif sections:
            for slug in re.findall(rf'href="{folder}/([^"]+)\.html"', line):
                if slug not in sections[-1][1]:
                    sections[-1][1].append(slug)
    return sections


def write_ai_physics_overview():
    """Write articles_internal/ai-physics-overview.md from the physics menu.

    Every physics article as one complete https url under its menu category, on
    its own line. The urls are left bare, not wrapped in angle brackets, so
    nothing on the page is a link: the text is the address, to be copied or
    fetched, not clicked. Two trailing spaces per line are the markdown line
    break that keeps one url per line in the rendered page.

    It sits in the internal collection, so no menu links it and no sitemap lists
    it: it is a stand-in list for a reader given the corpus, not a page the site
    advertises.

    Left untouched when its content would not change, so neither the page nor
    its mtime moves on a build that changes nothing.
    """
    host = SITEMAPS[0][1]
    blocks, n = [], 0
    for title, slugs in menu_sections("physics.md", "articles_physics"):
        urls = [f"{host}/articles_physics/{slug}.html  " for slug in slugs]
        if not urls:
            continue
        blocks.append(f"## {title}\n\n" + "\n".join(urls))
        n += len(urls)
    head = ("# __AI Physics Overview__\n\n"
            "Every physics article of the corpus, as one complete url under its "
            "menu category, one url per line.  \n")
    text = head + "\n" + "\n\n".join(blocks) + "\n"
    out = SRC / "articles_internal" / "ai-physics-overview.md"
    if out.exists() and out.read_text(encoding="utf-8") == text:
        print(f"ai-physics-overview.md unchanged ({n} urls)")
        return
    out.write_text(text, encoding="utf-8")
    print(f"Wrote ai-physics-overview.md ({n} urls)")


def plain_summary(html_text, limit=155, min_chars=60):
    """First substantial paragraph of a rendered body, as plain text.

    Inline math is dropped: a crawler shows the description verbatim, raw TeX
    included, so the formulas are removed rather than escaped.
    """
    for chunk in re.findall(r"<p>(.*?)</p>", html_text, re.DOTALL):
        text = re.sub(r"\$\$.*?\$\$|\$[^$\n]*?\$", " ", chunk, flags=re.DOTALL)
        text = re.sub(r"<[^>]+>", "", text)
        text = re.sub(r"\s+", " ", unescape(text)).strip()
        text = re.sub(r"\s+([.,;:])", r"\1", text)
        if len(text) < min_chars:
            continue
        if len(text) > limit:
            text = text[:limit].rsplit(" ", 1)[0].rstrip(" ,;:") + "…"
        return text
    return ""


def menu_summary(body_html, title):
    """Description for a menu page, which has links but no prose paragraph.

    Only the two public collections are counted: the menu also links a few
    internal drafts, and those are not part of what the page announces.
    """
    n = len(set(re.findall(r'href="articles_(?:maths|physics)/[^"]*\.html"', body_html)))
    if n:
        return f"{title} — index of {n} articles in the Biquaternion Universe corpus."
    return title


def build_root_page(md_path, out_name, articles, is_menu=False):
    if md_path.exists():
        raw = md_path.read_text()
        meta, body_md = parse_frontmatter(raw)

        body_html = md_to_html(body_md)
        title = meta.get("title") or heading_title(body_md) or label_from_stem(md_path.stem)
        description = (menu_summary(body_html, title) if is_menu
                       else plain_summary(body_html) or menu_summary(body_html, title))

        html = (INDEX_TEMPLATE
            .replace("{title}",       escape(f"{title} — Biquaternion Universe"))
            .replace("{description}", escape(description))
            .replace("{nav}",         build_nav_index(articles))
            .replace("{body_attr}",   ' class="menu"' if is_menu else "")
            .replace("{index_items}", body_html)
        )
        (DEPLOY / out_name).write_text(html)
        print(f"Built: {out_name}")
    else:
        print(f"Warning: {md_path.name} not found at {md_path}")


def build_article(coll, f, articles):
    raw = f.read_text()
    meta, body_md = parse_frontmatter(raw)
    # parse_frontmatter always defines "title" (default ""), so .get()'s
    # default never fires — fall back explicitly.
    title = meta.get("title") or heading_title(body_md) or label_from_stem(f.stem)

    body_html = md_to_html(body_md)

    rel = f.relative_to(coll["src"])
    # The collection folder is itself one level below the site root, so the
    # prefix counts every part of `rel`, not only its parent folders.
    depth = len(rel.parts)
    root = "../" * depth
    out = coll["deploy"] / rel.with_suffix(".html")
    out.parent.mkdir(parents=True, exist_ok=True)

    html = (TEMPLATE
        .replace("{title}",      escape(title))
        .replace("{description}", escape(plain_summary(body_html)))
        .replace("{coordinate}", meta.get("coordinate", ""))
        .replace("{nav}",        build_nav_article(articles, current_stem=f.stem, depth=depth))
        .replace("{root}",       root)
        .replace("{body}",       body_html)
    )
    out.write_text(html)
    print(f"Built: {coll['src'].name}/{rel.with_suffix('.html')}")


# Root pages first: the menus and the landing page are the site's entry points,
# so they are written before the article corpus. The third field marks the two
# menu pages, whose body carries the `menu` class the banded headings need;
# `index.md` is a prose article, not a list of entries, and keeps article styling.
ROOT_PAGES = [
    ("index.md",      "index.html",      False),
    ("maths.md",      "maths.html",      True),
    ("physics.md",    "physics.html",    True),
    ("disclaimer.md", "disclaimer.html", False),
    ("contact.md",    "contact.html",    False),
]

# The three public mirrors. Each gets its own sitemap file, named so the file's
# host is obvious in the deploy folder.
SITEMAPS = [
    ("sitemap_github.xml",   "https://ai-research-unit.github.io"),
    ("sitemap_gitlab.xml",   "https://a-i-research-unit.gitlab.io"),
    ("sitemap_codeberg.xml", "https://ai-research-unit.codeberg.page"),
]


def ordered_collections():
    # Physics before maths. build_order only controls build sequence; COLLECTIONS
    # keeps its own order because the nav links are derived from it.
    build_order = ["physics", "maths", "internal"]
    return sorted(COLLECTIONS, key=lambda c: build_order.index(c["name"]))


def prune_orphans():
    # ── prune orphaned article HTML ───────────────────────────────────────
    # We only ever write files into the deploy dir, never delete, so a renamed
    # or removed source md leaves its old .html behind — still served, still
    # indexable, and silently diverging from the current article. Drop any
    # deployed article page that no longer has a matching source. This also
    # removes pages left in a collection by a file that moved to the other one.
    # The legacy aliases are the exception: they have no source by design.
    keep = {(DEPLOY / alias).resolve() for _, alias in LEGACY_COPIES}
    for coll in COLLECTIONS:
        built = {str(f.relative_to(coll["src"]).with_suffix(".html")) for f in coll["articles"]}
        for stale in coll["deploy"].rglob("*.html"):
            rel = str(stale.relative_to(coll["deploy"]))
            if rel not in built and stale.resolve() not in keep:
                stale.unlink()
                print(f"Removed orphan: {coll['src'].name}/{rel}")
    # ──────────────────────────────────────────────────────────────────────


def prune_legacy():
    # ── prune the pre-split deploy directory ──────────────────────────────
    # Before the split every page was written to <deploy>/articles/. Those pages
    # are now superseded by the two per-collection directories, and leaving them
    # would publish each article twice at the old URL.
    legacy_art = DEPLOY / "articles"
    if legacy_art.is_dir():
        shutil.rmtree(legacy_art)
        print("Removed legacy deploy directory: articles/")
    # ──────────────────────────────────────────────────────────────────────


def copy_legacy_pages():
    # ── serve the pre-rename URL ──────────────────────────────────────────
    # A bookmark or an outside link to the old name must not 404. The alias is a
    # byte copy, so it follows every later rebuild of the article with no second
    # template pass. It runs after prune_orphans(), which would otherwise delete
    # a deployed page that has no source .md behind it.
    for src_rel, alias_rel in LEGACY_COPIES:
        src = DEPLOY / src_rel
        if not src.exists():
            continue
        data = src.read_bytes()
        alias = DEPLOY / alias_rel
        if alias.exists() and alias.read_bytes() == data:
            continue
        alias.write_bytes(data)
        print(f"Alias written: {alias_rel}")
    # ──────────────────────────────────────────────────────────────────────


def run_convention_check():
    # ── Convention check (non-fatal) ──────────────────────────────────────
    # Reports shared symbols given conflicting definitions across articles — the
    # class of defect the ordering rules cannot see. Never fails the build; the
    # report is advisory.
    conv = SRC / "_reserve" / "convention_check.py"
    if not conv.exists():
        return
    try:
        r = subprocess.run([sys.executable, str(conv)], capture_output=True, text=True)
        print(r.stdout.strip() or r.stderr.strip())
    except Exception as e:
        print(f"convention check skipped: {e}")
    # ──────────────────────────────────────────────────────────────────────


def main():
    # Before the state is stamped: the copy it may write must not look newer
    # than this build, or the next incremental run rebuilds index.html for nothing.
    sync_index()
    started = datetime.now()

    write_ai_physics_overview()
    collect_articles()
    if not any(c["articles"] for c in COLLECTIONS):
        print("No md files found in articles_maths/ or articles_physics/. Add some and re-run.")
        return

    ensure_dirs()
    copy_static()

    articles = nav_pool()

    for md_name, out_name, is_menu in ROOT_PAGES:
        build_root_page(SRC / md_name, out_name, articles, is_menu)

    for coll in ordered_collections():
        if not coll["articles"]:
            if not coll.get("optional"):
                print(f"Warning: no md files in {coll['src'].name}/")
            continue
        for f in coll["articles"]:
            build_article(coll, f, articles)

    prune_orphans()
    prune_legacy()
    write_sitemaps()
    run_convention_check()
    copy_legacy_pages()
    write_state(started)

    print("Done.")


if __name__ == "__main__":
    main()

