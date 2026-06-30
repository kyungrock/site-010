#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""루트에서 실행: python publish_blog.py --add blog-draft.json"""
import subprocess
import sys
from pathlib import Path

script = Path(__file__).resolve().parent / "scripts" / "publish_blog.py"
raise SystemExit(subprocess.call([sys.executable, str(script), *sys.argv[1:]]))
