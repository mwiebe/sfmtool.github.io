# Copyright The SfM Tool Authors
# SPDX-License-Identifier: Apache-2.0
"""Write a redirect page under ``sfmtool/`` for every page of the built site.

The site used to be the project Pages site of the ``sfmtool/sfmtool``
repository, served at ``https://sfmtool.github.io/sfmtool/``. It is now the
organization site, served at the root. GitHub Pages serves a path under
``/sfmtool/`` from this site once the ``sfmtool`` repository has Pages turned
off, so a page at ``sfmtool/<path>`` that redirects to ``/<path>`` keeps every
old link working.

Usage: ``python scripts/add_legacy_redirects.py site``
"""

import html
import sys
from pathlib import Path

LEGACY_PREFIX = "sfmtool"

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Moved</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<meta name="robots" content="noindex">
<script>location.replace({url_js} + location.search + location.hash);</script>
</head>
<body><p>This page has moved to <a href="{url}">{url}</a>.</p></body>
</html>
"""


def main() -> None:
    site = Path(sys.argv[1])
    legacy = site / LEGACY_PREFIX
    if legacy.exists():
        sys.exit(f"{legacy} already exists; a page of the site uses the legacy prefix")
    pages = list(site.rglob("index.html"))
    for page in pages:
        rel = page.parent.relative_to(site).as_posix()
        url = "/" if rel == "." else f"/{rel}/"
        out = legacy / page.relative_to(site)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(
            TEMPLATE.format(url=html.escape(url), url_js=repr(url)), encoding="utf-8"
        )
    print(f"Wrote {len(pages)} redirect pages under {legacy}")


if __name__ == "__main__":
    main()
