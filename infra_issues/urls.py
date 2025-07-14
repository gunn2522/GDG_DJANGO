from django.urls import path
from . import views

urlpatterns = [
    path("report/", views.report_issue, name="infra_report"),
    path("my-reports/", views.my_reports, name="my_reports"),
    path("admin-panel/", views.infra_admin_panel, name="infra_admin_panel"),
]
