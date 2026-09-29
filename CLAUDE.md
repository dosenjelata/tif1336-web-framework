# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Jekyll static site (theme: `minima`) publishing course materials for TIF1336 Pemrograman Web Frameworks (Django backend, Next.js frontend). It is deployed to GitHub Pages at `https://dosenjelata.github.io/tif1336-web-framework`. There is no application code here, only tutorial posts written in Indonesian.

## Commands

```bash
bundle install                     # install Jekyll + plugins
bundle exec jekyll serve           # local preview at http://localhost:4000/tif1336-web-framework/
bundle exec jekyll serve --future  # also render posts whose front-matter date is in the future
bundle exec jekyll build           # build into _site/ (a successful build is the only "test")
```

## Content structure

- `_posts/YYYY-MM-DD-<slug>.md`: the tutorials. Most are a sequential "Django untuk pemula - Part N" series that builds one blog project step by step, and each part assumes the code from the previous parts. Keep project names, file paths and model/view names consistent with earlier parts when adding or editing one. Part 1 sets the project up with uv, so later parts write commands as `uv run python manage.py ...` and don't activate a venv or use `pip`. Part 0 (file `2025-09-08-membuat-virtualenvirontment.md`, kept under its old name and categories so its URL doesn't change) teaches `venv` + `pip` in a throwaway `latihan_venv` folder and ends by pointing to uv in Part 1.
- Front matter pattern: `layout: post`, `title`, `date: YYYY-MM-DD HH:MM:SS +0700`, `categories: [...]`, `tags: [...]`. The front-matter `date` (not the filename) controls ordering and whether the post appears. A future date hides the post unless you build with `--future`. Keep the front-matter date matching the filename date.
- Permalinks are `/:categories/:year/:month/:day/:title/`, so changing `categories` changes a post's URL.
- `source/part-NN/website_django/` holds the finished code of Part NN, which is also the starting point of Part NN+1. The folders contain code, `pyproject.toml` and `uv.lock`, but no `db.sqlite3` or `.venv`. Each post starts with a "Kode sumber" line linking its start and finish folders on GitHub. When a post's code changes, update that part's folder and every later folder the change carries into. `source/` is excluded from the Jekyll site.
- Screenshots live in `assets/images/`, named by part (`08-home.png`, `09-contact.png`, etc.).

## Liquid gotchas

- Django template syntax (`{% ... %}`, `{{ ... }}`) conflicts with Liquid. Wrap any post section with Django template code in `{% raw %}` ... `{% endraw %}`. Otherwise the Jekyll build fails or silently mangles the code.
- Image links must use Liquid so the `baseurl` is applied, e.g. `![Alt]({{ '/assets/images/09-about.png' | relative_url }})`. Put them **outside** the `{% raw %}` block; in existing posts, `{% endraw %}` sits just before the screenshot section at the end.

- Links between posts are written as `[text]({{ site.baseurl }}{% post_url 2025-09-08-<slug> %})`. On Jekyll 3, `post_url` doesn't add the baseurl, so the prefix is needed on the live site. A local Jekyll 4 build shows these links with the baseurl doubled, and that's expected.

## Config notes

- **Production is not the local build.** GitHub Pages builds straight from `main` with the `github-pages` gem (Jekyll 3.10), not the Jekyll 4.4 in the `Gemfile`. A passing local build doesn't guarantee a passing deploy. Pages also runs `jekyll-optional-front-matter`, which renders any root `.md` file even without front matter. Non-site Markdown files must therefore be listed under `exclude:` in `_config.yml`, as `CLAUDE.md` is.

- `_config.yml` sets `baseurl: "/tif1336-web-framework"`, so internal links need `relative_url`.
- `_config.yml` lists `jekyll-seo-tag` under plugins. The `Gemfile` doesn't declare it, but it comes in as a dependency of `minima`.
