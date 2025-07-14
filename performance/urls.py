from django.urls import path
from . import views

urlpatterns = [
    path("my-score/", views.my_performance, name="my_performance"),
    path("admin-eval/", views.admin_dashboard, name="admin_performance"),
]
