from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('gdg_member', 'GDG Member'),
        ('event_head', 'Event Head'),
        ('hod', 'HOD'),
        ('teacher', 'Teacher'),
        ('Admin', 'admin'),    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    erp_number = models.CharField(max_length=20, unique=True)

    is_blocked = models.BooleanField(default=False)
    blocked_reason = models.TextField(blank=True, null=True)
    hod_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} ({self.role})"
