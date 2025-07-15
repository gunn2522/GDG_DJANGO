from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if logged in
    return redirect('login')  # Redirect to login if not logged in

urlpatterns = [
    path('', home_redirect, name='home'),  # 👈 Add this to handle `/`
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('attendence/', include('attendence.urls')),
    path('tasks/', include('gdg_tasks.urls')),
    path('infra_issues/', include('infra_issues.urls')),
    path('performance/', include('performance.urls')),
    path('ai_assistant/', include('ai_assistant.urls')),
]
