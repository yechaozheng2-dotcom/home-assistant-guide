#!/usr/bin/env python3
"""
fetch-image.py — 从 Unsplash 搜索并下载图片，自动更新文章 frontmatter 或返回内嵌图片 URL。

用法：
  # 交互式（选封面图）
  python3 scripts/fetch-image.py <markdown文件路径> [关键词]

  # 全自动（取第一张，用于脚本/Agent）
  python3 scripts/fetch-image.py <markdown文件路径> [关键词] --auto

  # 只下载图片，返回 URL（用于内嵌图片）
  python3 scripts/fetch-image.py --inline <关键词> <输出文件名（不含扩展名）>

环境变量：
  UNSPLASH_ACCESS_KEY  — Unsplash API Access Key（必须）
"""

import os
import re
import sys
import json
import shutil
import urllib.request
import urllib.parse
import urllib.error

# ── 配置 ──────────────────────────────────────────────────────────────────────

UNSPLASH_API_BASE = "https://api.unsplash.com"
IMAGE_DIR = "public/images"
IMAGE_URL_PREFIX = "/images"
IMAGE_WIDTH = 1920
IMAGE_HEIGHT = 1080
SITE_KEY = os.environ.get("SITE_KEY", "diy_maker_station").replace("-", "_")

# ── 工具函数 ──────────────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text[:80]


def parse_frontmatter(content: str) -> tuple[dict, str, str]:
    match = re.match(r"^---\n(.*?)\n---\n?(.*)", content, re.DOTALL)
    if not match:
        return {}, "", content
    raw = match.group(1)
    body = match.group(2)
    fm = {}
    for line in raw.split("\n"):
        if ": " in line:
            key, _, val = line.partition(": ")
            fm[key.strip()] = val.strip().strip('"')
        elif line.endswith(":"):
            fm[line.rstrip(":")] = ""
    return fm, raw, body


def update_frontmatter(content: str, key: str, value: str) -> str:
    match = re.match(r"^(---\n)(.*?)(\n---\n?)(.*)", content, re.DOTALL)
    if not match:
        return content
    prefix, raw, suffix, body = match.groups()
    lines = raw.split("\n")
    updated = False
    new_lines = []
    for line in lines:
        if re.match(rf"^{re.escape(key)}\s*:", line):
            new_lines.append(f'{key}: "{value}"')
            updated = True
        else:
            new_lines.append(line)
    if not updated:
        insert_idx = next(
            (i for i, l in enumerate(new_lines) if l.startswith("draft:")),
            len(new_lines)
        )
        new_lines.insert(insert_idx, f'{key}: "{value}"')
    return prefix + "\n".join(new_lines) + suffix + body


def unsplash_search(query: str, access_key: str, per_page: int = 5) -> list[dict]:
    # 支持多个 Key 轮换：主 Key 失败时自动切换备用 Key
    keys = [access_key]
    backup = os.environ.get("UNSPLASH_ACCESS_KEY_2", "").strip()
    if backup and backup != access_key:
        keys.append(backup)

    params = urllib.parse.urlencode({
        "query": query,
        "per_page": per_page,
        "orientation": "landscape",
        "order_by": "relevant",
    })
    url = f"{UNSPLASH_API_BASE}/search/photos?{params}"

    for key in keys:
        req = urllib.request.Request(url, headers={
            "Authorization": f"Client-ID {key}",
            "Accept-Version": "v1",
        })
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read().decode())
                return data.get("results", [])
        except urllib.error.HTTPError as e:
            if e.code == 403 and len(keys) > 1:
                print(f"⚠️  Key 受限，切换备用 Key", file=sys.stderr)
                continue
            body = e.read().decode()
            print(f"❌ Unsplash API 错误 {e.code}：{body}", file=sys.stderr)
            sys.exit(1)
        except urllib.error.URLError as e:
            print(f"❌ 网络错误：{e.reason}", file=sys.stderr)
            sys.exit(1)

    print(f"❌ 所有 Unsplash Key 均受限", file=sys.stderr)
    sys.exit(1)


def download_image(url: str, dest_path: str) -> None:
    req = urllib.request.Request(url, headers={
        "User-Agent": "diy-maker-station/1.0 (fetch-image script)"
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        with open(dest_path, "wb") as f:
            shutil.copyfileobj(resp, f)


def get_project_root() -> str:
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.dirname(script_dir)


def save_photo(photo: dict, filename_slug: str) -> tuple[str, str]:
    """下载图片，返回 (image_url, alt_text)"""
    project_root = get_project_root()
    img_dir = os.path.join(project_root, IMAGE_DIR)
    os.makedirs(img_dir, exist_ok=True)

    dest_filename = f"{filename_slug}.jpg"
    dest_path = os.path.join(img_dir, dest_filename)
    image_url = f"{IMAGE_URL_PREFIX}/{dest_filename}"

    raw_url = photo["urls"]["raw"]
    download_url = f"{raw_url}&w={IMAGE_WIDTH}&h={IMAGE_HEIGHT}&fit=crop&auto=format&q=85"

    download_image(download_url, dest_path)

    alt_text = photo.get("alt_description") or photo.get("description") or filename_slug
    return image_url, alt_text[:120]


# ── 主流程 ────────────────────────────────────────────────────────────────────

def mode_inline(args: list[str], access_key: str) -> None:
    """
    --inline 模式：只下载一张图片，打印 markdown 图片语法到 stdout。
    用法：python3 fetch-image.py --inline <关键词> <文件名slug>
    输出：![alt text](/images/filename.jpg)
    """
    if len(args) < 2:
        print("用法：python3 fetch-image.py --inline <关键词> <文件名slug>", file=sys.stderr)
        sys.exit(1)

    query = args[0]
    filename_slug = slugify(args[1])

    results = unsplash_search(query, access_key, per_page=3)
    if not results:
        print(f"❌ 没有找到图片：{query}", file=sys.stderr)
        sys.exit(1)

    photo = results[0]
    image_url, alt_text = save_photo(photo, filename_slug)

    author_name = photo["user"]["name"]
    author_url = photo["user"]["links"]["html"]
    attribution = (
        f'*Photo by [{author_name}]({author_url}?utm_source={SITE_KEY}&utm_medium=referral) '
        f'on [Unsplash](https://unsplash.com?utm_source={SITE_KEY}&utm_medium=referral)*'
    )

    # 打印 markdown 图片语法 + 署名（供调用方捕获）
    print(f"![{alt_text}]({image_url})")
    print(attribution)


def mode_cover(md_path: str, query: str, auto: bool, access_key: str) -> None:
    """封面图模式：更新文章 frontmatter 的 image 字段"""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    fm, _, _ = parse_frontmatter(content)
    title = fm.get("title", "")
    if not title:
        print("❌ 文章缺少 title 字段", file=sys.stderr)
        sys.exit(1)

    if not query:
        stopwords = {"i", "my", "a", "an", "the", "for", "to", "how", "why",
                     "what", "when", "where", "under", "with", "and", "or"}
        words = [w for w in re.sub(r"[^\w\s]", "", title.lower()).split()
                 if w not in stopwords]
        query = " ".join(words[:5])

    print(f"📷 搜索关键词：{query}", file=sys.stderr)

    results = unsplash_search(query, access_key)
    if not results:
        print("❌ 没有找到相关图片", file=sys.stderr)
        sys.exit(1)

    if auto:
        selected = results[0]
        print(f"🤖 自动选择第一张：{selected.get('alt_description', '')[:60]}", file=sys.stderr)
    else:
        print("\n搜索结果：")
        for i, photo in enumerate(results):
            desc = photo.get("description") or photo.get("alt_description") or "（无描述）"
            author = photo["user"]["name"]
            print(f"  [{i + 1}] {desc[:60]}  — by {author}")
        print("  [0] 跳过，不添加图片")
        while True:
            try:
                choice = int(input(f"\n请选择图片编号 [0-{len(results)}]：").strip())
                if 0 <= choice <= len(results):
                    break
            except (ValueError, EOFError):
                pass
        if choice == 0:
            print("⏭  已跳过")
            sys.exit(0)
        selected = results[choice - 1]

    filename_slug = slugify(title)
    image_url, alt_text = save_photo(selected, filename_slug)

    content = update_frontmatter(content, "image", image_url)
    content = update_frontmatter(content, "imageAlt", alt_text)

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ 封面图已保存并更新 frontmatter", file=sys.stderr)
    print(f"   image: {image_url}", file=sys.stderr)

    author_name = selected["user"]["name"]
    author_url = selected["user"]["links"]["html"]
    print(f"\n📌 Unsplash 署名：", file=sys.stderr)
    print(f'   Photo by <a href="{author_url}?utm_source={SITE_KEY}&utm_medium=referral">{author_name}</a> on Unsplash', file=sys.stderr)


def main():
    access_key = os.environ.get("UNSPLASH_ACCESS_KEY", "").strip()
    if not access_key:
        print("❌ 请设置环境变量 UNSPLASH_ACCESS_KEY", file=sys.stderr)
        sys.exit(1)

    args = sys.argv[1:]

    if not args:
        print(__doc__)
        sys.exit(1)

    if args[0] == "--inline":
        mode_inline(args[1:], access_key)
        return

    md_path = args[0]
    if not os.path.isfile(md_path):
        print(f"❌ 找不到文件：{md_path}", file=sys.stderr)
        sys.exit(1)

    auto = "--auto" in args
    remaining = [a for a in args[1:] if a != "--auto"]
    query = " ".join(remaining) if remaining else ""

    mode_cover(md_path, query, auto, access_key)


if __name__ == "__main__":
    main()
