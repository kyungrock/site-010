#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""전 샤워 블로그 HTML 생성"""

from __future__ import annotations

import html
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
POSTS_PATH = ROOT / "data" / "blog-posts.json"
SITE_PATH = ROOT / "config" / "site.json"
INDEX_PATH = ROOT / "index.html"

# 홈 전체글에 항상 포함되는 정적 페이지·기존 글
HOME_STATIC = [
    {
        "href": "posts/exercise-shower-massage-routine.html",
        "title": "운동 후 마사지 전 샤워 루틴 — 근육 회복과 힐링을 한 번에",
        "summary": "헬스·러닝·필라테스 후 땀을 씻고 근육을 풀어주는 전 샤워 루틴. 종목별 포인트와 스포츠마사지 선택 팁까지 정리했습니다.",
        "category": "운동 · 회복",
        "date": "2026-06-17",
        "badge": "운동 · 회복",
    },
    {
        "href": "posts/pre-massage-checklist.html",
        "title": "마사지 당일 전 샤워 체크리스트 — 5분이면 충분합니다",
        "summary": "출근 후 바로 샵에 가는 날, 집에서 받는 날 모두 활용할 수 있는 전 샤워·준비 체크리스트를 단계별로 안내합니다.",
        "category": "체크리스트",
        "date": "2026-06-16",
        "badge": "체크리스트",
    },
    {
        "href": "posts/shower-timing-temperature.html",
        "title": "마사지 전 샤워, 몇 분·몇 도가 적당할까? 온도·시간 가이드",
        "summary": "너무 뜨겁거나 길면 오히려 피로할 수 있어요. 체질·마사지 종류별 권장 온도와 소요 시간을 표로 정리했습니다.",
        "category": "실전 팁",
        "date": "2026-06-14",
        "badge": "실전 팁",
    },
    {
        "href": "posts/shower-blood-circulation.html",
        "title": "샤워가 혈행에 미치는 영향 — 마사지 전 워밍업의 과학",
        "summary": "미지근한 물 한 번이 왜 근육을 풀어줄까요? 체온·혈관·림프 순환 관점에서 마사지 전 샤워의 원리를 쉽게 설명합니다.",
        "category": "혈행",
        "date": "2026-06-12",
        "badge": "혈행",
    },
    {
        "href": "posts/why-shower-before-massage.html",
        "title": "마사지 전 샤워, 꼭 해야 할까? 청결·예절·효과까지",
        "summary": '"그냥 가도 되지 않나?" 싶은 순간에도 전 샤워는 작지만 큰 차이를 만듭니다. 관리사·동반 이용자 배려부터 마사지 효과까지 이유를 정리했습니다.',
        "category": "기본 가이드",
        "date": "2026-06-10",
        "badge": "기본 가이드",
    },
    {
        "href": "guide.html",
        "title": "마사지 전 샤워 기본 가이드",
        "summary": "전 샤워가 왜 중요한지, 어떤 순서로 하면 좋은지 기본 원칙을 정리한 가이드 페이지입니다.",
        "category": "가이드",
        "date": "2026-06-09",
        "badge": "가이드",
    },
    {
        "href": "tips.html",
        "title": "마사지 전 샤워 실전 팁",
        "summary": "온도·시간·제품 선택 등 현장에서 바로 쓸 수 있는 전 샤워 팁 모음입니다.",
        "category": "팁",
        "date": "2026-06-08",
        "badge": "팁",
    },
    {
        "href": "faq.html",
        "title": "마사지 전 샤워 FAQ",
        "summary": "자주 묻는 질문 — 꼭 샤워해야 하나요, 집에서도 동일한가요 등을 Q&A로 정리했습니다.",
        "category": "FAQ",
        "date": "2026-06-07",
        "badge": "FAQ",
    },
]

STATIC_SITEMAP = [
    ("", "weekly", "1.0"),
    ("guide.html", "weekly", "0.9"),
    ("tips.html", "weekly", "0.9"),
    ("faq.html", "monthly", "0.8"),
    ("blog.html", "weekly", "0.9"),
    ("blog-write.html", "monthly", "0.3"),
    ("posts/why-shower-before-massage.html", "monthly", "0.8"),
    ("posts/shower-blood-circulation.html", "monthly", "0.8"),
    ("posts/shower-timing-temperature.html", "monthly", "0.8"),
    ("posts/pre-massage-checklist.html", "monthly", "0.8"),
    ("posts/exercise-shower-massage-routine.html", "monthly", "0.8"),
]


def esc(s: str) -> str:
    return html.escape(s or "", quote=True)


def load_site() -> dict:
    site = json.loads(SITE_PATH.read_text(encoding="utf-8"))
    site.setdefault("domain", "https://agreeable-forest-0c76fb500.7.azurestaticapps.net")
    site.setdefault("site_name", site.get("site_title", "전 샤워"))
    site.setdefault("defaultAuthor", site["site_name"])
    site.setdefault("blogTitle", f"{site['site_name']} 블로그")
    site.setdefault(
        "blogDescription",
        f"{site.get('topic', '마사지 전 샤워')}·{site.get('content_focus', '청결·혈행')} 관련 웰니스 정보를 블로그 형식으로 정리합니다.",
    )
    return site


def load_blog_posts() -> list[dict]:
    if not POSTS_PATH.exists():
        return []
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    posts = [p for p in data.get("posts", []) if p.get("published", True)]
    posts.sort(key=lambda p: p.get("date", ""), reverse=True)
    return posts


def load_all_posts_raw() -> list[dict]:
    if not POSTS_PATH.exists():
        return []
    data = json.loads(POSTS_PATH.read_text(encoding="utf-8"))
    return data.get("posts", [])


def save_posts(posts: list[dict]) -> None:
    POSTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    POSTS_PATH.write_text(
        json.dumps({"posts": posts}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def slugify(text: str) -> str:
    s = (text or "").strip().lower()
    s = re.sub(r"[^\w\s-가-힣]", "", s, flags=re.UNICODE)
    s = re.sub(r"[\s_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:60] or "post"


def format_date_kr(d: str) -> str:
    if not d or len(d) < 10:
        return d or ""
    y, m, day = d[:10].split("-")
    return f"{y}년 {int(m)}월 {int(day)}일"


def inline_format(text: str) -> str:
    s = esc(text)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener noreferrer">\1</a>',
        s,
    )
    return s


def fix_escaped_html(content: str) -> str:
    if "&lt;a " not in content and "&lt;/a&gt;" not in content:
        return content
    return html.unescape(content)


def markdown_to_html(text: str) -> str:
    lines = (text or "").replace("\r\n", "\n").split("\n")
    parts: list[str] = []
    in_ul = False

    def close_ul() -> None:
        nonlocal in_ul
        if in_ul:
            parts.append("</ul>")
            in_ul = False

    for line in lines:
        stripped = line.strip()
        if not stripped:
            close_ul()
            continue
        if re.search(r"^<a\s+href=", stripped, re.I) or re.search(
            r"^<p>\s*<a\s+href=", stripped, re.I
        ):
            close_ul()
            parts.append(stripped if stripped.startswith("<p>") else f"<p>{stripped}</p>")
        elif stripped.startswith("<") and (stripped.endswith(">") or "</" in stripped):
            close_ul()
            parts.append(stripped)
        elif stripped.startswith("### "):
            close_ul()
            parts.append(f"<h3>{inline_format(stripped[4:])}</h3>")
        elif stripped.startswith("## "):
            close_ul()
            parts.append(f"<h2>{inline_format(stripped[3:])}</h2>")
        elif stripped.startswith("# "):
            close_ul()
            parts.append(f"<h2>{inline_format(stripped[2:])}</h2>")
        elif stripped.startswith("* "):
            if not in_ul:
                parts.append("<ul>")
                in_ul = True
            parts.append(f"<li>{inline_format(stripped[2:])}</li>")
        else:
            close_ul()
            parts.append(f"<p>{inline_format(stripped)}</p>")

    close_ul()
    return "\n".join(parts)


def normalize_content(content: str) -> str:
    c = (content or "").strip()
    if not c:
        return ""
    if c.startswith("<"):
        return fix_escaped_html(c)
    return fix_escaped_html(markdown_to_html(c))


def site_header(site: dict, *, active: str = "", depth: int = 0) -> str:
    prefix = "../" * depth
    emoji = site.get("emoji", "🚿")
    name = site.get("site_name", "전 샤워")
    links = [
        ("홈", "index.html", "home"),
        ("가이드", "guide.html", "guide"),
        ("블로그", "blog.html", "blog"),
        ("팁", "tips.html", "tips"),
        ("FAQ", "faq.html", "faq"),
        ("글쓰기", "blog-write.html", "write"),
    ]
    nav = "\n".join(
        f'        <a href="{prefix}{href}" class="nav-link{" active" if key == active else ""}">{label}</a>'
        for label, href, key in links
    )
    return f"""  <header class="site-header">
    <div class="container header-inner">
      <a href="{prefix}index.html" class="logo">
        <span class="logo-icon">{emoji}</span>
        <span class="logo-text">마사지 <strong>{esc(name)}</strong></span>
      </a>
      <nav class="nav">
{nav}
      </nav>
    </div>
  </header>"""


def site_footer(site: dict) -> str:
    name = site.get("site_name", site.get("site_title", "전 샤워"))
    return f"""  <footer class="site-footer">
    <div class="container">
      <p class="footer-brand">{esc(name)}</p>
      <p class="footer-tagline">{esc(site.get("tagline", ""))}</p>
      <p class="footer-copy">&copy; 2026 {esc(name)}. All rights reserved.</p>
    </div>
  </footer>"""


def post_home_card(post: dict, depth: int = 0) -> str:
    prefix = "../" * depth
    if post.get("href"):
        url = f"{prefix}{esc(post['href'])}"
    else:
        url = f"{prefix}blog/{esc(post['id'])}.html"
    badge = esc(
        post.get("badge")
        or post.get("category")
        or ((post.get("tags") or ["블로그"])[0])
    )
    dt = esc(post.get("date", ""))
    display = esc(format_date_kr(post.get("date", "")))
    title = esc(post.get("title", ""))
    summary = esc(post.get("summary", ""))
    return f"""      <article class="post-card">
        <a href="{url}" class="post-card-link">
          <div class="post-card-image" aria-hidden="true">
            <span class="post-card-badge">{badge}</span>
          </div>
          <div class="post-card-body">
            <time datetime="{dt}" class="post-date">{display}</time>
            <h3 class="post-card-title">{title}</h3>
            <p class="post-card-excerpt">{summary}</p>
            <span class="read-more">글 읽기 →</span>
          </div>
        </a>
      </article>"""


def home_feed_items(posts: list[dict]) -> list[dict]:
    items = list(posts) + list(HOME_STATIC)
    items.sort(key=lambda p: p.get("date", ""), reverse=True)
    return items


def replace_html_block(html: str, block: str, content: str) -> str:
    pattern = rf"(<!-- {block}_START -->).*?(<!-- {block}_END -->)"
    if not re.search(pattern, html, re.S):
        raise ValueError(f"index.html에 <!-- {block}_START/END --> 마커가 없습니다.")
    return re.sub(pattern, rf"\1\n{content}\n    \2", html, count=1, flags=re.S)


def update_index_html(out_dir: Path, posts: list[dict]) -> None:
    index_path = out_dir / "index.html"
    if not index_path.is_file():
        return
    html = index_path.read_text(encoding="utf-8")
    feed = home_feed_items(posts)
    feed_html = "\n".join(post_home_card(p) for p in feed)
    html = replace_html_block(html, "HOME_FEED", feed_html)
    index_path.write_text(html, encoding="utf-8")


def blog_sitemap_urls() -> list[str]:
    return [f"blog/{post['id']}.html" for post in load_blog_posts()]


def post_card_html(post: dict, depth: int = 0) -> str:
    """블로그 목록 카드 (정적 글·동적 글 공통)"""
    prefix = "../" * depth
    if post.get("href"):
        url = f"{prefix}{esc(post['href'])}"
    else:
        url = f"{prefix}blog/{esc(post['id'])}.html"
    badge = esc(
        post.get("badge")
        or post.get("category")
        or ((post.get("tags") or ["블로그"])[0])
    )
    tags = post.get("tags") or []
    tag_html = "".join(f'<span class="blog-tag">{esc(t)}</span>' for t in tags[:5])
    tag_block = f'<div class="blog-tags">{tag_html}</div>' if tag_html else ""
    return f"""      <article class="blog-card">
        <a href="{url}" class="blog-card-link">
          <div class="blog-card-body">
            <span class="blog-card-badge">{badge}</span>
            <time class="blog-date" datetime="{esc(post.get("date", ""))}">{esc(format_date_kr(post.get("date", "")))}</time>
            <h2 class="blog-card-title">{esc(post.get("title", ""))}</h2>
            <p class="blog-card-summary">{esc(post.get("summary", ""))}</p>
            {tag_block}
          </div>
        </a>
      </article>"""


def render_blog_list(site: dict, posts: list[dict]) -> str:
    domain = site["domain"].rstrip("/")
    canonical = f"{domain}/blog.html"
    page_title = f"{site.get('blogTitle', '블로그')} | {site['site_name']}"
    meta_desc = site.get("blogDescription", "")
    items = home_feed_items(posts)
    cards = "\n".join(post_card_html(p) for p in items) or (
        '      <p class="muted blog-empty">아직 등록된 글이 없습니다. '
        '<a href="blog-write.html">첫 글 작성하기</a></p>'
    )
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(page_title)}</title>
  <meta name="description" content="{esc(meta_desc)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="css/style.css">
  <link rel="stylesheet" href="css/common.css">
  <link rel="stylesheet" href="css/blog.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
</head>
<body>
{site_header(site, active="blog")}
  <main>
    <section class="blog-hero">
      <div class="container">
        <h1>{esc(site.get("blogTitle", "블로그"))}</h1>
        <p class="muted">{esc(meta_desc)}</p>
        <a href="blog-write.html" class="blog-write-btn">✏️ 글 작성하기</a>
      </div>
    </section>
    <section class="blog-list-section">
      <div class="container">
        <div class="blog-grid">
{cards}
        </div>
      </div>
    </section>
  </main>
{site_footer(site)}
</body>
</html>
"""


def render_blog_post(site: dict, post: dict, all_posts: list[dict]) -> str:
    domain = site["domain"].rstrip("/")
    canonical = f"{domain}/blog/{post['id']}.html"
    title = post.get("title", "")
    page_title = f"{title} | {site['site_name']}"
    meta_desc = (post.get("summary", "") or "")[:160]
    tags = post.get("tags") or []
    tag_html = "".join(f'<span class="blog-tag">{esc(t)}</span>' for t in tags)
    others = [p for p in all_posts if p["id"] != post["id"]][:3]
    related = ""
    if others:
        items = "\n".join(
            f'        <li><a href="{esc(p["id"])}.html">{esc(p.get("title", ""))}</a></li>'
            for p in others
        )
        related = f"""        <aside class="blog-related card">
          <h3>다른 글 보기</h3>
          <ul class="blog-related-list">
{items}
          </ul>
        </aside>"""
    article_ld = json.dumps(
        {
            "@context": "https://schema.org",
            "@type": "BlogPosting",
            "headline": title,
            "description": meta_desc,
            "datePublished": post.get("date", ""),
            "author": {"@type": "Organization", "name": post.get("author", site["site_name"])},
            "publisher": {"@type": "Organization", "name": site["site_name"]},
            "mainEntityOfPage": canonical,
            "inLanguage": "ko-KR",
        },
        ensure_ascii=False,
        indent=2,
    )
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(page_title)}</title>
  <meta name="description" content="{esc(meta_desc)}">
  <meta name="robots" content="index, follow">
  <link rel="canonical" href="{canonical}">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(title)}">
  <link rel="stylesheet" href="../css/style.css">
  <link rel="stylesheet" href="../css/common.css">
  <link rel="stylesheet" href="../css/blog.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700&family=Playfair+Display:wght@600&display=swap" rel="stylesheet">
  <script type="application/ld+json">
{article_ld}
  </script>
</head>
<body>
{site_header(site, active="blog", depth=1)}
  <main>
    <article class="blog-article">
      <div class="container blog-article-inner">
        <nav class="blog-breadcrumb" aria-label="breadcrumb">
          <a href="../index.html">홈</a> › <a href="../blog.html">블로그</a>
        </nav>
        <header class="blog-article-header">
          <time datetime="{esc(post.get("date", ""))}">{esc(format_date_kr(post.get("date", "")))}</time>
          <h1>{esc(title)}</h1>
          <div class="blog-tags">{tag_html}</div>
          <p class="blog-author muted">작성: {esc(post.get("author", site["site_name"]))}</p>
        </header>
        <div class="blog-content card">
          {normalize_content(post.get("content", ""))}
        </div>
{related}
        <p><a href="../blog.html" class="blog-back">← 블로그 목록으로</a></p>
      </div>
    </article>
  </main>
{site_footer(site)}
</body>
</html>
"""


def write_sitemap(out_dir: Path, site: dict, posts: list[dict]) -> None:
    domain = site["domain"].rstrip("/")
    today = date.today().isoformat()
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for path, freq, priority in STATIC_SITEMAP:
        loc = f"{domain}/" if not path else f"{domain}/{path}"
        lines.append(f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{today}</lastmod>\n    <changefreq>{freq}</changefreq>\n    <priority>{priority}</priority>\n  </url>")
    for post in posts:
        if not post.get("published", True):
            continue
        loc = f"{domain}/blog/{post['id']}.html"
        lastmod = (post.get("date") or today)[:10]
        lines.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>monthly</changefreq>\n    <priority>0.7</priority>\n  </url>"
        )
    lines.append("</urlset>\n")
    (out_dir / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")


def write_blog_pages(out_dir: Path, site: dict) -> int:
    posts = load_blog_posts()
    (out_dir / "blog.html").write_text(render_blog_list(site, posts), encoding="utf-8")
    update_index_html(out_dir, posts)
    blog_dir = out_dir / "blog"
    blog_dir.mkdir(exist_ok=True)
    count = 1
    for post in posts:
        (blog_dir / f"{post['id']}.html").write_text(
            render_blog_post(site, post, posts), encoding="utf-8"
        )
        count += 1
    return count


def merge_draft(draft_path: Path, site: dict | None = None) -> dict:
    draft = json.loads(draft_path.read_text(encoding="utf-8"))
    if site is None:
        site = load_site()
    if "posts" in draft:
        new_posts = draft["posts"]
    elif "id" in draft:
        new_posts = [draft]
    else:
        raise ValueError("draft JSON must be a post object or {posts: [...]}")

    posts = load_all_posts_raw()
    by_id = {p["id"]: i for i, p in enumerate(posts)}
    added, updated = 0, 0
    for p in new_posts:
        if not p.get("id"):
            p["id"] = slugify(p.get("title", "post")) + "-" + date.today().strftime("%Y%m%d")
        if not p.get("date"):
            p["date"] = date.today().isoformat()
        p.setdefault("published", True)
        p.setdefault("author", site.get("defaultAuthor", site["site_name"]))
        p.setdefault("category", (p.get("tags") or ["블로그"])[0] if p.get("tags") else "블로그")
        if p.get("content"):
            p["content"] = normalize_content(str(p["content"]))
        if p["id"] in by_id:
            posts[by_id[p["id"]]] = p
            updated += 1
        else:
            posts.append(p)
            added += 1
    posts.sort(key=lambda x: x.get("date", ""), reverse=True)
    save_posts(posts)
    return {"added": added, "updated": updated, "total": len(posts)}
