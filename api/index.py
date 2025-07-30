# api/index.py

import os
import sys

# Add your Django project to the path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append('./GDG_project')

# Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDG_project.settings")
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Import Django's WSGI handler
from django.core.wsgi import get_wsgi_application

# Export `app` as expected by Vercel
app = get_wsgi_application()

