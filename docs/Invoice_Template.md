# SmartByteKC Invoice Template

**Copy this into a Google Doc and save as "Invoice Template"**

---

## HEADER SECTION (Table: 2 columns)

| | |
|---|---|
| **SmartByteKC** | **INVOICE** |
| 123 Tech Drive | Invoice #: `{{INVOICE_NUMBER}}` |
| Kansas City, MO 64101 | Date Issued: `{{DATE_ISSUED}}` |
| Phone: (555) 000-0000 | Due Date: `{{DUE_DATE}}` |
| Email: billing@smartbytekc.com | Status: `{{STATUS}}` |
| Website: smartbytekc.com | |

---

## BILL TO SECTION

**Bill To:**
`{{CLIENT_NAME}}`
`{{CONTACT_NAME}}`
`{{ADDRESS}}`
`{{CITY}}, {{STATE}} {{ZIP}}`
`{{EMAIL}}`
`{{PHONE}}`

---

## JOB DETAILS

**Job:** `{{JOB_TITLE}}` (`{{JOB_ID}}`)
**Service Line:** `{{SERVICE_LINE}}`
**Billing Method:** `{{BILLING_METHOD}}`

---

## LINE ITEMS TABLE

| # | Description | Qty | Unit Price | Line Total | Taxable |
|---|-------------|-----|------------|------------|---------|
`{{LINE_ITEMS_ROWS}}`

---

## TOTALS SECTION (Right-aligned)

| | |
|---|---|
| **Subtotal:** | `$ {{SUBTOTAL}}` |
| **Tax ({{TAX_RATE}}%):** | `$ {{TAX_AMOUNT}}` |
| | **----------** |
| **TOTAL:** | **$ {{TOTAL_AMOUNT}}** |
| **Amount Paid:** | `$ {{AMOUNT_PAID}}` |
| **Balance Due:** | **$ {{BALANCE_DUE}}** |

---

## PAYMENT TERMS & NOTES

**Payment Terms:** Net `{{PAYMENT_TERMS}}` days
**Due Date:** `{{DUE_DATE}}`

**Accepted Payment Methods:**
- Check payable to: SmartByteKC
- Bank Transfer (ACH): [Your routing/account details]
- Credit Card: [Link to payment portal or "Call to pay"]

**Notes:**
`{{NOTES}}`

---

## FOOTER

Thank you for your business!

SmartByteKC | 123 Tech Drive, Kansas City, MO 64101 | billing@smartbytekc.com