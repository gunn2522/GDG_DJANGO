# middleware.py
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

class FakeLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        User = get_user_model()

        try:
            demo_user = User.objects.get(username='demo')  # or any existing username
            request.user = demo_user
        except User.DoesNotExist:
            request.user = AnonymousUser()  # fallback if demo user not found

        return self.get_response(request)
