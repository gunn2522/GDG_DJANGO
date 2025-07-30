# api/index.py

import os
import sys

# Add the Django project directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('./GDG_project')

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDG_project.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Load WSGI application
from django.core.wsgi import get_wsgi_application

# Vercel looks for "app" or "handler"
app = get_wsgi_application()
