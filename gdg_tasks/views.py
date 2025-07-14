from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Task, IssueReport
from events.models import Event
from users.models import User


@login_required
def assign_task(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        role = request.POST['role']
        user_id = request.POST['assigned_to']
        event_id = request.POST['event']

        Task.objects.create(
            title=title,
            description=description,
            role=role,
            assigned_to=User.objects.get(pk=user_id),
            event=Event.objects.get(pk=event_id),
        )
        return redirect("assign_task")

    users = User.objects.filter(role="gdg_member")
    events = Event.objects.all()
    return render(request, "assign_task.html", {"users": users, "events": events})


@login_required
def my_tasks(request):
    tasks = Task.objects.filter(assigned_to=request.user)

    if request.method == "POST":
        task_id = request.POST['task_id']
        task = Task.objects.get(pk=task_id, assigned_to=request.user)
        task.is_completed = True
        task.save()
        return redirect("my_tasks")

    return render(request, "my_tasks.html", {"tasks": tasks})


@login_required
def report_issue(request):
    if request.method == "POST":
        event_id = request.POST['event']
        issue = request.POST['issue']
        IssueReport.objects.create(
            event=Event.objects.get(pk=event_id),
            reported_by=request.user,
            issue=issue
        )
        return redirect("report_issue")

    events = Event.objects.all()
    return render(request, "report_issue.html", {"events": events})
