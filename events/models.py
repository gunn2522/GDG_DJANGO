from django.db import models
from users.models import User


class Event(models.Model):
    EVENT_TYPES = [
        ('tech_talk', 'Tech Talk'),
        ('workshop', 'Workshop'),
        ('competition', 'Competition'),
        ('meetup', 'Meetup'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('pending_venue_approval', 'Pending Venue Approval'),
        ('venue_approved', 'Venue Approved'),
        ('published', 'Published'),
        ('completed', 'Completed'),
        ('attendance_sent_to_erp', 'Attendance Sent to ERP'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    event_type = models.CharField(max_length=20, choices=EVENT_TYPES, default='other')
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    is_venue_approved_by_hod = models.BooleanField(default=False)
    last_date_to_apply = models.DateField()
    registration_link = models.URLField(max_length=300, blank=True, null=True)
    systems_required = models.TextField(blank=True)
    poster = models.ImageField(upload_to='event_posters/', blank=True, null=True)
    is_visible = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_events")
    created_at = models.DateTimeField(auto_now_add=True)

    assigned_teachers = models.ManyToManyField(User, related_name='assigned_events_as_teacher', blank=True,
                                               limit_choices_to={'role': 'Teacher'})
    assigned_gdg_members = models.ManyToManyField(User, related_name='assigned_events_as_gdg', blank=True,
                                                  limit_choices_to={'role': 'GDG'})
    event_head = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='led_events',
                                   limit_choices_to={'role': 'EventHead'})

    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)
    is_approved_by_event_head = models.BooleanField(default=False)
    attended = models.BooleanField(default=False)
    is_attendance_approved_by_hod = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.username} → {self.event.title}"


class GDGTask(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'GDG'})
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.event.title} - {self.assigned_to.username}"
