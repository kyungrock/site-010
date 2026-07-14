#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""10편 날짜를 오늘(2026-07-14)로 맞추고 publish"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
TODAY = "2026-07-14"
IDS = {
    "running-post-workout-pre-massage-shower",
    "pregnancy-pre-massage-shower-safety",
    "foot-reflexology-pre-shower-clean",
    "leg-swelling-lymph-pre-shower",
    "fine-dust-day-pre-massage-shower",
    "hydration-before-massage-and-shower",
    "night-shift-worker-pre-massage-shower",
    "swim-after-pool-pre-massage-shower",
    "golf-round-pre-massage-shower",
    "rainy-season-humidity-pre-shower",
}


def main() -> None:
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    n = 0
    for p in data["posts"]:
        if p.get("id") in IDS:
            p["date"] = TODAY
            n += 1
    data["posts"].sort(key=lambda x: x.get("date", ""), reverse=True)
    POSTS_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"updated dates to {TODAY}: {n} posts")
    subprocess.run([sys.executable, str(ROOT / "scripts" / "publish_blog.py")], check=True)


if __name__ == "__main__":
    main()
