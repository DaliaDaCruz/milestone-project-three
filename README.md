# Coffee CPR - Espresso Machine Repair & Management System
## Coffee CPR

Coffee CPR is a full-stack Django web application designed for commercial coffee machine repair shops and coffee technical services and selling coffee in future. It enables clients to submit equipment service requests and allows technicians to track, update, and manage repair status in real time.

## Project Purpose 

* **Target Audience:** Espresso machine owners, cafe managers and commercial coffee technicians.
* **Problem Solved:** Simplifies service tracking by moving away from paper logs into a database system where users can submit and monitor repair statuses.
* **UX & Accessibility:** Built using Bootstrap 5, featuring accessible contrast ratios, responsive grids for mobile/desktop, and explicit visual cues for instant user feedback.

## Data Schema & Architecture

For the main webpage design I opted for a combination of colours that stand outwith the serviced offered. All browns and beige to represent coffee, the coffee foam and everything related. 
The letter chosen,Roboto (googleapis.com), brown and round to look like coffee beans, so the user feels or has the sense that every serviced offered or products sold are done by someone that knows the business.
Structured wise, I aseen several videos but one great tutorial about having all in just one page (index.html) it would be cleaner and less cahotic while adjusting the css styles, so gallery, contact, services and checkout are all under index page.
Favicon I used an online one as I though it looked better than the image I previousy had, which in the end use for the logo.
For the machines on the gallery section I used the pictures from a website I know (coffeepassion.co.uk) which is my brother in law company, the descriptions and key features of each machine I just used (google.com). The remaining pictures used throughout the pages where downloaded from (pixabay.com)

## Service and Gallery pages 

Used SQLite database scheme managed via Django ORM:

1. **Category Model**
   - `name` (CharField): Name of equipment category.
   - `slug` (SlugField): URL-friendly string identifier.

2. **Product Model**
   - `category` (ForeignKey -> Category): One-to-Many relationship.
   - `title` (CharField): Equipment name.
   - `price` (DecimalField): Item listing cost.
   - `condition` (CharField): Refurbished/New state.
   - `description` (TextField): Detailed item information.

3. **ServiceRequest Model**
   - `customer_name` (CharField): Requesting client's name.
   - `machine_model` (CharField): Coffee machine make/model.
   - `issue_description` (TextField): Breakdown details.
   - `status` (CharField): Progress state (Pending, In Repair, Completed).
   - `created_at` (DateTimeField): Auto-generated timestamp.

* All this process was used while doing the gallery/service page, so clients can easily book a service repair, buy a machine and proceed to checkout at ease.
---

## Security Features Considered

- **Environment Isolation:** Sensitive database configurations and secret keys are separated from tracked code via `.gitignore`.
- **CSRF Protection:** All forms include `{% csrf_token %}` tokens to prevent Cross-Site Request Forgery attacks.
- **SQL Injection Defense:** Database queries utilize Django's parameterized ORM abstraction layers.
- **Debug Configuration:** `DEBUG = False` for the live production deployments.

---

## Manual Testing & Verification 
All testing can be verified in the texting.md file.


## Deployment Procedures

1. Clone the repository: `git clone <repository-url>`
2. Install project dependencies: `pip install -r requirements.txt`
3. Execute database migrations: `python manage.py migrate`
4. Launch local development environment: `python manage.py runserver`
