import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

# Calculate base path to ensure Gunicorn resolves nested modules
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
sys.path.append(str(BASE_DIR.parent))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coffee_cpr.settings')

application = get_wsgi_application()
