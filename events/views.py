from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from django.utils.timezone import now
from django.contrib import messages
from .models import Event, EventRegistration, GDGTask
from users.models import User

@login_required
def event_list(request):
    user = request.user
    today = now().date()

    # Staff roles see all events
    if user.role in ['Admin', 'HOD', 'GDG', 'EventHead']:
        events = Event.objects.all().order_by('-date')
    else:
        # Students only see visible and not-expired events
        events = Event.objects.filter(is_visible=True, last_date_to_apply__gte=today).order_by('date')

    # Fetch the student's registrations
    registrations = EventRegistration.objects.filter(student=user)
    registered_event_ids = set(registrations.values_list('event_id', flat=True))
    attended_event_ids = set(registrations.filter(attended=False).values_list('event_id', flat=True))

    # Add flags to each event for template logic
    for event in events:
        event.is_user_registered = event.id in registered_event_ids
        event.can_mark_attendance = event.id in attended_event_ids

    # DEBUG: show what events are passed to template
    print(f"[DEBUG] Events for user {user.username} ({user.role}): {[event.title for event in events]}")

    return render(request, "events/event_list.html", {
        "events": events,
        "today": today,
        "user": request.user,
    })

from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden
from .models import Event

def create_event(request):
    if request.user.role not in ['admin', 'GDG', 'EventHead']:
        return HttpResponseForbidden("Not authorized to create event.")

    if request.method == "POST":
        poster = request.FILES.get('poster')
        Event.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            date=request.POST['date'],
            time=request.POST['time'],
            venue=request.POST['venue'],
            systems_required=request.POST.get('systems_required', ''),
            last_date_to_apply=request.POST['last_date_to_apply'],
            created_by=request.user,
            event_head=request.user,
            status='pending_venue_approval',
            poster=poster
        )
        return redirect('event_list')

    # This must render the form
    return render(request, 'events/create_event.html')



@login_required
def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, "events/event_details.html", {"event": event})


@login_required
def register_for_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if now().date() > event.last_date_to_apply:
        messages.error(request, "Registration deadline passed.")
        return redirect("event_list")

    reg, created = EventRegistration.objects.get_or_create(event=event, student=request.user)
    if created:
        messages.success(request, "Successfully registered!")
    else:
        messages.info(request, "Already registered.")

    return redirect("event_list")


@login_required
def mark_attendance(request, event_id):
    registration = EventRegistration.objects.filter(event_id=event_id, student=request.user).first()
    if registration:
        registration.attended = True
        registration.save()
        messages.success(request, "Marked as attended. Awaiting HOD approval.")
    return redirect("event_list")


@login_required
def approve_venue(request, event_id):
    if request.user.role != 'HOD':
        return HttpResponseForbidden()
    event = get_object_or_404(Event, pk=event_id)
    event.is_venue_approved_by_hod = True
    event.status = 'venue_approved'
    event.save()
    messages.success(request, "Venue approved.")
    return redirect("event_detail", event_id=event.id)


@login_required
def approve_attendance(request, event_id):
    if request.user.role != 'HOD':
        return HttpResponseForbidden()
    EventRegistration.objects.filter(event_id=event_id, attended=True).update(is_attendance_approved_by_hod=True)
    event = get_object_or_404(Event, pk=event_id)
    event.status = 'attendance_sent_to_erp'
    event.save()
    messages.success(request, "Attendance pushed to ERP.")
    return redirect("event_detail", event_id)


@login_required
def admin_dashboard(request):
    if request.user.role != 'Admin':
        return HttpResponseForbidden()

    events = Event.objects.prefetch_related('assigned_teachers', 'assigned_gdg_members', 'eventregistration_set')
    return render(request, 'admin_dashboard.html', {'events': events})


@login_required
def event_calendar_data(request):
    events = Event.objects.filter(is_visible=True)
    data = [
        {
            "title": event.title,
            "start": f"{event.date}T{event.time}",
            "url": f"/events/{event.id}/"
        } for event in events
    ]
    return JsonResponse(data, safe=False)


@login_required
def event_calendar_view(request):
    return render(request, 'events/calendar.html')
