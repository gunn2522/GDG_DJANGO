from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from events.models import Event, EventRegistration
from gdg_tasks.models import Task
from infra_issues.models import InfraIssue
from performance.models import PerformanceRecord
from attendence.models import Attendance

User = get_user_model()


def get_effective_user(request):
    """Returns the authenticated user or a demo user if not logged in."""
    if request.user.is_authenticated:
        return request.user, False  # not demo
    try:
        demo_user = User.objects.get(username="demo")
        return demo_user, True
    except User.DoesNotExist:
        return None, True  # No demo user available


def dashboard_view(request):
    user, is_demo = get_effective_user(request)
    if not user:
        return HttpResponseForbidden("Access denied: no user or demo user found.")

    context = {"is_demo": is_demo}

    # Allowed roles
    allowed_roles = ["student", "gdg_member", "event_head", "hod", "teacher"]
    if user.role not in allowed_roles:
        return HttpResponseForbidden("Access denied: unrecognized role.")

    # Role-based context
    if user.role == "student":
        context["upcoming_events"] = Event.objects.all().order_by('date')[:5]
        context["my_registrations"] = EventRegistration.objects.filter(student=user)
        context["is_blocked"] = getattr(user, "is_blocked", False)

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


def approval_dashboard_view(request):
    user, is_demo = get_effective_user(request)
    if not user or is_demo:
        return HttpResponseForbidden("Access denied: demo users cannot access approval dashboard.")

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
        return HttpResponseForbidden("Access denied: this page is restricted to event heads and HODs.")

    return render(request, "approval_dashboard.html", context)
