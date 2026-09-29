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

- `_posts/YYYY-MM-DD-<slug>.md`: the tutorials. Most are a sequential "Django untuk pemula - Part N" series that builds one blog project step by step, and each part assumes the code from the previous parts. Keep project names, file paths and model/view names consistent with earlier parts when adding or editing one. Part 1 sets the project up with uv, so later parts write commands as `uv run python manage.py ...` and don't activate a venv or use `pip`. The standalone `membuat-virtualenvirontment` post still teaches `venv` and `pip`, and Part 1 links to it as background.
- Front matter pattern: `layout: post`, `title`, `date: YYYY-MM-DD HH:MM:SS +0700`, `categories: [...]`, `tags: [...]`. The front-matter `date` (not the filename) controls ordering and whether the post appears. A future date hides the post unless you build with `--future`. Keep the front-matter date matching the filename date.
- Permalinks are `/:categories/:year/:month/:day/:title/`, so changing `categories` changes a post's URL.
- Screenshots live in `assets/images/`, named by part (`08-home.png`, `09-contact.png`, etc.).

## Liquid gotchas

- Django template syntax (`{% ... %}`, `{{ ... }}`) conflicts with Liquid. Wrap any post section with Django template code in `{% raw %}` ... `{% endraw %}`. Otherwise the Jekyll build fails or silently mangles the code.
- Image links must use Liquid so the `baseurl` is applied, e.g. `![Alt]({{ '/assets/images/09-about.png' | relative_url }})`. Put them **outside** the `{% raw %}` block; in existing posts, `{% endraw %}` sits just before the screenshot section at the end.

## Config notes

- `_config.yml` sets `baseurl: "/tif1336-web-framework"`, so internal links need `relative_url`.
- `_config.yml` lists `jekyll-seo-tag` under plugins. The `Gemfile` doesn't declare it, but it comes in as a dependency of `minima`.
