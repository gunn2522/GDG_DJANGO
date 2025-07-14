from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['event', 'student', 'marked_by_student', 'approved_by_event_head', 'approved_by_hod', 'pushed_to_erp', 'marked_at']
    list_filter = ['marked_by_student', 'approved_by_event_head', 'approved_by_hod', 'pushed_to_erp']
    search_fields = ['event__title', 'student__username']
