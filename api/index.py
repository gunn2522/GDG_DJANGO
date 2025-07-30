# api/index.py

import os
import sys

# Ensure the app root is in the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('./GDG_project')

# Set environment variable to your Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDG_project.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

from django.core.wsgi import get_wsgi_application

# Vercel uses this as the entry point
app = get_wsgi_application()
