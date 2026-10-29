# Working in the sfmtool.github.io Repository

The documentation site for [SfM Tool](https://github.com/sfmtool/sfmtool),
deployed to <https://sfmtool.github.io/>. Pages are Markdown under `docs/`, the
navigation is in `zensical.toml`, and the build runs through Pixi:
`pixi run docs-build` and `pixi run docs-serve`.

- The code, its specs and `AGENTS.md` live in the `sfmtool` repository, which
  is usually checked out beside this one. Check every command, menu name,
  panel name and output block a page shows against that code or a real run,
  not against memory.
- Screenshots live beside the page that uses them, in an `images/` directory.
  Take them on copies of the `sfmtool` repository's `test-data`, never on the
  originals, and crop out local paths and usernames.
- `scripts/add_legacy_redirects.py` keeps the old
  `https://sfmtool.github.io/sfmtool/...` links working. No page may live
  under `docs/sfmtool/`; the script fails the build if one does.
- Write in plain language: no metaphors or idioms where a literal phrase says
  the same thing. Name the thing and say what it does.
- Pull requests are squash-merged, and every commit needs a DCO sign-off
  (`git commit -s`).
