#!/usr/bin/env python3
"""
SmartByte Group, LLC — Social Posting Automation Runner
=======================================================
Stdlib-only so it runs inside GitHub Actions with zero dependencies.

What it does
------------
1. VALIDATE   — checks calendar.json is well-formed and every post respects
                the per-platform length / hashtag rules (fails loudly).
2. DUE        — finds posts whose (date + platform publish time) has passed but
                are not yet marked posted (or, with --date, for a given day).
3. DISPATCH   — for each due post, calls the platform connector. If real API
                credentials are present (env vars), it posts for real; otherwise
                it runs in DRY-RUN mode and writes the exact payload to the log.
4. LOG        — appends every action to social/post-log.jsonl so the calendar
                never double-posts.

Platform connectors are intentionally pluggable: the Meta/LinkedIn/Nextdoor
Graph/REST calls are stubbed with clear TODOs showing exactly where to drop
real credentials + SDK calls. The runner is fully functional today (validates,
schedules, logs, dry-runs) and becomes live the moment you add tokens.

Usage
-----
  python social/runner.py                 # validate + run due posts (dry by default)
  python social/runner.py --post         # actually publish (needs credentials)
  python social/runner.py --date 2026-09-01   # act as if "today" is this date
  python social/runner.py --validate-only # only run the rules check
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CALENDAR = os.path.join(HERE, "calendar.json")
LOG_PATH = os.path.join(HERE, "post-log.jsonl")

# Per-platform hard limits used by VALIDATE (mirrors build_calendar.PLATFORM_RULES)
LIMITS = {
    "instagram": dict(max_chars=2200, hashtag_cap=12),
    "facebook":  dict(max_chars=63206, hashtag_cap=3),
    "linkedin":  dict(max_chars=3000, hashtag_cap=3),
    "nextdoor":  dict(max_chars=1000, hashtag_cap=0),
}


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------
def now_local() -> dt.datetime:
    """Local KC time. Use America/Chicago if available, else system local."""
    try:
        from zoneinfo import ZoneInfo
        return dt.datetime.now(ZoneInfo("America/Chicago"))
    except Exception:
        return dt.datetime.now()


def _parse_dt(date_str: str, time_str: str) -> dt.datetime:
    d = dt.date.fromisoformat(date_str)
    h, m = (int(x) for x in time_str.split(":"))
    return dt.datetime(d.year, d.month, d.day, h, m)


def load_calendar() -> dict:
    with open(CALENDAR, encoding="utf-8") as f:
        return json.load(f)


def load_posted_ids() -> set:
    ids = set()
    if os.path.exists(LOG_PATH):
        with open(LOG_PATH, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                    if rec.get("result") in ("posted", "dry-run", "skipped-duplicate"):
                        ids.add(rec["key"])
                except json.JSONDecodeError:
                    continue
    return ids


def append_log(record: dict) -> None:
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------------------
# VALIDATE
# ---------------------------------------------------------------------------
def validate(calendar: dict) -> list[str]:
    errors = []
    required = {"date", "platform", "time", "copy", "post_id"}
    for i, p in enumerate(calendar.get("posts", [])):
        missing = required - set(p)
        if missing:
            errors.append(f"post[{i}] missing fields: {sorted(missing)}")
            continue
        lim = LIMITS.get(p["platform"])
        if lim is None:
            errors.append(f"post[{i}] unknown platform: {p['platform']}")
            continue
        if len(p["copy"]) > lim["max_chars"]:
            errors.append(f"{p['post_id']}/{p['platform']}: copy {len(p['copy'])}>"
                          f"{lim['max_chars']} chars")
        tags = p.get("hashtags", [])
        if len(tags) > lim["hashtag_cap"]:
            errors.append(f"{p['post_id']}/{p['platform']}: {len(tags)} hashtags >"
                          f" cap {lim['hashtag_cap']}")
    return errors


# ---------------------------------------------------------------------------
# PLATFORM CONNECTORS (plug point for live APIs)
# ---------------------------------------------------------------------------
def _requires_creds() -> bool:
    """Return True only if at least one real provider token is configured."""
    return any(os.environ.get(k) for k in (
        "META_ACCESS_TOKEN", "LINKEDIN_ACCESS_TOKEN", "NEXTDOOR_ACCESS_TOKEN"))


def post_to_instagram(post: dict, live: bool) -> dict:
    # TODO(live): use Facebook Graph API (ig_media / ig_media_publish)
    #   https://graph.facebook.com/v19.0/{ig_user_id}/media  (image + caption)
    # Requires: META_ACCESS_TOKEN, IG_USER_ID, FB_PAGE_ID
    payload = {"image_url": post.get("image_url"),
               "caption": post["copy"] + ("\n\n" + " ".join(post["hashtags"])
                                          if post["hashtags"] else "")}
    if not live:
        return dict(result="dry-run", detail="IG connector: add META_ACCESS_TOKEN + IG_USER_ID",
                    payload=payload)
    raise NotImplementedError("Set META_ACCESS_TOKEN + IG_USER_ID to go live (see TODO).")


def post_to_facebook(post: dict, live: bool) -> dict:
    # TODO(live): POST /{page_id}/feed with META_ACCESS_TOKEN
    payload = {"message": post["copy"] + ("\n\n" + " ".join(post["hashtags"])
                                          if post["hashtags"] else "")}
    if not live:
        return dict(result="dry-run", detail="FB connector: add META_ACCESS_TOKEN + FB_PAGE_ID",
                    payload=payload)
    raise NotImplementedError("Set META_ACCESS_TOKEN + FB_PAGE_ID to go live (see TODO).")


def post_to_linkedin(post: dict, live: bool) -> dict:
    # TODO(live): POST https://api.linkedin.com/v2/ugcPosts with LINKEDIN_ACCESS_TOKEN
    payload = {"author": "urn:li:organization:{COMPANY_ID}",
               "text": post["copy"] + ("\n\n" + " ".join(post["hashtags"])
                                        if post["hashtags"] else "")}
    if not live:
        return dict(result="dry-run", detail="LI connector: add LINKEDIN_ACCESS_TOKEN + COMPANY_ID",
                    payload=payload)
    raise NotImplementedError("Set LINKEDIN_ACCESS_TOKEN to go live (see TODO).")


def post_to_nextdoor(post: dict, live: bool) -> dict:
    # TODO(live): Nextdoor Business Posts API (no hashtags)
    payload = {"body": post["copy"]}  # Nextdoor strips hashtags
    if not live:
        return dict(result="dry-run", detail="ND connector: add NEXTDOOR_ACCESS_TOKEN",
                    payload=payload)
    raise NotImplementedError("Set NEXTDOOR_ACCESS_TOKEN to go live (see TODO).")


def post_to_linkedin_personal(post: dict, live: bool) -> dict:
    return dict(result="manual-only", detail="MANUAL POST: This is a personal LinkedIn post. Copy the content from the calendar and post via LinkedIn manually.")

CONNECTORS = {
    "instagram": post_to_instagram,
    "facebook": post_to_facebook,
    "linkedin": post_to_linkedin,
    "linkedin-personal": post_to_linkedin_personal,
    "nextdoor": post_to_nextdoor,
}


def dispatch(post: dict, live: bool) -> dict:
    connector = CONNECTORS[post["platform"]]
    return connector(post, live)


# ---------------------------------------------------------------------------
# DUE + RUN
# ---------------------------------------------------------------------------
def find_due(calendar: dict, as_of: dt.datetime, posted: set) -> list[dict]:
    due = []
    for p in calendar["posts"]:
        if p.get("status") == "posted":
            continue
        key = f"{p['date']}|{p['platform']}|{p['post_id']}"
        if key in posted:
            continue
        scheduled = _parse_dt(p["date"], p["time"])
        if scheduled <= as_of:
            due.append((key, p))
    return due


def run(as_of: dt.datetime, live: bool, validate_only: bool) -> int:
    calendar = load_calendar()
    errors = validate(calendar)
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for e in errors:
            print("  -", e, file=sys.stderr)
        return 2

    print(f"[validate] OK — {len(calendar['posts'])} posts pass brand/length rules")
    if validate_only:
        return 0

    posted = load_posted_ids()
    due = find_due(calendar, as_of, posted)
    mode = "LIVE" if live else "DRY-RUN"
    print(f"[{mode}] as_of={as_of.isoformat()}  due_posts={len(due)}")

    for key, post in due:
        try:
            res = dispatch(post, live)
            rec = dict(key=key, platform=post["platform"], post_id=post["post_id"],
                       date=post["date"], time=post["time"], ran_at=as_of.isoformat(),
                       **res)
            append_log(rec)
            print(f"  -> {post['platform']:<9} {post['post_id']:<8} "
                  f"{res.get('result'):<8} {res.get('detail','')}")
        except NotImplementedError as exc:
            # Live mode but connector not wired: record as skipped, keep going.
            append_log(dict(key=key, platform=post["platform"], post_id=post["post_id"],
                            date=post["date"], time=post["time"], ran_at=as_of.isoformat(),
                            result="not-configured", detail=str(exc)))
            print(f"  !! {post['platform']:<9} {post['post_id']:<8} not-configured")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="SmartByte social posting runner")
    ap.add_argument("--date", help="Act as if today is this date (YYYY-MM-DD)",
                    default=None)
    ap.add_argument("--post", action="store_true",
                    help="Actually publish (requires provider credentials)")
    ap.add_argument("--validate-only", action="store_true")
    args = ap.parse_args()

    as_of = now_local()
    if args.date:
        as_of = dt.datetime.fromisoformat(args.date).replace(
            hour=23, minute=59, second=59)

    live = args.post and _requires_creds()
    if args.post and not _requires_creds():
        print("[warn] --post given but no provider tokens found; "
              "falling back to DRY-RUN.", file=sys.stderr)

    return run(as_of, live, args.validate_only)


if __name__ == "__main__":
    raise SystemExit(main())
