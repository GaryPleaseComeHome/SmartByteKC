# Google Form: SmartByteKC Lead / Job Intake

**Create this at forms.google.com → Blank Form → Title: "SmartByteKC - New Job Request"**

---

## Form Settings
- **Collect email addresses:** ON (required)
- **Limit to 1 response:** OFF
- **Edit after submit:** ON
- **Confirmation message:** "Thanks! We'll review and contact you within 4 business hours."

---

## Form Fields (in order)

### Section 1: Contact Info
1. **Your Name** — Short answer — Required
2. **Company Name** — Short answer — Optional
3. **Email** — Short answer — Required (validated email)
4. **Phone** — Short answer — Required
5. **Service Address** — Paragraph — Required
   - *Help text: Street, City, State, ZIP*

### Section 2: Job Details
6. **What do you need help with?** — Multiple choice — Required
   - Break-fix / On-site repair
   - Managed services / Ongoing support
   - Project (install, migration, setup)
   - Hardware/software purchase
   - Other (specify)

7. **Describe the issue or project** — Paragraph — Required
   - *Help text: Be specific — equipment, symptoms, goals, timeline*

8. **Urgency** — Multiple choice — Required
   - Emergency (down, critical) — Same/next day
   - High — Within 2-3 business days
   - Standard — Within 1 week
   - Planning / Quote only — No rush

9. **Preferred contact method** — Checkboxes
   - Phone call
   - Email
   - Text/SMS

10. **Budget range (optional)** — Multiple choice
    - Under $500
    - $500 - $1,500
    - $1,500 - $5,000
    - $5,000+
    - Not sure / Need quote

### Section 3: For Existing Clients
11. **Are you an existing SmartByteKC client?** — Yes/No — Required
12. **If yes, your Client ID (if known)** — Short answer — Optional

---

## Form Responses → Google Sheet
- In Form: **Responses** tab → **Link to Sheets** → Create new spreadsheet: "SmartByteKC - Form Responses"
- This auto-creates a "Form Responses 1" tab

---

## Apps Script: Auto-create Job from Form Response
*(Add to the Form Responses spreadsheet → Extensions → Apps Script)*

```javascript
function onFormSubmit(e) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const jobsSheet = ss.getSheetByName('Jobs') || createJobsSheet(ss);
  const clientsSheet = ss.getSheetByName('Clients') || createClientsSheet(ss);
  
  // Map form columns (adjust indices to match your form)
  const timestamp = e.values[0];
  const name = e.values[1];
  const company = e.values[2];
  const email = e.values[3];
  const phone = e.values[4];
  const address = e.values[5];
  const serviceType = e.values[6];
  const description = e.values[7];
  const urgency = e.values[8];
  const contactMethod = e.values[9];
  const budget = e.values[10];
  const existingClient = e.values[11];
  const clientId = e.values[12];
  
  // Parse address
  const addrParts = parseAddress(address);
  
  // Find or create client
  let clientRow = findOrCreateClient(clientsSheet, clientId, company || name, name, email, phone, addrParts);
  
  // Create job
  const jobId = generateJobId(jobsSheet);
  const status = urgency.includes('Emergency') ? 'Scheduled' : 'Lead';
  const priority = urgency.includes('Emergency') ? 'Critical' : 
                   urgency.includes('High') ? 'High' : 'Medium';
  
  jobsSheet.appendRow([
    jobId,
    clientRow.clientId,
    serviceType + ' - ' + description.substring(0, 50),
    mapServiceLine(serviceType),
    description,
    status,
    priority,
    '', // Scheduled Date
    '', // Start Date
    '', // End Date
    '', // Estimated Hours
    '', // Actual Hours
    '', // Estimated Cost
    '', // Actual Cost
    '', // Quoted Amount
    '', // Invoiced Amount
    '', // Paid Amount
    '', // Assigned Tech
    'From web form: ' + contactMethod + '. Budget: ' + budget,
    timestamp,
    new Date()
  ]);
  
  // Notify owner (email)
  MailApp.sendEmail({
    to: 'you@yourdomain.com',
    subject: 'New Job Request: ' + jobId + ' - ' + (company || name),
    htmlBody: buildNotificationHtml(jobId, company || name, serviceType, description, urgency, email, phone)
  });
}

function parseAddress(addr) {
  // Simple parser - improve as needed
  const lines = addr.split('\n').map(l => l.trim()).filter(l => l);
  return {
    street: lines[0] || '',
    city: lines[1] || '',
    state: lines[2] || '',
    zip: lines[3] || ''
  };
}

function findOrCreateClient(sheet, clientId, company, contact, email, phone, addr) {
  if (clientId) {
    const data = sheet.getDataRange().getValues();
    for (let i = 1; i < data.length; i++) {
      if (data[i][0] === clientId) return {clientId, row: i+1};
    }
  }
  // Create new
  const newId = 'C-' + String(sheet.getLastRow()).padStart(3, '0');
  sheet.appendRow([newId, company, contact, email, phone, addr.street, addr.city, addr.state, addr.zip, mapServiceLine(company), 'Net 15', '', 'From web form', new Date(), 0, 0, '', '']);
  return {clientId: newId, row: sheet.getLastRow()};
}

function generateJobId(sheet) {
  return 'J-' + String(sheet.getLastRow()).padStart(3, '0');
}

function mapServiceLine(type) {
  const map = {
    'Break-fix / On-site repair': 'Break-Fix',
    'Managed services / Ongoing support': 'Managed Services',
    'Project (install, migration, setup)': 'Project',
    'Hardware/software purchase': 'Hardware/Software'
  };
  return map[type] || 'Break-Fix';
}

function createJobsSheet(ss) {
  const sheet = ss.insertSheet('Jobs');
  sheet.appendRow(['Job ID','Client ID','Job Title','Service Line','Description','Status','Priority','Scheduled Date','Start Date','End Date','Estimated Hours','Actual Hours','Estimated Cost','Actual Cost','Quoted Amount','Invoiced Amount','Paid Amount','Assigned Tech','Notes','Created Date','Updated Date']);
  return sheet;
}

function createClientsSheet(ss) {
  const sheet = ss.insertSheet('Clients');
  sheet.appendRow(['Client ID','Client Name','Contact Name','Email','Phone','Address','City','State','ZIP','Service Line Tendency','Payment Terms (Days)','Preferred Payment Method','Notes','Date Added','Total Revenue','Total Jobs','Last Job Date','Payment Habits']);
  return sheet;
}

function buildNotificationHtml(jobId, client, type, desc, urgency, email, phone) {
  return `<h2>New Job: ${jobId}</h2>
    <p><strong>Client:</strong> ${client}<br>
    <strong>Type:</strong> ${type}<br>
    <strong>Urgency:</strong> ${urgency}<br>
    <strong>Description:</strong> ${desc}<br>
    <strong>Contact:</strong> ${email} | ${phone}</p>
    <p><a href="${SpreadsheetApp.getActiveSpreadsheet().getUrl()}">Open in Sheets</a></p>`;
}
```

---

## After Setup
1. Test: Submit a test form entry
2. Verify: Job appears in "Jobs" tab with correct Client ID
3. Verify: Email notification arrives
4. Share form link with clients / put on website