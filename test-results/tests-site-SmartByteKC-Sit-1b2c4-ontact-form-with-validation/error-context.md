# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tests\site.spec.ts >> SmartByteKC Site Validation >> should have a working contact form with validation
- Location: tests\site.spec.ts:126:3

# Error details

```
Error: expect(page).toHaveURL(expected) failed

Expected pattern: /\/contact\//
Received string:  "http://localhost:4325/contact"
Timeout: 5000ms

Call log:
  - Expect "toHaveURL" with timeout 5000ms
    14 × locator resolved to <html lang="en" class="scroll-smooth">…</html>
       - unexpected value "http://localhost:4325/contact"

```

```yaml
- link "Skip to main content":
  - /url: "#main-content"
- banner:
  - link "SmartByteKC Home":
    - /url: /
    - img "SmartByteKC"
    - text: SmartByteKC
  - navigation "Primary":
    - link "Services":
      - /url: /services
- heading "Contact Us" [level=1]
- paragraph: Have a question or ready to start a project? We'd love to hear from you.
- text: Full Name *
- textbox "Full Name *"
- text: Email Address *
- textbox "Email Address *"
- text: Phone Number
- textbox "Phone Number"
- text: Service Interested In *
- combobox "Service Interested In *":
  - option "Select a service" [disabled] [selected]
  - option "Network Security"
  - option "Smart Home Automation"
  - option "Structured Cabling"
  - option "TV Mounting"
  - option "Home Theater"
  - option "Other"
- text: Message *
- textbox "Message *"
- button "Send Message"
- text: We use cookies to enhance your experience. By continuing to visit this site you agree to our use of cookies.
- button "Accept"
- button "Reject"
```

# Test source

```ts
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
  124 |   });
  125 | 
  126 |   test('should have a working contact form with validation', async ({ page }) => {
  127 |     await page.goto(baseURL + 'contact');
  128 |     await expect(page).toHaveTitle(/Contact SmartByteKC/);
  129 |     
  130 |     // Try to submit empty form
  131 |     await page.locator('button[type="submit"]').click();
  132 |     
  133 |     // Check that the form shows validation errors (we'll check that the name and email fields are invalid)
  134 |     const nameInput = page.locator('#name');
  135 |     const emailInput = page.locator('#email');
  136 |     // We expect the browser to show validation UI, but we can check if the fields are empty and required
  137 |     // Since we can't easily check for validation UI, we'll check that the form didn't submit (by checking we're still on the contact page)
> 138 |     await expect(page).toHaveURL(new RegExp(`/contact/`));
      |                        ^ Error: expect(page).toHaveURL(expected) failed
  139 |     
  140 |     // Fill in the form
  141 |     await nameInput.fill('John Doe');
  142 |     await emailInput.fill('john@example.com');
  143 |     await page.locator('#service').selectOption('network-security');
  144 |     await page.locator('#message').fill('This is a test message.');
  145 |     
  146 |     // We can't actually submit because there's no backend, but we can check that the button is enabled
  147 |     const submitBtn = page.locator('button[type="submit"]');
  148 |     await expect(submitBtn).toBeEnabled();
  149 |     
  150 |     // We'll just check that the form accepts the input (no error)
  151 |   });
  152 | 
  153 |   test('should have a custom 404 page', async ({ page }) => {
  154 |     await page.goto(baseURL + 'this-page-does-not-exist');
  155 |     await expect(page).toHaveTitle(/404|Not Found/);
  156 |     await expect(page.locator('text=Page Not Found')).toBeVisible();
  157 |     await expect(page.locator('text=Go to Homepage')).toBeVisible();
  158 |   });
  159 | });
```