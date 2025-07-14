from django.contrib import admin
from .models import Task, IssueReport

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'assigned_to', 'event', 'role', 'is_completed')

@admin.register(IssueReport)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('reported_by', 'event', 'issue', 'resolved')
