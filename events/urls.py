from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('calendar/', views.event_calendar_view, name='event_calendar'),
    path('calendar/data/', views.event_calendar_data, name='event_calendar_data'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('<int:event_id>/mark-attendance/', views.mark_attendance, name='mark_attendance'),
    path('<int:event_id>/approve-venue/', views.approve_venue, name='approve_venue'),
    path('<int:event_id>/approve-attendance/', views.approve_attendance, name='approve_attendance'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
