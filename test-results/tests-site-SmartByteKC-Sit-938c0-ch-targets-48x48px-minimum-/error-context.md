# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tests\site.spec.ts >> SmartByteKC Site Validation >> should have accessible touch targets (48x48px minimum)
- Location: tests\site.spec.ts:17:3

# Error details

```
Error: expect(received).toBeGreaterThanOrEqual(expected)

Expected: >= 48
Received:    18
```

# Page snapshot

```yaml
- generic [active] [ref=f1e1]:
  - link "Skip to main content" [ref=f1e2] [cursor=pointer]:
    - /url: "#main-content"
  - banner [ref=f1e3]:
    - link "SmartByteKC Home" [ref=f1e5] [cursor=pointer]:
      - /url: /
      - img "SmartByteKC" [ref=f1e7]
      - generic [ref=f1e8]: SmartByteKC
    - navigation "Primary" [ref=f1e10]:
      - link "Services" [ref=f1e11] [cursor=pointer]:
        - /url: /services
  - main [ref=f1e12]:
    - generic [ref=f1e13]:
      - heading "Kansas City IT & Low-Voltage Experts." [level=1] [ref=f1e14]
      - paragraph [ref=f1e15]: We provide reliable network security, smart home automation, and professional structured cabling services across the KC metro area.
      - link "Request Consultation" [ref=f1e16] [cursor=pointer]:
        - /url: /contact
    - generic [ref=f1e17]:
      - heading "Our Services" [level=2] [ref=f1e18]
      - generic [ref=f1e19]:
        - link [ref=f1e20] [cursor=pointer]:
          - /url: /services/network-security
          - heading "Network Security" [level=3] [ref=f1e21]
          - paragraph [ref=f1e22]: Enterprise-grade firewalls, intrusion detection, and 24/7 monitoring to keep your business safe from cyber threats.
        - link [ref=f1e23] [cursor=pointer]:
          - /url: /services/smart-home
          - heading "Smart Home Automation" [level=3] [ref=f1e24]
          - paragraph [ref=f1e25]: Custom lighting, climate control, and entertainment systems that make your home more comfortable and efficient.
        - link [ref=f1e26] [cursor=pointer]:
          - /url: /services/cabling
          - heading "Structured Cabling" [level=3] [ref=f1e27]
          - paragraph [ref=f1e28]: Professional Cat6 and fiber optic installation for reliable, high-speed data and voice communications.
    - generic [ref=f1e29]:
      - heading "Why SmartByteKC?" [level=2] [ref=f1e30]
      - generic [ref=f1e31]:
        - generic [ref=f1e32]:
          - heading "Locally Owned & Operated" [level=3] [ref=f1e33]
          - paragraph [ref=f1e34]: We're proud to serve the Kansas City community with personalized service and quick response times.
        - generic [ref=f1e35]:
          - heading "Licensed & Insured" [level=3] [ref=f1e36]
          - paragraph [ref=f1e37]: Fully licensed low-voltage contractor with comprehensive liability insurance for your protection.
        - generic [ref=f1e38]:
          - heading "24/7 Emergency Support" [level=3] [ref=f1e39]
          - paragraph [ref=f1e40]: We're available around the clock for critical technology emergencies that impact your business operations.
        - generic [ref=f1e41]:
          - heading "Transparent Pricing" [level=3] [ref=f1e42]
          - paragraph [ref=f1e43]: Clear, upfront pricing with no hidden fees. We provide detailed quotes before any work begins.
    - generic [ref=f1e44]:
      - heading "Ready to Upgrade Your Technology?" [level=2] [ref=f1e45]
      - paragraph [ref=f1e46]: Get a free consultation and site assessment from our experts.
      - link "Schedule Free Consultation" [ref=f1e47] [cursor=pointer]:
        - /url: /contact
  - generic [ref=f1e49]:
    - generic [ref=f1e50]: We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.
    - generic [ref=f1e51]:
      - button "Accept" [ref=f1e52] [cursor=pointer]
      - button "Reject" [ref=f1e53] [cursor=pointer]
```

# Test source

```ts
  1   | import { test, expect } from '@playwright/test';
  2   | 
  3   | const baseURL = process.env.BASE_URL || 'http://localhost:4325/';
  4   | 
  5   | test.describe('SmartByteKC Site Validation', () => {
  6   |   test.beforeEach(async ({ page }) => {
  7   |     await page.goto(baseURL);
  8   |     // Clear cookies for each test to see the banner
  9   |     await page.context().clearCookies();
  10  |     await page.reload();
  11  |   });
  12  | 
  13  |   test('should load successfully', async ({ page }) => {
  14  |     await expect(page).toHaveTitle(/SmartByteKC/);
  15  |   });
  16  | 
  17  |   test('should have accessible touch targets (48x48px minimum)', async ({ page }) => {
  18  |     const clickableElements = page.locator('a, button, [role="button"], input[type="submit"], input[type="button"]');
  19  |     const count = await clickableElements.count();
  20  |     
  21  |     for (let i = 0; i < count; i++) {
  22  |       const box = await clickableElements.nth(i).boundingBox();
> 23  |       expect(box.width).toBeGreaterThanOrEqual(48);
      |                         ^ Error: expect(received).toBeGreaterThanOrEqual(expected)
  24  |       expect(box.height).toBeGreaterThanOrEqual(48);
  25  |     }
  26  |   });
  27  | 
  28  |   test('should be mobile responsive at 375px width', async ({ page }) => {
  29  |     await page.setViewportSize({ width: 375, height: 667 });
  30  |     await page.goto(baseURL);
  31  |     
  32  |     // Check that no horizontal overflow occurs
  33  |     const hasHorizontalOverflow = await page.evaluate(() => {
  34  |       return document.body.scrollWidth > document.documentElement.clientWidth;
  35  |     });
  36  |     expect(hasHorizontalOverflow).toBe(false);
  37  |   });
  38  | 
  39  |   test('should have no console errors', async ({ page }) => {
  40  |     const errors = [];
  41  |     page.on('console', msg => {
  42  |       if (msg.type() === 'error') {
  43  |         errors.push(msg.text());
  44  |       }
  45  |     });
  46  |     
  47  |     await page.goto(baseURL);
  48  |     await page.waitForLoadState('networkidle');
  49  |     expect(errors).toHaveLength(0);
  50  |   });
  51  | 
  52  |   test('should have proper heading hierarchy', async ({ page }) => {
  53  |     await page.goto(baseURL);
  54  |     
  55  |     // Check for exactly one H1
  56  |     const h1Count = await page.locator('h1').count();
  57  |     expect(h1Count).toBe(1);
  58  |     
  59  |     // Check that we have headings in order (we'll just check that we have at least one of each expected)
  60  |     const h2Count = await page.locator('h2').count();
  61  |     expect(h2Count).toBeGreaterThan(0);
  62  |   });
  63  | 
  64  |   test('should have descriptive alt text for images', async ({ page }) => {
  65  |     await page.goto(baseURL);
  66  |     const images = await page.locator('img').all();
  67  |     
  68  |     for (const img of images) {
  69  |       const alt = await img.getAttribute('alt');
  70  |       expect(alt).toBeTruthy();
  71  |       expect(alt.length).toBeGreaterThan(0);
  72  |     }
  73  |   });
  74  | 
  75  |   test('should have sufficient color contrast (AAA) - simplified check', async ({ page }) => {
  76  |     await page.goto(baseURL);
  77  |     // We'll check that we are not using red for important information (as a proxy)
  78  |     const hasOnlyDecorativeColors = await page.evaluate(() => {
  79  |       const redElements = document.querySelectorAll('[style*="color: red"], [style*="color:#f00"], [style*="color: #f00"]');
  80  |       return redElements.length === 0;
  81  |     });
  82  |     expect(hasOnlyDecorativeColors).toBe(true);
  83  |   });
  84  | 
  85  |   test('should have a skip link', async ({ page }) => {
  86  |     await page.goto(baseURL);
  87  |     const skipLink = page.locator('.skip-link');
  88  |     expect(await skipLink.isVisible()).toBe(false); // Should be hidden by default
  89  |     await skipLink.focus();
  90  |     expect(await skipLink.isVisible()).toBe(true); // Should be visible on focus
  91  |   });
  92  | 
  93  |   test('should have skip link pointing to main content', async ({ page }) => {
  94  |     await page.goto(baseURL);
  95  |     const skipLink = page.locator('.skip-link');
  96  |     const href = await skipLink.getAttribute('href');
  97  |     expect(href).toBe('#main-content');
  98  |     
  99  |     // Check that there is an element with id="main-content"
  100 |     const mainContent = page.locator('#main-content');
  101 |     expect(await mainContent.isVisible()).toBe(true);
  102 |   });
  103 | 
  104 |   test('should show cookie consent banner on first visit', async ({ page }) => {
  105 |     await page.goto(baseURL);
  106 |     const banner = page.locator('#cookie-banner');
  107 |     expect(await banner.isVisible()).toBe(true);
  108 |   });
  109 | 
  110 |   test('should hide cookie consent banner after accepting', async ({ page }) => {
  111 |     await page.goto(baseURL);
  112 |     const banner = page.locator('#cookie-banner');
  113 |     const acceptBtn = page.locator('#accept-cookies');
  114 |     await acceptBtn.click();
  115 |     expect(await banner.isVisible()).toBe(false);
  116 |   });
  117 | 
  118 |   test('should hide cookie consent banner after rejecting', async ({ page }) => {
  119 |     await page.goto(baseURL);
  120 |     const banner = page.locator('#cookie-banner');
  121 |     const rejectBtn = page.locator('#reject-cookies');
  122 |     await rejectBtn.click();
  123 |     expect(await banner.isVisible()).toBe(false);
```