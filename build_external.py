#!/usr/bin/env python3
# DO NOT MODIFY THIS FILE WITHOUT EXPLICIT USER APPROVAL.
# The build files -- build.py, build_diff.py, build_external.py, sync_index.py --
# are the only route from the .md sources to the deploy folder. A change here
# rewrites pages wholesale and can delete deployed files, so it is made only on
# the user's explicit request, never as a side effect of another task.
"""Build only the external conversions: articles_external/**/*.md -> .html.

Scope is one folder. Unlike build.py and build_diff.py, this script writes
nothing outside <deploy>/articles_external/:

    no root page (index, maths.html, physics.html, disclaimer, contact),
    no other collection (articles_maths, articles_physics, articles_internal),
    no assets/, no sitemap, no build_state, no legacy alias, no convention check.

That is deliberate. The conversions arrive in bulk from outside the corpus, so a
conversion pass must not republish, restamp or prune the site already deployed.
No menu links these pages either: they are reachable by url only, like the
internal collection.

    python3 build_external.py                  every conversion
    python3 build_external.py Pati-Salam       one source subfolder
    python3 build_external.py Pati-Salam/Addazi*.md   matching files
"""
import sys
from pathlib import Path

import build

FOLDER = "articles_external"

COLLECTION = {
    "name": FOLDER,
    "src": build.SRC / FOLDER,
    "deploy": build.DEPLOY / FOLDER,
    "optional": True,
    "recursive": True,
}


def sources(args):
    """Markdown files named by the command line, or every file when it is empty."""
    if not COLLECTION["src"].is_dir():
        return []

    if not args:
        return sorted(COLLECTION["src"].rglob("*.md"))

    found = []
    for arg in args:
        path = Path(arg)
        target = path if path.is_absolute() else COLLECTION["src"] / path
        if target.is_file():
            found.append(target)
        elif target.is_dir():
            found.extend(target.rglob("*.md"))
        else:
            matches = sorted(COLLECTION["src"].rglob(arg))
            if not matches:
                print(f"Warning: {arg} matches nothing — skipped.")
            found.extend(m for m in matches if m.suffix == ".md")
    return sorted(set(found))


def prune():
    """Delete deployed pages whose source is gone, inside this folder alone.

    The test is the source file, not this run's list: a build restricted to one
    subfolder must not delete the pages of the others.
    """
    if not COLLECTION["deploy"].is_dir():
        return
    for page in COLLECTION["deploy"].rglob("*.html"):
        rel = page.relative_to(COLLECTION["deploy"])
        if not (COLLECTION["src"] / rel).with_suffix(".md").exists():
            page.unlink()
            print(f"Removed orphan: {FOLDER}/{rel}")


def main():
    if not COLLECTION["src"].is_dir():
        print(f"No {FOLDER}/ folder — nothing to build.")
        return

    files = sources(sys.argv[1:])
    if not files:
        print(f"No md files in {FOLDER}/. Nothing to build.")
        return

    COLLECTION["deploy"].mkdir(parents=True, exist_ok=True)

    # The pdf->conversion pairs live in subfolders, so a page sits two levels
    # below the site root; build_article derives the ../ prefix from the path.
    built = 0
    for f in files:
        build.build_article(COLLECTION, f, [])
        built += 1

    prune()
    print(f"Done: {built} conversion{'s' if built != 1 else ''} built.")


if __name__ == "__main__":
    main()
