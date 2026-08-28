#!/usr/bin/env python3
"""
SmartByte Group, LLC — Social Media Calendar Builder
====================================================
Single source of truth for the 30-day social calendar across
Instagram, Facebook, LinkedIn, and Nextdoor.

It reads:
  * CONTENT_BANK  — reusable post drafts (6 per week x 4 weeks = 24)
  * WEEK_THEMES   — the 4-week content strategy (from BrandStyleGuide /
                    the Sept 2026 plan: Residential -> Commercial ->
                    Security -> Local Trust)
  * PLATFORM_RULES — per-platform cadence + adaptation notes
  * POSTING_TIME  — when each platform should publish (local KC time)

and emits:
  * social/calendar.json   — machine-readable schedule (one entry per
                             platform per scheduled day)
  * social/calendar.md     — human-readable 30-day calendar
  * social/drafts/weekN.md — per-week post drafts for human review

Run:  python social/build_calendar.py
"""
from __future__ import annotations

import json
import os
from datetime import date, timedelta

# ---------------------------------------------------------------------------
# CONFIG
# ---------------------------------------------------------------------------
# 30-day window start. Change this to roll the calendar forward.
# Default: the day this sprint begins (today).
START_DATE = date(2026, 8, 28)
CALENDAR_DAYS = 30

# Kansas City is Central Time (CDT in Aug/Sep). Stored as 24h "HH:MM".
# These are the brand-default publish times; the runner uses them as the
# "is this post due yet?" gate.
POSTING_TIMES = {
    "instagram": "09:00",
    "facebook":  "11:00",
    "linkedin":  "08:00",
    "nextdoor":  "17:00",
}

PLATFORM_RULES = {
    "instagram": {
        "cadence": "MWF + 1 weekend",
        "schedule_days": [0, 2, 4, 5],   # Mon, Wed, Fri, Sat
        "max_chars": 2200,
        "hashtag_cap": 12,
        "adapt": "Lead with the visual. First line must hook. 8-12 hashtags "
                 "in a comment-style block. Use carousel-friendly copy.",
    },
    "facebook": {
        "cadence": "3x/week",
        "schedule_days": [0, 2, 4],       # Mon, Wed, Fri
        "max_chars": 63206,
        "hashtag_cap": 3,
        "adapt": "Write like a neighbor posting to the neighborhood group. "
                 "1-3 hashtags max. Ask a question to invite comments.",
    },
    "linkedin-personal": {
        "cadence": "2x/week",
        "schedule_days": [1, 3],          # Tue, Thu
        "max_chars": 3000,
        "hashtag_cap": 3,
        "adapt": "MANUAL POST: Personal LinkedIn profile. Focus on founder-led tech leadership, local business insights, and industry trends.",
    },
    "linkedin": {
        "cadence": "2x/week",
        "schedule_days": [1, 3],          # Tue, Thu
        "max_chars": 3000,
        "hashtag_cap": 3,
        "adapt": "Professional, outcome-first. No hashtag stuffing (max 3). "
                 "Lead with a business result or lesson. Plain-English only.",
    },
    "nextdoor": {
        "cadence": "2x/week",
        "schedule_days": [1, 3],          # Tue, Thu
        "max_chars": 1000,
        "hashtag_cap": 0,
        "adapt": "Hyper-local and helpful. NO hashtags (Nextdoor strips them). "
                 "Frame as a KC neighbor sharing a tip. Mention the metro area.",
    },
}

# ---------------------------------------------------------------------------
# CONTENT BANK  (24 drafts: 6 per week, mapped onto the 4-week theme arc)
# Each draft: id, week, theme, title, topic, tone, base copy, hashtags, cta
# ---------------------------------------------------------------------------
CONTENT_BANK = [
    # ---- WEEK 1 — RESIDENTIAL (Wi-Fi / smart home) -----------------------
    dict(id="w1-p1", week=1, theme="Residential", title="Dead Zones? We Fix That.",
         topic="Wi-Fi dead zones", tone="Warm, relatable",
         copy=("Dead zones in the living room? Buffering during the big game? "
               "We hear you. We're your Kansas City neighbors who happen to be "
               "Wi-Fi experts. Get a straight answer and a fast, reliable network."),
         hashtags=["#SmartByteKC", "#KCTech", "#HomeNetworking", "#KansasCity"],
         cta="Book a free home network audit."),
    dict(id="w1-p2", week=1, theme="Residential", title="Whole-Home Coverage, Finally",
         topic="Mesh Wi-Fi 6E", tone="Warm, educational",
         copy=("Tired of the 'one bar' corner of your house? A properly designed "
               "mesh network gives every room full speed. We map your home, then "
               "install and explain it in plain English."),
         hashtags=["#SmartByteKC", "#MeshWiFi", "#KCNeighbors", "#SmartHome"],
         cta="See what whole-home Wi-Fi looks like."),
    dict(id="w1-p3", week=1, theme="Residential", title="Hidden Cables, Clean Walls",
         topic="Concealed TV mounting", tone="Warm, reassuring",
         copy=("Your home theater, finally wire-free. We mount, conceal, and "
               "calibrate — no spaghetti cables, no guesswork. You just press play."),
         hashtags=["#SmartByteKC", "#HomeTheater", "#KansasCity", "#TVInstall"],
         cta="Get a clean, pro TV install."),
    dict(id="w1-p4", week=1, theme="Residential", title="Your Smart Home, Actually Simple",
         topic="Smart home hub setup", tone="Warm, plain-English",
         copy=("Smart plugs, cameras, thermostats — they're supposed to make life "
               "easier, not harder. We set up one hub that just works, and we show "
               "you how to use it."),
         hashtags=["#SmartByteKC", "#SmartHome", "#KCHome", "#TechHelp"],
         cta="Let's simplify your setup."),
    dict(id="w1-p5", week=1, theme="Residential", title="Vince Answers the Phone",
         topic="Local support", tone="Friendly, local",
         copy=("When something goes sideways at 8pm, you want a neighbor, not a "
               "call center in another time zone. At SmartByte, Vince answers. "
               "That's the whole business model."),
         hashtags=["#SmartByteKC", "#KCLocal", "#SupportPlan", "#KansasCity"],
         cta="Talk to a real KC human."),
    dict(id="w1-p6", week=1, theme="Residential", title="Back to School, Back Online",
         topic="Home network for remote learning", tone="Warm, timely",
         copy=("Back-to-school season means more devices fighting for bandwidth. "
               "We tune your network so homework, Zoom, and game night all run "
               "smooth — no more 'the wifi's down!' meltdowns."),
         hashtags=["#SmartByteKC", "#KC BackToSchool", "#HomeNetworking", "#KansasCity"],
         cta="Get the house back online."),

    # ---- WEEK 2 — COMMERCIAL (infrastructure that scales) ----------------
    dict(id="w2-p1", week=2, theme="Commercial", title="Infrastructure That Grows With You",
         topic="Commercial cabling / scaling", tone="Authoritative, outcome-focused",
         copy=("Infrastructure that grows with you. From server-rack organization to "
               "secure office cabling, we deliver the precision engineering your KC "
               "business needs to scale — backed by SLAs, built to last."),
         hashtags=["#SmartByteKC", "#KCBusiness", "#KCInfrastructure", "#ManagedIT"],
         cta="Request a proposal today."),
    dict(id="w2-p2", week=2, theme="Commercial", title="The Rack Cleanup Nobody Asked For",
         topic="Server rack cleanup", tone="Authoritative, visual",
         copy=("A tangled rack isn't just ugly — it's a downtime risk. We re-label, "
               "re-route, and document your infrastructure so the next outage takes "
               "minutes to fix, not hours."),
         hashtags=["#SmartByteKC", "#KCInfrastructure", "#ManagedIT", "#KCBusiness"],
         cta="Book a rack audit."),
    dict(id="w2-p3", week=2, theme="Commercial", title="Guest Wi-Fi That Won't Leak",
         topic="Guest VLANs", tone="Authoritative, security-minded",
         copy=("Your customers get fast Wi-Fi. Your internal network stays private. "
               "We deploy separate, secure guest networks (VLANs) so a coffee-shop "
               "password never touches your POS."),
         hashtags=["#SmartByteKC", "#CyberSecurity", "#KCBusiness", "#Networking"],
         cta="Make your network compliant."),
    dict(id="w2-p4", week=2, theme="Commercial", title="99.9% Uptime, In Writing",
         topic="Managed IT SLA", tone="Authoritative, trustworthy",
         copy=("99.9% uptime. Contractual SLAs. A dedicated KC point of contact. "
               "Managed IT shouldn't feel like a gamble — it should feel like a "
               "safety net you never have to think about."),
         hashtags=["#SmartByteKC", "#ManagedIT", "#KCBusiness", "#SLA"],
         cta="Request your SLA proposal."),
    dict(id="w2-p5", week=2, theme="Commercial", title="Move-In Day Without the Chaos",
         topic="Office build-out / deployment", tone="Authoritative, project-led",
         copy=("New office? We handle drops, racks, access points, and VoIP — "
               "sequenced so your team walks in Monday to a network that's already "
               "working. Deployment done right, on schedule."),
         hashtags=["#SmartByteKC", "#KCBusiness", "#OfficeBuildout", "#Deployment"],
         cta="Plan your move with us."),
    dict(id="w2-p6", week=2, theme="Commercial", title="Why KC Businesses Choose SmartByte",
         topic="Local partnership", tone="Authoritative, relational",
         copy=("We're not a faceless MSP. We're your neighbors — which means we "
               "show up, we document everything, and we treat your uptime like our "
               "own. That's the KC way to do managed IT."),
         hashtags=["#SmartByteKC", "#KCBusiness", "#LocalIT", "#KansasCity"],
         cta="Partner with a local team."),

    # ---- WEEK 3 — SECURITY (peace of mind 24/7) --------------------------
    dict(id="w3-p1", week=3, theme="Security", title="Sleep Better. We're Watching.",
         topic="24/7 IP camera monitoring", tone="Reassuring, tech-forward",
         copy=("Sleep better knowing your business is monitored 24/7. HD 4K IP "
               "cameras, designed and installed for total peace of mind. We design "
               "the security — you run the business."),
         hashtags=["#SmartByteKC", "#KCSecurity", "#IPCameras", "#KansasCityBusiness"],
         cta="Get a security design consult."),
    dict(id="w3-p2", week=3, theme="Security", title="One App. Every Camera.",
         topic="NVR / unified view", tone="Reassuring, simple",
         copy=("Ten cameras, three apps, zero patience? We consolidate everything "
               "into one clean dashboard you can check from your phone — at the "
               "shop or on the lake."),
         hashtags=["#SmartByteKC", "#IPCameras", "#KCSecurity", "#KCbusiness"],
         cta="Simplify your security view."),
    dict(id="w3-p3", week=3, theme="Security", title="Who's At The Door (Even At 2AM)",
         topic="Access control", tone="Reassuring, controlled",
         copy=("Door access that logs every entry and locks down on schedule. "
               "No lost keys, no copied fobs. Just clean, auditable control over "
               "who walks into your building."),
         hashtags=["#SmartByteKC", "#AccessControl", "#KCSecurity", "#KCbusiness"],
         cta="Lock down your access."),
    dict(id="w3-p4", week=3, theme="Security", title="Case Study: From Blind Spots to 4K",
         topic="Before/after install", tone="Proof-driven, reassuring",
         copy=("A local KC shop came to us with blind corners and a DVR from 2014. "
               "Six weeks later: 4K coverage, cloud backup, and an owner who finally "
               "sleeps. Swipe to see the before/after."),
         hashtags=["#SmartByteKC", "#CaseStudy", "#KCSecurity", "#KansasCity"],
         cta="See your before/after."),
    dict(id="w3-p5", week=3, theme="Security", title="Your Network, Monitored 24/7",
         topic="Managed network security", tone="Reassuring, proactive",
         copy=("Firewalls are set-and-forget until they're not. We monitor your "
               "network around the clock, patch proactively, and flag threats before "
               "they become headlines."),
         hashtags=["#SmartByteKC", "#CyberSecurity", "#KCBusiness", "#ManagedIT"],
         cta="Put your network on watch."),
    dict(id="w3-p6", week=3, theme="Security", title="Security Doesn't Have to Feel Like Black Magic",
         topic="Plain-English security", tone="Reassuring, on-brand",
         copy=("Technology shouldn't feel like black magic. We explain your security "
               "setup in plain English — what it does, why it matters, and what to "
               "do if something looks off."),
         hashtags=["#SmartByteKC", "#KCSecurity", "#ExplainNotConfuse", "#KC"],
         cta="Get the straight story."),

    # ---- WEEK 4 — LOCAL TRUST (why choose a KC expert) -------------------
    dict(id="w4-p1", week=4, theme="Local Trust", title="Meet Vince, Founder of SmartByte",
         topic="Founder story", tone="Friendly, community-oriented",
         copy=("I'm Vince, founder of SmartByte. I believe technology shouldn't feel "
               "like black magic. We're here to simplify it for you, right here in "
               "Kansas City. Need a hand with your tech? Let's talk."),
         hashtags=["#SmartByteKC", "#KCLocal", "#ExpertSupport", "#KansasCity"],
         cta="Say hi to Vince."),
    dict(id="w4-p2", week=4, theme="Local Trust", title="Proud to Be 100% KC",
         topic="Local roots", tone="Friendly, proud",
         copy=("We live here, we work here, we shop here. When you hire SmartByte, "
               "the money stays in Kansas City and the tech stays accountable. "
               "100% local, every job."),
         hashtags=["#SmartByteKC", "#ShopLocalKC", "#KansasCity", "#SupportLocal"],
         cta="Hire a neighbor."),
    dict(id="w4-p3", week=4, theme="Local Trust", title="A Note From the Team",
         topic="Team spotlight", tone="Friendly, human",
         copy=("Behind every clean rack and calm support call is a small KC team that "
               "genuinely likes fixing things. Meet the people who answer when you "
               "call. (Swipe for faces.)"),
         hashtags=["#SmartByteKC", "#KCTeam", "#MeetTheTeam", "#KansasCity"],
         cta="Meet your local team."),
    dict(id="w4-p4", week=4, theme="Local Trust", title="What 5 Stars Actually Means",
         topic="Social proof", tone="Friendly, credible",
         copy=("'They explained everything and didn't make me feel dumb.' That's the "
               "kind of review we chase. Five stars isn't a metric to us — it's a "
               "promise we keep for every KC neighbor."),
         hashtags=["#SmartByteKC", "#KCReviews", "#KansasCity", "#TrustedLocal"],
         cta="Read our reviews."),
    dict(id="w4-p5", week=4, theme="Local Trust", title="Know a KC Business That Needs Tech Help?",
         topic="Referral ask", tone="Friendly, reciprocal",
         copy=("Love your SmartByte experience? Send a KC friend our way. For every "
               "referral that books a project, we thank you with a $50 gift card. "
               "Good tech, good neighbors, good karma."),
         hashtags=["#SmartByteKC", "#Referral", "#KansasCity", "#ShopLocalKC"],
         cta="Refer a neighbor."),
    dict(id="w4-p6", week=4, theme="Local Trust", title="One Month In — Thank You, KC",
         topic="Recap / community", tone="Friendly, grateful",
         copy=("One month, a lot of clean racks and quieter dead zones. Thank you, "
               "Kansas City, for trusting us with your homes and businesses. More "
               "to come — and Vince is still the one answering the phone."),
         hashtags=["#SmartByteKC", "#ThankYouKC", "#KansasCity", "#OneMonth"],
         cta="Here's to month two."),
]

# ---------------------------------------------------------------------------
# 4-WEEK THEME ARC (drives which week's content is published on which day)
# ---------------------------------------------------------------------------
WEEK_THEMES = {
    1: dict(theme="Residential", focus="No more Wi-Fi dead zones",
            post_type="Educational", tone="Warm, relatable"),
    2: dict(theme="Commercial",   focus="Infrastructure for scale",
            post_type="Authoritative", tone="Authoritative, outcome-focused"),
    3: dict(theme="Security",     focus="Peace of mind 24/7",
            post_type="Case Study", tone="Reassuring, tech-forward"),
    4: dict(theme="Local Trust",  focus="Why choose a KC expert",
            post_type="Humanizing", tone="Friendly, community-oriented"),
}

# Which content-bank index to use for a given platform on a given weekday.
# 6 drafts per week -> assign by weekday so each post type recurs evenly.
WEEKDAY_SLOT = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 0}


# ---------------------------------------------------------------------------
# GENERATION
# ---------------------------------------------------------------------------
def iso(d: date) -> str:
    return d.isoformat()


def week_of(d: date) -> int:
    """Week 1 == first 7 days from START_DATE, etc."""
    return ((d - START_DATE).days // 7) + 1


def build_entries() -> list[dict]:
    entries = []
    for day_offset in range(CALENDAR_DAYS):
        d = START_DATE + timedelta(days=day_offset)
        wk = min(week_of(d), 4)  # days 28-30 continue Week 4 (Local Trust) theme
        week_info = WEEK_THEMES[wk]
        slot = WEEKDAY_SLOT[d.weekday()]
        week_posts = [p for p in CONTENT_BANK if p["week"] == wk]
        # pick the post for this weekday slot (wrap if needed)
        post = week_posts[slot % len(week_posts)]

        for platform, rules in PLATFORM_RULES.items():
            if d.weekday() not in rules["schedule_days"]:
                continue
            entries.append(dict(
                date=iso(d),
                day=day_offset + 1,
                weekday=d.strftime("%a"),
                week=wk,
                theme=week_info["theme"],
                focus=week_info["focus"],
                post_type=week_info["post_type"],
                platform=platform,
                time=POSTING_TIMES[platform],
                post_id=post["id"],
                title=post["title"],
                topic=post["topic"],
                tone=post["tone"],
                copy=post["copy"],
                hashtags=post["hashtags"][: rules["hashtag_cap"]],
                cta=post["cta"],
                status="scheduled",
            ))
    return entries


def write_markdown(entries: list[dict], path: str) -> None:
    by_day: dict[int, list[dict]] = {}
    for e in entries:
        by_day.setdefault(e["day"], []).append(e)

    lines = ["# SmartByte Group, LLC — 30-Day Social Media Calendar", ""]
    lines.append(f"**Window:** {entries[0]['date']} → "
                 f"{entries[-1]['date']}  ")
    lines.append(f"**Platforms:** Instagram · Facebook · LinkedIn · Nextdoor  ")
    lines.append(f"**Posts scheduled:** {len(entries)}  ")
    lines.append("**Brand:** Smart Technology. Simplified. — Kansas City's "
                 "trusted tech neighbor.")
    lines.append("")
    lines.append("> Themed arc: **Wk1 Residential** → **Wk2 Commercial** → "
                 "**Wk3 Security** → **Wk4 Local Trust**")
    lines.append("")
    for day in sorted(by_day):
        day_entries = sorted(by_day[day], key=lambda x: x["time"])
        first = day_entries[0]
        lines.append(f"## Day {day} — {first['date']} ({first['weekday']}) "
                     f"· Week {first['week']}: {first['theme']}")
        lines.append(f"_{first['focus']} · {first['post_type']}_")
        lines.append("")
        for e in day_entries:
            lines.append(f"- **{e['time']} · {e['platform'].title()}** — "
                         f"{e['title']}  ")
            lines.append(f"  - Topic: {e['topic']} · Tone: {e['tone']}")
            lines.append(f"  - Copy: {e['copy']}")
            if e["hashtags"]:
                lines.append(f"  - Hashtags: {' '.join(e['hashtags'])}")
            lines.append(f"  - CTA: {e['cta']}")
            lines.append("")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def write_week_drafts(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    for wk in range(1, 5):
        posts = [p for p in CONTENT_BANK if p["week"] == wk]
        info = WEEK_THEMES[wk]
        lines = [f"# Week {wk} Drafts — {info['theme']}", ""]
        lines.append(f"**Focus:** {info['focus']}  ")
        lines.append(f"**Post type:** {info['post_type']}  ")
        lines.append(f"**Tone:** {info['tone']}  ")
        lines.append("")
        for p in posts:
            lines.append(f"## {p['title']}  ")
            lines.append(f"- **ID:** `{p['id']}`  ")
            lines.append(f"- **Topic:** {p['topic']}  ")
            lines.append(f"- **Tone:** {p['tone']}  ")
            lines.append(f"- **Copy:** {p['copy']}  ")
            lines.append(f"- **Hashtags:** {' '.join(p['hashtags'])}  ")
            lines.append(f"- **CTA:** {p['cta']}  ")
            lines.append("")
            lines.append("---")
            lines.append("")
        with open(os.path.join(path, f"week{wk}.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(lines))


def main() -> None:
    here = os.path.dirname(os.path.abspath(__file__))
    entries = build_entries()

    calendar = {
        "brand": "SmartByte Group, LLC",
        "tagline": "Smart Technology. Simplified.",
        "window_start": iso(START_DATE),
        "window_end": iso(START_DATE + timedelta(days=CALENDAR_DAYS - 1)),
        "platforms": list(PLATFORM_RULES.keys()),
        "posting_times": POSTING_TIMES,
        "generated_at": date.today().isoformat(),
        "posts": entries,
    }

    out_json = os.path.join(here, "calendar.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(calendar, f, indent=2, ensure_ascii=False)

    write_markdown(entries, os.path.join(here, "calendar.md"))
    write_week_drafts(os.path.join(here, "drafts"))

    # quick sanity counts
    per_platform = {}
    per_week = {}
    for e in entries:
        per_platform[e["platform"]] = per_platform.get(e["platform"], 0) + 1
        per_week[e["week"]] = per_week.get(e["week"], 0) + 1

    print(f"[ok] calendar.json  ({len(entries)} posts)")
    print(f"[ok] calendar.md    ({len(entries)} posts)")
    print(f"[ok] drafts/week1-4.md")
    print("Per platform:", per_platform)
    print("Per week:    ", per_week)


if __name__ == "__main__":
    main()
