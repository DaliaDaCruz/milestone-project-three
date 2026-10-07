# Coffee CPR - Testing & Validation Log 🧪

## 1. Code Validation Evidence

### HTML Validation
All HTML templates were run through the W3C Markup Validation Service to ensure standard compliance, clean syntax, and proper element nesting.
![Index.html testing](image.png)

### CSS Validation
Custom styles and Tailwind configurations were validated to confirm syntax error-free rendering across browsers.
![CSS testing](image-1.png)

---

## 2. Functional & Manual Testing Log

| Feature / Page | Test Action | Expected Result | Pass / Fail |
| :--- | :--- | :--- | :--- |
| **Homepage Navigation** | Click "Proceed to Checkout" | Redirects cleanly to `/checkout/` without Nginx/404 errors | PASS |
| **Homepage Navigation** | Click "Submit Repair Request" | Navigates to repair request form at `/request/new/` | PASS |
| **Checkout Flow** | Enter promo code `BARISTA10` | Applies 10% discount and recalculates grand total | PASS |
| **Checkout Form Switch** | Toggle between Card & Bank Transfer | Updates active tab UI and dynamically toggles input requirements | PASS |
| **Checkout Completion** | Submit checkout form | Displays processing indicator and opens order confirmation modal | PASS |
| **CRUD: Create Ticket** | Submit new ticket form | Saves record to database and redirects to ticket list | PASS |
| **CRUD: Read Ticket** | View homepage list | Displays active repair tickets dynamically from database | PASS |
| **Responsive Design** | Test on Mobile, Tablet & Desktop | Layout adjusts smoothly with proper contrast ratios | PASS |

---

## 3. Security & Environment Checks

- **CSRF Tokens:** Verified that all forms include `{% csrf_token %}`.
- **Environment Isolation:** Ensured `.gitignore` excludes local database files (`db.sqlite3`), secret keys, and virtual environments.
- **Broken Link Check:** Confirmed all template links (`{% url 'request_list' %}`) navigate properly without dead links.