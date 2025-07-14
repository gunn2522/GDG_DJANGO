from django.db import models
from users.models import User
from events.models import Event


class Task(models.Model):
    TASK_ROLES = [
        ('manage_students', 'Manage Students'),
        ('photography', 'Photography'),
        ('attendance', 'Attendance'),
        ('tech_setup', 'Tech Setup'),
        ('reporting', 'Issue Reporting'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    role = models.CharField(max_length=50, choices=TASK_ROLES)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.assigned_to.username} ({self.event.title})"


class IssueReport(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.TextField()
    resolved = models.BooleanField(default=False)
    reported_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Issue by {self.reported_by.username} for {self.event.title}"
