# SfM Tool documentation

The source of the SfM Tool documentation site,
[sfmtool.github.io](https://sfmtool.github.io/). The tool itself lives in
[sfmtool/sfmtool](https://github.com/sfmtool/sfmtool).

The pages are Markdown under `docs/`, built with
[Zensical](https://zensical.org/) through [Pixi](https://pixi.sh):

```bash
pixi run docs-serve   # Live preview at http://localhost:8000
pixi run docs-build   # Build the site into site/
```

Every push to `main` builds the site and deploys it to GitHub Pages.

## Why a separate repository

The documentation's screenshots are regenerated as SfM Explorer changes, and
each regeneration adds binary files to the history. Keeping them here keeps the
`sfmtool` repository small. Naming this repository `sfmtool.github.io` makes it
the organization's Pages site, served at the root URL.

The site used to be served at `https://sfmtool.github.io/sfmtool/`.
`scripts/add_legacy_redirects.py` writes a redirect page under `sfmtool/` for
every page of the built site, so old links still reach the page they named.

## License

Apache-2.0; see [LICENSE](LICENSE).
