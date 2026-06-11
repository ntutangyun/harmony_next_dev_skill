#!/usr/bin/env python3
"""Fetch the current Xiaoyi Open Platform (小艺开放平台) doc subtree as working-copy
markdown under _update_work/xiaoyi_pages/.

These pages source the three hand-distilled files in references/pages/
(service-agent-dev-intro / service-agent-configuration / service-agent-protocol)
and references/11-xiaoyi-agent-dev.md — after fetching, review and refresh those
by hand (or with Claude) against the fetched content.

Usage (from repo root): python scripts/fetch_xiaoyi.py
"""
import json
import os
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from convert import convert

API_ROOT = "https://svc-drcn.developer.huawei.com/community/servlet/consumer/cn/documentPortal/"
SOURCE_ROOT = "https://developer.huawei.com/consumer/cn/doc/service/"
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "_update_work", "xiaoyi_pages")
os.makedirs(OUT_DIR, exist_ok=True)


def api(endpoint, payload, timeout=120):
    req = urllib.request.Request(API_ROOT + endpoint, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=timeout).read().decode("utf-8-sig"))


d = api("getCatalogTree", {"catalogName": "service", "language": "cn",
                           "objectId": "agent2agent-0000002498656261"})
tops = d["value"]["catalogTreeList"]
xiaoyi = next(t for t in tops if t.get("nodeName") == "小艺开放平台")

entries = []


def walk(nodes, path):
    for n in nodes:
        slug = n.get("relateDocument")
        name = n.get("nodeName", "")
        if slug:
            entries.append({"slug": slug, "title": name, "path": " / ".join(path + [name])})
        walk(n.get("children") or [], path + [name])


walk(xiaoyi["children"], [])
print("xiaoyi pages:", len(entries))


def fetch_one(e):
    slug = e["slug"]
    out_path = os.path.join(OUT_DIR, slug + ".md")
    if os.path.exists(out_path):
        return slug, "cached"
    body = {"objectId": slug, "version": "", "catalogName": "service", "language": "cn"}
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
            md = convert(content["content"], v.get("title") or e["title"], SOURCE_ROOT + slug)
            with open(out_path, "w", encoding="utf-8", newline="\n") as f:
                f.write(f"<!-- nav: {e['path']} | updated: {v.get('displayUpdateTime')} -->\n" + md)
            return slug, "ok"
        except Exception as ex:
            err = repr(ex)
            time.sleep(1.5 * (attempt + 1))
    return slug, f"fetch_error:{err}"


statuses = {}
with ThreadPoolExecutor(max_workers=8) as ex:
    futs = [ex.submit(fetch_one, e) for e in entries]
    for fut in as_completed(futs):
        slug, st = fut.result()
        statuses[st.split(":")[0]] = statuses.get(st.split(":")[0], 0) + 1
        if not st.startswith(("ok", "cached")):
            print("PROBLEM:", slug, st)

json.dump(entries, open(os.path.join(OUT_DIR, "..", "xiaoyi_manifest.json"), "w",
                        encoding="utf-8"), ensure_ascii=False, indent=1)
print("FINAL:", statuses)
