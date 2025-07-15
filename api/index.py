# api/index.py
from django.core.wsgi import get_wsgi_application
import os
import sys

# Add your project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set environment variable for settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDG_project.settings")

# Get the WSGI app
app = get_wsgi_application()

