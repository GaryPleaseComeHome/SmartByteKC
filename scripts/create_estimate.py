#!/usr/bin/env python3
"""
SmartByte Group, LLC — Instant Client Estimate Generator
=========================================================
Generates branded HTML/PDF estimates for client quotes in 60 seconds.
"""
import sys
import os
import json
import datetime
import argparse

PRICING_PACKAGES = {
    "wifi-mesh": {
        "title": "Whole-Home Wi-Fi 6E Optimization & Mesh Deployment",
        "description": "Enterprise-grade mesh network, zero dead zones, VLAN setup, speed test audit.",
        "base_price": 499.00
    },
    "security-4k": {
        "title": "4-Camera 4K Security System & NVR Setup",
        "description": "4x 4K PoE IP cameras, local NVR, mobile app setup, clean line concealed wiring.",
        "base_price": 1299.00
    },
    "cabling-drop": {
        "title": "Structured Cat6 Data Cable Drop (Per Run)",
        "description": "Cat6 solid copper cabling, wall plate terminate, test & certification tag.",
        "base_price": 150.00
    },
    "tv-mount": {
        "title": "Concealed AV & TV Wall Mount Package",
        "description": "Heavy-duty tilt/full-motion mount, in-wall wire concealment, device hookup.",
        "base_price": 249.00
    }
}

def generate_html_estimate(client_name, client_email, client_phone, address, selected_items, notes=""):
    date_str = datetime.date.today().strftime("%B %d, %Y")
    est_num = f"SB-EST-{datetime.date.today().strftime('%Y%m%d')}-01"
    
    total = 0.0
    items_html = ""
    for item in selected_items:
        key = item.get("key")
        pkg = PRICING_PACKAGES.get(key, {})
        title = item.get("title") or pkg.get("title") or "Custom Service"
        desc = item.get("desc") or pkg.get("description") or ""
        rate = item.get("price") or pkg.get("base_price") or 0.0
        qty = item.get("qty", 1)
        subtotal = rate * qty
        total += subtotal
        items_html += f'''
        <tr>
          <td style="padding: 12px; border-bottom: 1px solid #1F2937;">
            <strong style="color: #F9FAFB;">{title}</strong><br>
            <span style="font-size: 12px; color: #9CA3AF;">{desc}</span>
          </td>
          <td style="padding: 12px; border-bottom: 1px solid #1F2937; text-align: center; color: #F9FAFB;">{qty}</td>
          <td style="padding: 12px; border-bottom: 1px solid #1F2937; text-align: right; color: #F9FAFB;">${rate:.2f}</td>
          <td style="padding: 12px; border-bottom: 1px solid #1F2937; text-align: right; font-weight: bold; color: #10B981;">${subtotal:.2f}</td>
        </tr>
        '''
        
    html = f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>Estimate {est_num} — SmartByte Group, LLC</title>
  <style>
    body {{ background-color: #0B0F19; color: #F9FAFB; font-family: -apple-system, sans-serif; padding: 40px; line-height: 1.6; }}
    .container {{ max-width: 750px; margin: 0 auto; background: #111827; border: 1px solid #1F2937; border-radius: 12px; padding: 32px; }}
    .header {{ display: flex; justify-content: space-between; border-bottom: 1px solid #1F2937; padding-bottom: 20px; margin-bottom: 24px; }}
    .brand {{ font-size: 22px; font-weight: bold; color: #10B981; letter-spacing: -0.5px; }}
    .subhead {{ font-size: 13px; color: #9CA3AF; }}
    .meta-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 24px; }}
    .box {{ background: #1F2937; padding: 16px; border-radius: 8px; font-size: 13px; }}
    table {{ width: 100%; border-collapse: collapse; margin-bottom: 24px; }}
    th {{ background: #1F2937; color: #9CA3AF; text-align: left; padding: 10px 12px; font-size: 12px; text-transform: uppercase; }}
    .total-box {{ text-align: right; font-size: 18px; font-weight: bold; padding: 16px; background: rgba(16, 185, 129, 0.1); border: 1px solid #10B981; border-radius: 8px; color: #10B981; }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div>
        <div class="brand">⚡ SmartByte Group, LLC</div>
        <div class="subhead">Smart Technology. Simplified.</div>
        <div class="subhead" style="margin-top:4px;">Vince@SmartByteKC.com • (816) 555-BYTE</div>
      </div>
      <div style="text-align: right;">
        <h2 style="margin:0; font-size: 20px; color:#F9FAFB;">ESTIMATE</h2>
        <div style="font-size:13px; color:#9CA3AF; margin-top:4px;">{est_num}</div>
        <div style="font-size:13px; color:#9CA3AF;">Date: {date_str}</div>
      </div>
    </div>

    <div class="meta-grid">
      <div class="box">
        <strong style="color:#10B981; font-size:12px; text-transform:uppercase;">Prepared For:</strong><br>
        <strong>{client_name}</strong><br>
        {address}<br>
        {client_email} | {client_phone}
      </div>
      <div class="box">
        <strong style="color:#10B981; font-size:12px; text-transform:uppercase;">Project Notes:</strong><br>
        {notes or "Low-voltage installation, testing, and full customer walkthrough included."}
      </div>
    </div>

    <table>
      <thead>
        <tr>
          <th>Description</th>
          <th style="text-align:center;">Qty</th>
          <th style="text-align:right;">Rate</th>
          <th style="text-align:right;">Amount</th>
        </tr>
      </thead>
      <tbody>
        {items_html}
      </tbody>
    </table>

    <div class="total-box">
      Estimated Total: ${total:.2f}
    </div>
    
    <div style="margin-top: 30px; font-size: 12px; color: #9CA3AF; text-align: center; border-top: 1px solid #1F2937; padding-top: 16px;">
      Estimate valid for 30 days. High-voltage electrical subcontracted separately if required.
    </div>
  </div>
</body>
</html>
'''
    return html

if __name__ == "__main__":
    sample_html = generate_html_estimate(
        client_name="Overland Park Residential Client",
        client_email="client@example.com",
        client_phone="(913) 555-0199",
        address="12345 Metcalf Ave, Overland Park, KS 66213",
        selected_items=[
            {"key": "wifi-mesh", "qty": 1},
            {"key": "cabling-drop", "qty": 3},
            {"key": "tv-mount", "qty": 1}
        ],
        notes="Whole-home Wi-Fi optimization plus 3 Cat6 hardline ethernet drops for home office & living room TV."
    )
    out_path = "C:/Users/Gibby/smartbytekc/docs/Sample_Client_Estimate.html"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sample_html)
    print(f"Generated sample client estimate at {out_path}!")
