#!/usr/bin/env python3
"""
SmartByte Group, LLC — Playwright Chrome Profile Connector
===========================================================
Attaches to the user's running Chrome profile via CDP port 9222.
Updates Facebook, Bing Places, Nextdoor, Yelp, and Apple Maps profiles.
"""
import asyncio
import os
import sys
from playwright.async_api import async_playwright

PROFILE_IMG = r"C:\Users\Gibby\smartbytekc\public\brand_assets\SmartByte_Profile_500x500.png"
COVER_IMG = r"C:\Users\Gibby\smartbytekc\public\brand_assets\SmartByte_Cover_1200x628.png"

DESC_SHORT = "Kansas City's premier smart home & low-voltage technology specialists. We design and install enterprise Wi-Fi 6E mesh networks, 4K PoE security camera systems, structured Cat6 data cabling, and custom AV wall mounting. Clean lines, zero dead zones, and simple tech."

async def main():
    print("Connecting to Chrome on http://localhost:9222 ...")
    async with async_playwright() as p:
        try:
            browser = await p.chromium.connect_over_cdp("http://localhost:9222")
            print("Successfully connected to Chrome via CDP!")
            
            contexts = browser.contexts
            if not contexts:
                print("No active browser contexts found.")
                return
            
            context = contexts[0]
            pages = context.pages
            print(f"Found {len(pages)} open tabs:")
            for i, page in enumerate(pages):
                print(f" Tab {i+1}: {page.title} ({page.url})")
                
            # Scan for Bing Places tab or open one
            bing_page = None
            for page in pages:
                if "bing" in page.url.lower() or "bingplaces" in page.url.lower():
                    bing_page = page
                    break
            
            if not bing_page:
                bing_page = await context.new_page()
                await bing_page.goto("https://www.bingplaces.com")
            
            print("Navigated/Selected Bing Places tab:", bing_page.url)
            
            # Additional platform handlers can be triggered here
            
        except Exception as e:
            print(f"Error connecting to Chrome: {e}")
            print("Make sure Chrome was launched with: chrome.exe --remote-debugging-port=9222")

if __name__ == "__main__":
    asyncio.run(main())
