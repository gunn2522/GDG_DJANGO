from django.contrib import admin
from .models import InfraIssue

@admin.register(InfraIssue)
class InfraIssueAdmin(admin.ModelAdmin):
    list_display = ('issue_type', 'location', 'status', 'reporter', 'reported_at')
    list_filter = ('status', 'issue_type', 'location')
