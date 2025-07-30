import os
import sys

from django.core.wsgi import get_wsgi_application

# Add your project root to the sys path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "GDG_project.settings")

# Allow unsafe async for serverless
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# Export the app that Vercel looks for
app = get_wsgi_application()
