#!/usr/bin/env python3
"""Refresh the bundled offline HarmonyOS docs from developer.huawei.com.

The docs SPA is backed by a JSON API (no browser needed):
  POST .../documentPortal/getCatalogTree    -> full nav tree (slugs + titles)
  POST .../documentPortal/getDocumentById   -> per-page HTML content

Usage (from repo root):
  python scripts/update_docs.py            # diff catalog, fetch all, swap pages
  python scripts/update_docs.py --diff     # only print the catalog diff

Requires: beautifulsoup4, lxml.
Run time: ~10 min for the full ~5,350-page fetch (8 workers).
"""
import argparse
import json
import os
import shutil
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from convert import convert

API_ROOT = "https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/"
SOURCE_ROOT = "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES_DIR = os.path.join(REPO, "references", "pages")
MANIFEST = os.path.join(REPO, "references", "manifest.json")
WORK_DIR = os.path.join(REPO, "_update_work")

# Hand-distilled Xiaoyi pages (sourced from doc/service/*, not harmonyos-guides) —
# never deleted by the swap; refresh them separately (see scripts/fetch_xiaoyi.py).
DISTILLED = [
    {"p": "service-agent-dev-intro", "t": "鸿蒙智能体", "l": 1},
    {"p": "service-agent-configuration", "t": "开发智能体-配置与编排", "l": 2},
    {"p": "service-agent-protocol", "t": "鸿蒙Agent通信协议", "l": 2},
]
KEEP_FILES = {e["p"] + ".md" for e in DISTILLED}


def api(endpoint, payload, timeout=120):
    req = urllib.request.Request(API_ROOT + endpoint, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8-sig"))


def get_manifest_entries():
    d = api("getCatalogTree", {"catalogName": "harmonyos-guides", "language": "cn",
                               "objectId": "application-dev-guide"})
    entries = []

    def walk(nodes, level):
        for n in nodes:
            slug = n.get("relateDocument")
            if slug:
                entries.append({"p": slug, "t": n["nodeName"], "l": level})
            walk(n.get("children") or [], level + 1)

    walk(d["value"]["catalogTreeList"], 1)
    return entries


def print_diff(entries):
    old = json.load(open(MANIFEST, encoding="utf-8-sig"))
    old_by = {e["p"]: e for e in old}
    new_by = {e["p"]: e for e in entries}
    added = [s for s in new_by if s not in old_by]
    removed = [s for s in old_by if s not in new_by and not s.startswith("service-agent")]
    print(f"catalog: {len(entries)} pages | added: {len(added)} | removed: {len(removed)}")
    for s in added:
        print(f"  + {s}  {new_by[s]['t']}")
    for s in removed:
        print(f"  - {s}  {old_by[s]['t']}")


def fetch_one(entry, out_dir):
    slug = entry["p"]
    out_path = os.path.join(out_dir, slug + ".md")
    if os.path.exists(out_path):
        return slug, "cached"
    body = {"objectId": slug, "version": "", "catalogName": "harmonyos-guides", "language": "cn"}
    err = None
    for attempt in range(4):
        try:
            d = api("getDocumentById", body, timeout=60)
            if d.get("code") != 0:
                return slug, f"api_error:{d.get('code')}"
            v = d["value"]
            content = v.get("content") or {}
            if content.get("type") != "html":
                return slug, f"non_html:{content.get('type')}"
            md = convert(content["content"], v.get("title") or entry["t"], SOURCE_ROOT + slug)
            tmp = out_path + ".tmp"
            with open(tmp, "w", encoding="utf-8", newline="\n") as f:
                f.write(md)
            os.replace(tmp, out_path)
            return slug, "ok"
        except Exception as e:
            err = repr(e)
            time.sleep(1.5 * (attempt + 1))
    return slug, f"fetch_error:{err}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--diff", action="store_true", help="only print the catalog diff")
    args = ap.parse_args()

    entries = get_manifest_entries()
    print_diff(entries)
    if args.diff:
        return

    out_dir = os.path.join(WORK_DIR, "new_pages")
    os.makedirs(out_dir, exist_ok=True)
    statuses = {}
    with ThreadPoolExecutor(max_workers=8) as ex:
        futs = [ex.submit(fetch_one, e, out_dir) for e in entries]
        for i, fut in enumerate(as_completed(futs), 1):
            slug, st = fut.result()
            statuses[st.split(":")[0]] = statuses.get(st.split(":")[0], 0) + 1
            if not st.startswith(("ok", "cached")):
                print("PROBLEM:", slug, st)
            if i % 500 == 0:
                print(f"{i}/{len(entries)}")
    print("fetch:", statuses)
    if statuses.get("ok", 0) + statuses.get("cached", 0) != len(entries):
        print("ABORT: not all pages fetched; pages dir left untouched "
              f"(re-run to resume — fetched pages are cached in {out_dir})")
        sys.exit(1)

    # swap: remove old guide pages (keep distilled), copy in new, rewrite manifest
    for f in os.listdir(PAGES_DIR):
        if f.endswith(".md") and f not in KEEP_FILES:
            os.remove(os.path.join(PAGES_DIR, f))
    for f in os.listdir(out_dir):
        if f.endswith(".md"):
            shutil.copyfile(os.path.join(out_dir, f), os.path.join(PAGES_DIR, f))
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as f:
        json.dump(entries + DISTILLED, f, ensure_ascii=False, separators=(",", ":"))
    print(f"done: {len(entries)} guide pages + {len(DISTILLED)} distilled; manifest rewritten")
    print(f"NOTE: review the curated references/00-*.md..11-*.md against the diff above, "
          f"then delete {WORK_DIR}")


if __name__ == "__main__":
    main()
