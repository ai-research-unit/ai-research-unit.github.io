#!/usr/bin/env python3
# DO NOT MODIFY THIS FILE WITHOUT EXPLICIT USER APPROVAL.
# The build files -- build.py, build_diff.py, build_external.py, sync_index.py --
# are the only route from the .md sources to the deploy folder. A change here
# rewrites pages wholesale and can delete deployed files, so it is made only on
# the user's explicit request, never as a side effect of another task.
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
    # Before the state is read and stamped: a copy written here is this build's
    # input, not the next build's change.
    build.sync_index()
    started = datetime.now()

    since = build.read_state()
    if since is None:
        print("build_state missing or unreadable — running a full build instead.")
        build.main()
        return

    print(f"Last build started {since.isoformat(timespec='seconds')}")

    # The url list is regenerated every run, before the sitemaps that follow it:
    # a new article must never be missing from it either.
    build.write_ai_physics_overview()
    build.collect_articles()
    if not any(c["articles"] for c in build.COLLECTIONS):
        print("No md files found in articles_maths/ or articles_physics/. Add some and re-run.")
        return

    build.ensure_dirs()
    build.copy_static(since)

    nav = build.nav_pool()

    article_tpl = build.newer_than(build.SRC / "article_template.html", since)
    index_tpl = build.newer_than(build.SRC / "index_template.html", since)
    # The two build scripts are dependencies too: a page list entry, a template
    # placeholder or a CSS scope changed in them leaves no newer .md behind, so
    # without this test the deployed pages keep the old markup and stay stale
    # while the build reports success.
    code_changed = (build.newer_than(build.SRC / "build.py", since)
                    or build.newer_than(build.SRC / "build_diff.py", since))
    if article_tpl:
        print("article_template.html changed — every article page is rebuilt.")
    if index_tpl:
        print("index_template.html changed — every root page is rebuilt.")
    if code_changed:
        print("build.py or build_diff.py changed — every root page and article page is rebuilt.")

    rebuilt = 0

    for md_name, out_name, is_menu in build.ROOT_PAGES:
        # A page whose deployed file is missing is built whatever its date says:
        # a rename keeps the old mtime and the target was never written.
        if (index_tpl or code_changed or build.newer_than(build.SRC / md_name, since)
                or not (build.DEPLOY / out_name).exists()):
            build.build_root_page(build.SRC / md_name, out_name, nav, is_menu)
            rebuilt += 1

    for coll in build.ordered_collections():
        if not coll["articles"]:
            if not coll.get("optional"):
                print(f"Warning: no md files in {coll['src'].name}/")
            continue
        for f in coll["articles"]:
            target = coll["deploy"] / f.relative_to(coll["src"]).with_suffix(".html")
            if article_tpl or code_changed or build.newer_than(f, since) or not target.exists():
                build.build_article(coll, f, nav)
                rebuilt += 1

    if rebuilt == 0:
        print("No source changed — nothing to redeploy.")

    build.prune_orphans()
    build.prune_legacy()
    # Sitemaps are rewritten every run: the URL set is cheap to recompute and a
    # new article must never be missing from them.
    build.write_sitemaps()
    build.run_convention_check()
    build.write_state(started)

    print("Done.")


if __name__ == "__main__":
    main()
