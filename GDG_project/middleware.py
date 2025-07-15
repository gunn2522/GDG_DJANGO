# middleware.py
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

class FakeLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            from django.contrib.auth.middleware import get_user
            user = get_user(request)  # Avoids .user access before ready

            if not hasattr(request, 'user'):
                request.user = AnonymousUser()

            if request.user.is_authenticated:
                return self.get_response(request)

            User = get_user_model()
            demo_user = User.objects.filter(username='demo').first()
            if demo_user:
                request.user = demo_user
            else:
                request.user = AnonymousUser()

        except Exception as e:
            import logging
            logging.error(f"FakeLoginMiddleware Error: {e}")
            request.user = AnonymousUser()

        return self.get_response(request)
