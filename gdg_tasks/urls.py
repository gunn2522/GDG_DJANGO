from django.urls import path
from . import views

urlpatterns = [
    path("assign/", views.assign_task, name="assign_task"),
    path("my-tasks/", views.my_tasks, name="my_tasks"),
    path("report-issue/", views.report_issue, name="report_issue"),
]
