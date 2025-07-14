from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import PerformanceRecord
from users.models import User
from gdg_tasks.models import Task
from infra_issues.models import InfraIssue
from events.models import Event

@login_required
def my_performance(request):
    record, created = PerformanceRecord.objects.get_or_create(user=request.user)

    return render(request, "performance/my_performance.html", {"record": record})


@login_required
def admin_dashboard(request):
    if request.user.role != "faculty":
        return redirect("my_performance")

    users = User.objects.filter(role="gdg_member")
    records = []

    for user in users:
        tasks = Task.objects.filter(assigned_to=user, is_completed=True).count()
        issues = InfraIssue.objects.filter(reporter=user).count()
        events_led = Event.objects.filter(organizer=user).count()

        total = (tasks * 2) + (issues * 1) + (events_led * 3)

        record, _ = PerformanceRecord.objects.get_or_create(user=user)
        record.tasks_completed = tasks
        record.issues_reported = issues
        record.events_led = events_led
        record.total_score = total
        record.save()

        records.append(record)

    return render(request, "performance/admin_dashboard.html", {"records": records})
