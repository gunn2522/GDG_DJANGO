from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from events.models import Event, EventRegistration
from gdg_tasks.models import Task
from infra_issues.models import InfraIssue
from performance.models import PerformanceRecord
from attendence.models import Attendance

User = get_user_model()

ALLOWED_ROLES = ["student", "gdg_member", "event_head", "hod", "teacher",'demo']


def get_effective_user(request):
    """Returns the authenticated user or a demo user if not logged in."""
    if request.user.is_authenticated:
        return request.user, False  # Not a demo user

    # Try to get or create the demo user
    demo_user, created = User.objects.get_or_create(
        username="demo",
        defaults={
            "password": "demo123",  # Only for creation, not actual login
            "role": "student",      # Default valid role
            "is_active": True,
        }
    )

    # Ensure demo user has a valid role
    if demo_user.role not in ALLOWED_ROLES:
        demo_user.role = "student"
        demo_user.save()

    return demo_user, True  # This is a demo user



def dashboard_view(request):
    user, is_demo = get_effective_user(request)
    if not user:
        return HttpResponseForbidden("Access denied: no user or demo user found.")

    if user.role not in ALLOWED_ROLES:
        return HttpResponseForbidden("Access denied: unrecognized role.")

    context = {"is_demo": is_demo}

    # Role-based context
    if user.role == "student":
        context["upcoming_events"] = Event.objects.all().order_by('date')[:5]
        context["my_registrations"] = EventRegistration.objects.filter(student=user)
        context["is_blocked"] = getattr(user, "is_blocked", False)

    elif user.role == "gdg_member":
        context["assigned_tasks"] = Task.objects.filter(assigned_to=user)
        context["my_performance"] = PerformanceRecord.objects.filter(user=user)

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
