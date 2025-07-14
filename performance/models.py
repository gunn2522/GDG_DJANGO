from django.db import models
from users.models import User

class PerformanceRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_score = models.FloatField(default=0)
    tasks_completed = models.IntegerField(default=0)
    events_led = models.IntegerField(default=0)
    issues_reported = models.IntegerField(default=0)
    admin_comment = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - Score: {self.total_score}"
