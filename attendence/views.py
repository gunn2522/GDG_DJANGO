from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.timezone import now
from .models import Attendance
from events.models import Event


@login_required
def attendance_home(request):
    events = Event.objects.filter(eventregistration__student=request.user)
    return render(request, 'attendance_home.html', {'events': events})


@login_required
def mark_attendance(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if not event.eventregistration_set.filter(student=request.user).exists():
        messages.error(request, "You are not registered for this event.")
        return redirect('attendance_home')

    attendance, created = Attendance.objects.get_or_create(event=event, student=request.user)
    if attendance.marked_by_student:
        messages.info(request, "You already marked your attendance.")
    else:
        attendance.marked_by_student = True
        attendance.marked_at = now()
        attendance.save()
        messages.success(request, "Attendance marked successfully.")
    return redirect('attendance_home')


@login_required
def admin_attendance_dashboard(request):
    if request.user.role != "Admin":
        messages.error(request, "Access denied.")
        return redirect("dashboard")

    attendance_list = Attendance.objects.select_related('event', 'student').all()
    return render(request, 'admin_dashboard.html', {'attendance_list': attendance_list})
