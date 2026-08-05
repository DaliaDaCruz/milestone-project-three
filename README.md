# milestone-project-three

## Testing
Please refer to the [TESTING.md](TESTING.md) file for all unit testing, automated coverage reports, and manual testing documentation.

#Coffee CPR
##Giving coffee machines a second shot!

Coffee CPR is a full-stack e-commerce and service platform built with Django, designed for coffee machine repairs, servicing, and commercial coffee equipment sales. Born out of the morning rush and high demand for reliable espresso setups in London, this web application connects coffee shop owners and enthusiasts with professional machine repair services and authentic Italian coffee equipment.

# Page Links & Live Deployment
Live Site (Heroku): [Insert your Heroku app URL here]

# GitHub Repository: [Insert your GitHub repository link here]

# Table of Contents
## Design
 - Colour Scheme
 - Typography
 - Imagery & Icons
 - Features
    - Current Features
    - Future Features

- Technologies Used
- Languages
- Frameworks, Libraries & Tools
- Testing
- Deployment
    - Heroku Deployment

- Local Cloning & Setup
- Credits & Acknowledgements

# Design
Colour Scheme
Primary Theme: #2b1e16 (Rich Coffee Bean Brown) for navigation, footers, and primary brand accents.

Secondary Accents: #f8f9fa (Off-white/Cream text) for high contrast and readability.

Hover Accent: #e6ccb2 / Warm brown accents for interactive links and buttons.

# Typography
Primary Font: Google Fonts (Comic Relief / Sans-Serif) to provide an approachable, clean aesthetic across all devices.

# Imagery & Icons
Backgrounds & Product Images: Sourced from Pixabay and custom assets stored under /static/core/img/.

Icons: Line Awesome and Font Awesome for contact info, navigation, and service features.

# Features
## Current Features
Navigation & Footer: Fully responsive Bootstrap navbar styled with custom CSS (.navbar-coffee, .bg-coffee). Includes collapsible mobile view and brand logos.

Hero Section: Dynamic hero banner (.hero-section) featuring centered overlay text and a circular layered accent (.circle-bg-accent).

Services & Quote Requests: Itemized repair/servicing offerings complete with description cards and interactive quote request forms.

Product Catalog: Showcase of commercial Italian coffee machines, formatted with structured Django models and uniform card layouts (.card-img-top).

Contact & Inquiries: Responsive message form alongside company contact details and London location info.

Custom Error Handling: Styled 404.html and 500.html pages for seamless user error handling.

## Future Features
Integration of online payment processing (Stripe API) for direct basket checkout.

Partnering with Italian bean distributors to offer subscription coffee bags.

Booking calendar integration for live repair scheduling and technician dispatch.

# Technologies Used
Languages
HTML5: Semantic markup structure.

CSS3: Custom styles, Flexbox layout, media queries, and absolute asset pathing.

JavaScript: Interactive UI enhancements and form handling.

Python: Core backend business logic and database management via Django.

Frameworks, Libraries & Tools
Django (v4+): Python Web Framework handling MVC architecture, ORM database models, and administration.

Bootstrap: Responsive layout framework and UI components.

Gunicorn: WSGI HTTP Server for production deployment on Heroku.

WhiteNoise: Efficient static file serving (/staticfiles/) for production environments.

Git & GitHub: Version control and source code repository management.

Heroku: Cloud platform for live application hosting and PostgreSQL database management.

# Deployment
Heroku Deployment
This project is deployed live on Heroku. The deployment steps followed were:

Created a Procfile declaring the web process: web: gunicorn core.wsgi:application --pythonpath core.

Configured WhiteNoiseMiddleware in settings.py and set STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles').

Created a requirements.txt file using pip freeze > requirements.txt.

Connected the GitHub repository to Heroku and deployed the main branch.

Executed remote migrations: heroku run python manage.py migrate.

Created an administrative user: heroku run python manage.py createsuperuser.

Local Setup
Clone the repository:

Bash
git clone https://github.com/your-username/milestone-project-three.git
Create and activate a virtual environment:

Bash
python3 -m venv .venv
source .venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Run migrations and start the local development server:

Bash
python manage.py migrate
python manage.py runserver

# Credits & Acknowledgements
Code: Custom CSS path resolution and Django configuration structured with assistance from Code Institute materials and documentation.

Media: Stock coffee imagery provided by Pixabay.

Educational Disclaimer: All company names and branding elements used in this project are for educational and portfolio demonstration purposes only.