# middleware/auto_login.py
from django.contrib.auth import login
from django.contrib.auth import get_user_model

from dashboard.views import User


class AutoLoginAsDemoUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            try:
                demo_user = User.objects.get(username='demo')  # Or use email/ID if needed
                login(request, demo_user)
            except User.DoesNotExist:
                pass  # Optionally, create the demo user here

        return self.get_response(request)
