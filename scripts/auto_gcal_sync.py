#!/usr/bin/env python3
"""
SmartByte Group, LLC — Batch Google Calendar Campaign Sync
"""
import os
import json
import datetime
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(HERE)
CALENDAR_PATH = os.path.join(PROJECT_ROOT, "social", "approved_queue.json")
if not os.path.exists(CALENDAR_PATH):
    CALENDAR_PATH = os.path.join(PROJECT_ROOT, "social", "calendar.json")

def sync_campaign():
    if not os.path.exists(CALENDAR_PATH):
        print(f"Calendar not found at {CALENDAR_PATH}")
        return

    with open(CALENDAR_PATH, "r", encoding="utf-8") as f:
        cal = json.load(f)

    posts = cal.get("posts", [])
    print(f"Found {len(posts)} campaign items to sync to Google Calendar.")

    # Check token file
    token_file = os.path.join(HERE, "token.json")
    if not os.path.exists(token_file):
        print("Note: token.json not found yet. OAuth authentication prompt will fire when gcal_sync is run interactively.")
    else:
        print("OAuth token found. Ready for batch calendar sync.")

if __name__ == "__main__":
    sync_campaign()
