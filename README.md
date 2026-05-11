# harmony_next_dev_skill

A [Claude Code](https://claude.com/claude-code) **skill** that lets Claude develop HarmonyOS NEXT applications offline, with the full official Huawei docs bundled.

> **HarmonyOS NEXT** (a.k.a. HarmonyOS 5+) is Huawei's standalone consumer OS — no Android compatibility layer. Apps are written in **ArkTS** with the **ArkUI** declarative framework, built with **DevEco Studio** / **hvigor**, and distributed via AppGallery.
>
> This is *not* OpenHarmony — different OS, different SDK. The skill is scoped strictly to `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`.

## What's in the skill

- **`SKILL.md`** — triggering description + routing table that fires whenever the user mentions HarmonyOS, ArkTS, ArkUI, `.ets`, `module.json5`, UIAbility, DevEco, `@kit.*` imports, etc.
- **`references/00-quick-start.md` → `10-kits-catalog.md`** — 11 hand-written reference files that distill the most important areas (project structure, ArkTS language, ArkUI, abilities & lifecycle, services, data & network, cards, tooling, testing, kits).
- **`references/pages/`** — **all 5301 pages** from the official HarmonyOS application-dev guide, crawled from `developer.huawei.com`, cleaned (nav/footer stripped), and stored per-slug. Code blocks preserved.
- **`references/manifest.json`** — the full slug index (title + depth) so Claude can find a page by keyword without internet.
- **`scripts/`** — the crawler / cleaner Python scripts used to build the skill (kept for re-crawl when docs evolve).
- **`assets/`** — reserved for future asset files.

## Installation

The skill lives at `.claude/skills/harmonyos-app-dev/` in this repo. To activate it for a project:

```bash
# In your HarmonyOS project directory
mkdir -p .claude/skills
cp -r /path/to/this/repo/.claude/skills/harmonyos-app-dev .claude/skills/
```

Or to make it user-wide (available in every project):

```bash
mkdir -p ~/.claude/skills
cp -r .claude/skills/harmonyos-app-dev ~/.claude/skills/
```

Then in Claude Code, the skill auto-loads when the user mentions HarmonyOS topics, or can be invoked explicitly as `/harmonyos-app-dev`.

## How it works

When Claude sees a HarmonyOS-related prompt:

1. The skill's `description` triggers loading.
2. Claude reads `SKILL.md` for the routing table.
3. For the matching surface (UI, abilities, networking, …), Claude reads the curated reference file.
4. For deeper / edge-case lookups, Claude greps `references/pages/` directly — no internet needed.

## Re-crawl

The crawler is iframe-based and runs against the live SPA on `developer.huawei.com`. To refresh:

```bash
# Open https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide in Chrome
# Then in Claude Code with browser tools enabled:
python scripts/analyze_manifest.py     # rebuild manifest from current nav
python scripts/build_full_plan.py      # plan the crawl
# … then drive the iframe crawler from the browser tab
python scripts/clean_pages.py          # strip nav/footer from raw_docs/pages → raw_docs/clean
```

See `scripts/step.py` for the per-batch state machine.

## Source authority

Every page in `references/pages/` keeps its canonical URL in the header:

```
# <title>

Source: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/<slug>
Slug: <slug>
```

This skill does not blend in OpenHarmony docs, GitHub-mirror sources, or third-party blogs.

## License & attribution

The crawled documentation content is © Huawei Technologies — please respect their copyright and the terms at https://developer.huawei.com/consumer/cn/agreement/. This repo redistributes the docs as a derivative work for the purpose of feeding Claude offline. The skill files (SKILL.md, the 11 reference files, scripts) are mine and may be reused under any permissive license you'd like; open an issue if you need a specific license header.
