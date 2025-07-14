from django.urls import path
from django.contrib.auth.views import LoginView
from .views import logout_view, user_list, profile_view

urlpatterns = [


    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", logout_view, name="logout"),
    path("list/", user_list, name="user_list"),
    path('profile/', profile_view, name='profile'),
]
