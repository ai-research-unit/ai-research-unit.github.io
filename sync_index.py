#!/usr/bin/env python3
# DO NOT MODIFY THIS FILE WITHOUT EXPLICIT USER APPROVAL.
# The build files -- build.py, build_diff.py, build_external.py, sync_index.py --
# are the only route from the .md sources to the deploy folder. A change here
# rewrites pages wholesale and can delete deployed files, so it is made only on
# the user's explicit request, never as a side effect of another task.
"""Regenerate index.md from the introduction article.

`index.md` is generated, not written: it is a copy of
`articles_physics/introduction-to-the-biquaternion-universe.md`, with only the
first heading replaced by the landing-page title (`build.INDEX_TITLE`), so the
landing page is the introduction and the two can never drift.

Both build scripts call the same function (build.sync_index) at the top of
main(), so a normal `python3 build.py` or `python3 build_diff.py` regenerates the
page before reading it. This file exists to run the copy on its own:

    python3 sync_index.py            copy if the article changed
    python3 sync_index.py --check    exit 1 if index.md is out of date, no write
"""
import sys

import build


def main():
    if "--check" in sys.argv[1:]:
        same = (build.INDEX_TARGET.exists()
                and build.INDEX_TARGET.read_text(encoding="utf-8")
                == build.index_text(build.INDEX_SOURCE.read_text(encoding="utf-8")))
        print("index.md up to date" if same else "index.md is out of date — run sync_index.py")
        return 0 if same else 1
    build.sync_index()
    return 0


if __name__ == "__main__":
    sys.exit(main())
