from django.contrib import admin
from .models import Event, EventRegistration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'venue', 'is_venue_approved_by_hod', 'created_by')

@admin.register(EventRegistration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'student', 'registered_at', 'is_approved_by_event_head', 'attended')
