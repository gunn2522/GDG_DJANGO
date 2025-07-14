from django.contrib import admin
from .models import PerformanceRecord

@admin.register(PerformanceRecord)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("user", "total_score", "tasks_completed", "events_led", "issues_reported", "updated_at")
    list_filter = ("user",)
    search_fields = ("user__username",)
