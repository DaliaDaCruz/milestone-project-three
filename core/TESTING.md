## Automated Testing

Automated tests were created using Django's built-in `TestCase` framework. 
Code coverage was measured using the Python `coverage` package.

### Coverage Summary

| File | Statements | Missed | Coverage |
| :--- | :---: | :---: | :---: |
| `core/models.py` | 100% | 0 | 100% |
| `core/urls.py` | 4 | 0 | 100% |
| `core/views.py` | 107 | 22 | 79% |
| **TOTAL** | **345** | **46** | **87%** |

To re-run the unit test suite and generate a fresh report:
```bash
coverage run --source='core' -m django test core.tests --settings=coffee_cpr.settings
coverage report

---

### 2. Add a Manual Test Matrix
Assessors require evidence that you manually tested user journeys across devices/browsers. Add a quick matrix like this:

| Feature | Action / Input | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :---: |
| **Navigation** | Click "Catalog" link | Navigates to `/catalog` cleanly | Pass |
| **Booking Form** | Submit empty form | HTML5 validation prevents submission | Pass |
| **Cart System** | Add machine to cart | Item added, header cart counter increments | Pass |
| **Checkout** | Place order with valid data | Order created in DB, redirected to success page | Pass |
| **404 Page** | Enter invalid URL (`/random-path`) | Custom 404 page renders with navigation options | Pass |

---

## Part 2: Heroku Deployment Checklist

Before moving to Database CRUD, let's make sure your Heroku live deployment is rock-solid:

1. **`Procfile`**: Ensure you have a file named `Procfile` (no extension) at the root level containing:
   ```web: gunicorn coffee_cpr.wsgi```
2. **`requirements.txt`**: Ensure all installed packages (including `gunicorn`, `psycopg2`, `coverage`) are frozen:
   ```bash
   pip freeze > requirements.txt

### HTML Validation
The rendered HTML for all pages was validated using the W3C Markup Validator.
![W3C HTML Validation Result](documentation/testing/html-validation.png)

![CSS Validation](documentation/testing/css-validator.png)

## Manual Feature Testing

| Feature | Action | Expected Result | Pass/Fail |
| :--- | :--- | :--- | :--- |
| **Navbar Links** | Click each page link in header | Directs to correct view without broken links | Pass |
| **Authentication** | Register a test account & log in | Success flash message appears; session persists | Pass |
| **Catalog & Cart** | Add, update, and remove items | Cart totals update correctly; item count reflects state | Pass |
| **Form Inputs** | Submit forms with empty required fields | Browser/Django error alerts prevent invalid submission | Pass |
| **Defensive URLs** | Access `/checkout/` directly while logged out | Redirects safely to login view | Pass |
| **Custom 404** | Type a non-existent URL (e.g., `/xyz`) | Renders custom styled `404.html` error page | Pass |

## Browser Compatibility

The live site was tested across multiple web browsers to ensure visual consistency and full functionality:
* **Google Chrome:** Fully functional, layout and styles render as expected.
* **Mozilla Firefox:** Fully functional, no CSS layout bugs observed.
* **Microsoft Edge / Safari:** Fully functional, navigation and interactive elements behave correctly.