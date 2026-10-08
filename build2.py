#!/usr/bin/env python3
"""Incremental build: redeploy only what changed since the last build.

build.py is the sweep. It rebuilds the whole site and, before it starts, stamps
the moment in `build_state`. This script reads that moment and rebuilds only the
pages that moved past it:

    an article page  when its own .md is newer, or when article_template.html is
    a root page      when its own .md is newer, or when index_template.html is
    assets/, robots.txt, .nojekyll, .gitlab-ci.yml   per file, when newer

Everything else is left alone in the deploy folder. The two prunes and the
convention check run every time regardless: they read the whole corpus by
nature, and a deletion never has a newer date to be spotted by.

The date is the one thing this design cannot see through: a file whose content
changed while its date was set back looks untouched and is skipped. Nothing else
here rewrites source dates, so that only happens if something outside the
project does it.

If `build_state` is missing or unreadable, this falls back to a full build.
"""
from datetime import datetime

import build


def main():
    started = datetime.now()

    since = build.read_state()
    if since is None:
        print("build_state missing or unreadable — running a full build instead.")
        build.main()
        return

    print(f"Last build started {since.isoformat(timespec='seconds')}")

    build.collect_articles()
    if not any(c["articles"] for c in build.COLLECTIONS):
        print("No md files found in articles_maths/ or articles_physics/. Add some and re-run.")
        return

    build.ensure_dirs()
    build.copy_static(since)

    nav = build.nav_pool()

    article_tpl = build.newer_than(build.SRC / "article_template.html", since)
    index_tpl = build.newer_than(build.SRC / "index_template.html", since)
    if article_tpl:
        print("article_template.html changed — every article page is rebuilt.")
    if index_tpl:
        print("index_template.html changed — every root page is rebuilt.")

    rebuilt = 0

    for md_name, out_name in build.ROOT_PAGES:
        if index_tpl or build.newer_than(build.SRC / md_name, since):
            build.build_root_page(build.SRC / md_name, out_name, nav)
            rebuilt += 1

    for coll in build.ordered_collections():
        if not coll["articles"]:
            if not coll.get("optional"):
                print(f"Warning: no md files in {coll['src'].name}/")
            continue
        for f in coll["articles"]:
            if article_tpl or build.newer_than(f, since):
                build.build_article(coll, f, nav)
                rebuilt += 1

    if rebuilt == 0:
        print("No source changed — nothing to redeploy.")

    build.prune_orphans()
    build.prune_legacy()
    build.run_convention_check()
    build.write_state(started)

    print("Done.")


if __name__ == "__main__":
    main()
