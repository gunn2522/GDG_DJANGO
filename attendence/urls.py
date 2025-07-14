from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_home, name='attendance_home'),
    path('mark/<int:event_id>/', views.mark_attendance, name='mark_attendance'),
    path('admin/dashboard/', views.admin_attendance_dashboard, name='admin_attendance_dashboard'),
]
