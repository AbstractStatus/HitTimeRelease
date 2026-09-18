#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
扫描脚本所在目录下的 APK 文件，生成 files.json 供 index.html 读取。

分类规则：
  manual_  开头 -> manual  （按文件名升序）
  release_ 开头 -> release （按文件名降序，新版本在前）

用法：
  python gen_index.py
每次新增/删除 APK 后、push 到 GitHub 之前运行一次即可。
"""

import json
import os
import sys


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    manual = []
    release = []

    for name in os.listdir(base_dir):
        if not name.lower().endswith(".apk"):
            continue
        path = os.path.join(base_dir, name)
        if not os.path.isfile(path):
            continue
        entry = {"name": name, "size": os.path.getsize(path)}
        if name.startswith("manual_"):
            manual.append(entry)
        elif name.startswith("release_"):
            release.append(entry)

    manual.sort(key=lambda f: f["name"])
    release.sort(key=lambda f: f["name"], reverse=True)

    data = {"manual": manual, "release": release}

    out_path = os.path.join(base_dir, "files.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("files.json 已生成：manual %d 个，release %d 个"
          % (len(manual), len(release)))


if __name__ == "__main__":
    sys.exit(main())
