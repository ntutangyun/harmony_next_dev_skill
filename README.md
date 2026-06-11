# harmony_next_dev_skill

A [Claude Code](https://claude.com/claude-code) **skill** that lets Claude develop HarmonyOS NEXT applications offline, with the full official Huawei docs bundled.

> **HarmonyOS NEXT** (a.k.a. HarmonyOS 5+) is Huawei's standalone consumer OS — no Android compatibility layer. Apps are written in **ArkTS** with the **ArkUI** declarative framework, built with **DevEco Studio** / **hvigor**, and distributed via AppGallery.
>
> This is *not* OpenHarmony — different OS, different SDK. The skill is scoped strictly to `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`.

## What's in the skill

- **`SKILL.md`** — triggering description + routing table that fires whenever the user mentions HarmonyOS, ArkTS, ArkUI, `.ets`, `module.json5`, UIAbility, DevEco, `@kit.*` imports, etc.
- **`references/00-quick-start.md` → `11-xiaoyi-agent-dev.md`** — 12 hand-written reference files that distill the most important areas (project structure, ArkTS language, ArkUI, abilities & lifecycle, services, data & network, cards, tooling, testing, kits, Xiaoyi agent development).
- **`references/pages/`** — **all 5351 pages** from the official HarmonyOS application-dev guide (synced 2026-06-11), fetched from `developer.huawei.com`'s docs API, cleaned, and stored per-slug. Code blocks preserved. Plus 3 hand-distilled Xiaoyi agent pages (`service-agent-*.md`).
- **`references/manifest.json`** — the full slug index (title + depth) so Claude can find a page by keyword without internet.
- **`scripts/`** — the Python scripts that sync the bundled docs from Huawei's docs API (`update_docs.py`, `fetch_xiaoyi.py`, `convert.py`).

## Installation

This repo **is** the skill — `SKILL.md` + `references/` live at the repo root, so the repo can be dropped straight into a `.claude/skills/<name>/` slot (e.g. as a git submodule). To activate it for a project:

```bash
# In your project, as a git submodule (recommended — stays updatable):
git submodule add https://github.com/ntutangyun/harmony_next_dev_skill.git .claude/skills/harmonyos-app-dev

# …or a plain copy:
git clone https://github.com/ntutangyun/harmony_next_dev_skill.git .claude/skills/harmonyos-app-dev
```

Or to make it user-wide (available in every project):

```bash
mkdir -p ~/.claude/skills
cp -r /path/to/this/repo ~/.claude/skills/harmonyos-app-dev
```

Then in Claude Code, the skill auto-loads when the user mentions HarmonyOS topics, or can be invoked explicitly as `/harmonyos-app-dev`.

## How it works

When Claude sees a HarmonyOS-related prompt:

1. The skill's `description` triggers loading.
2. Claude reads `SKILL.md` for the routing table.
3. For the matching surface (UI, abilities, networking, …), Claude reads the curated reference file.
4. For deeper / edge-case lookups, Claude greps `references/pages/` directly — no internet needed.

## Re-sync when the docs update

No browser needed — the docs SPA is backed by a public JSON API
(`documentPortal/getCatalogTree` + `documentPortal/getDocumentById` on
`svc-drcn.developer.huawei.com`), and the scripts drive it directly:

```bash
pip install beautifulsoup4 lxml

python scripts/update_docs.py --diff   # just show what was added/removed upstream
python scripts/update_docs.py          # fetch all ~5,350 pages (~10 min), swap into references/pages/, rebuild manifest
python scripts/fetch_xiaoyi.py         # fetch the Xiaoyi (小艺) agent doc subtree into _update_work/ for review
```

After a sync, review the catalog diff and refresh the curated files
(`references/00-*.md` … `11-*.md`) plus the three distilled
`references/pages/service-agent-*.md` against the new content, then delete
`_update_work/`.

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
