from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from users.models import User
from events.models import Event, EventRegistration
from gdg_tasks.models import Task
from infra_issues.models import InfraIssue
from performance.models import PerformanceRecord
from attendence.models import Attendance
from django.contrib.auth.decorators import login_required



def dashboard_view(request):
    user = request.user
    context = {}

    # Allow access if user is authenticated or demo
    # if not user.is_authenticated and not getattr(request, 'is_demo', False):
    #     return redirect('login')

    # Block non-admins who are not demo
    if not user.is_superuser and not getattr(request, 'is_demo', False):
        return HttpResponseForbidden("Not allowed")

    # Common dashboard for demo or unauthenticated view
    if not user.is_authenticated:
        context["common"] = True
        return render(request, "dashboard.html", context)

    # Role-based context
    if user.role == "student":
        context["upcoming_events"] = Event.objects.all().order_by('date')[:5]
        context["my_registrations"] = EventRegistration.objects.filter(student=user)
        context["is_blocked"] = user.is_blocked

    elif user.role == "gdg_member":
        context["assigned_tasks"] = Task.objects.filter(assigned_to=user)
        context["my_performance"] = PerformanceRecord.objects.filter(member=user)

    elif user.role == "event_head":
        context["events_created"] = Event.objects.filter(created_by=user)
        context["approval_pending"] = EventRegistration.objects.filter(is_approved_by_event_head=False)
        context["all_users"] = User.objects.all()
        context["attendance_records"] = Attendance.objects.all()

    elif user.role == "hod":
        context["events_to_approve"] = Event.objects.filter(is_venue_approved_by_hod=False)
        context["unblock_requests"] = User.objects.filter(is_blocked=True, hod_approved=False)

    elif user.role == "teacher":
        context["attendance_to_review"] = Attendance.objects.filter(reviewed_by_head=True, sent_to_teacher=False)

    return render(request, "dashboard.html", context)



@login_required
def approval_dashboard_view(request):
    user = request.user
    context = {}

    if user.role == "event_head":
        context["approval_pending"] = EventRegistration.objects.filter(
            is_approved_by_event_head=False,
            event__created_by=user
        )
        context["events_created"] = Event.objects.filter(created_by=user)
        context["role"] = "event_head"

    elif user.role == "hod":
        context["events_to_approve"] = Event.objects.filter(is_venue_approved_by_hod=False)
        context["unblock_requests"] = User.objects.filter(is_blocked=True, hod_approved=False)
        context["role"] = "hod"

    else:
        return redirect("dashboard")

    return render(request, "approval_dashboard.html", context)