from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import InfraIssue
from events.models import Event

@login_required
def report_issue(request):
    if request.method == "POST":
        location = request.POST["location"]
        issue_type = request.POST["issue_type"]
        description = request.POST["description"]
        event_id = request.POST.get("event")

        event = Event.objects.get(pk=event_id) if event_id else None

        InfraIssue.objects.create(
            reporter=request.user,
            location=location,
            issue_type=issue_type,
            description=description,
            event=event,
        )
        return redirect("my_reports")

    events = Event.objects.all()
    return render(request, "infra_issues/report_issue.html", {"events": events})


@login_required
def my_reports(request):
    issues = InfraIssue.objects.filter(reporter=request.user).order_by("-reported_at")
    return render(request, "my_reports.html", {"issues": issues})


@login_required
def infra_admin_panel(request):
    if request.user.role != "infra_head":
        return redirect("event_list")

    issues = InfraIssue.objects.all().order_by("status", "-reported_at")

    if request.method == "POST":
        issue_id = request.POST["issue_id"]
        new_status = request.POST["status"]

        issue = InfraIssue.objects.get(pk=issue_id)
        issue.status = new_status
        issue.save()
        return redirect("infra_admin_panel")

    return render(request, "infra_admin_panel.html", {"issues": issues})
