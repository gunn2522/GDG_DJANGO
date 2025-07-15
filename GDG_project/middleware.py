from django.contrib.auth import get_user_model
from django.contrib.auth.models import AnonymousUser

class FakeLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        User = get_user_model()

        # Auto-create demo user if it doesn't exist
        demo_user, created = User.objects.get_or_create(
            username='demo',
            defaults={'email': 'demo@example.com'}
        )

        # Optionally set is_staff or permissions
        demo_user.is_staff = True
        demo_user.save()

        request.user = demo_user
        return self.get_response(request)
