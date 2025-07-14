from django.urls import path
from .views import dashboard_view, approval_dashboard_view

urlpatterns = [
    path('/dashboard_view/', dashboard_view, name='dashboard'),

    path("dashboard/approval_dashboard/", approval_dashboard_view, name="approval_dashboard"),


]
