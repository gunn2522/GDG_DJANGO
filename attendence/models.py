from django.db import models
from django.utils import timezone
from users.models import User
from events.models import Event

class Attendance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    marked_by_student = models.BooleanField(default=False)
    marked_at = models.DateTimeField(null=True, blank=True)

    approved_by_event_head = models.BooleanField(default=False)
    approved_by_event_head_at = models.DateTimeField(null=True, blank=True)

    approved_by_hod = models.BooleanField(default=False)
    approved_by_hod_at = models.DateTimeField(null=True, blank=True)

    pushed_to_erp = models.BooleanField(default=False)
    pushed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.event.title}"
