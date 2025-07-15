# from django.contrib import admin
# from django.template.context_processors
# from django.urls import path, include
# from django.shortcuts import redirect
# from django.conf.urls.static import static
# from django.conf import settings
#
# from GDG_project import settings
#
#
# def home_redirect(request):
#     if request.user.is_authenticated:
#         return redirect('dashboard')  # Redirect to dashboard if logged in
#     return redirect('login')  # Redirect to login if not logged in
#
# # urls.py
# from django.urls import path
# from users import views
#
# urlpatterns = [
#     path('login/', views.custom_login_view, name='login'),
#     # ... other routes
# ]
#
# urlpatterns = [
#     path('', home_redirect, name='home'),  # 👈 Add this to handle `/`
#     path('admin/', admin.site.urls),
#     path('dashboard/', include('dashboard.urls')),
#     path('users/', include('users.urls')),
#     path('events/', include('events.urls')),
#     path('attendence/', include('attendence.urls')),
#     path('tasks/', include('gdg_tasks.urls')),
#     path('infra_issues/', include('infra_issues.urls')),
#     path('performance/', include('performance.urls')),
#     path('ai_assistant/', include('ai_assistant.urls')),
# ]
#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views  # for custom_login_view

# 👇 Home redirect view
def home_redirect(request):
    if request.user.is_authenticated:
        return redirect('dashboard')  # Redirect to dashboard if logged in
    return redirect('login')  # Redirect to login if not logged in

urlpatterns = [
    path('', home_redirect, name='home'),  # Root URL redirect logic
    path('admin/', admin.site.urls),
    path('login/', user_views.custom_login_view, name='login'),  # Login view

    # App routes
    path('dashboard/', include('dashboard.urls')),
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('attendence/', include('attendence.urls')),
    path('tasks/', include('gdg_tasks.urls')),
    path('infra_issues/', include('infra_issues.urls')),
    path('performance/', include('performance.urls')),
    path('ai_assistant/', include('ai_assistant.urls')),
]

# 👇 Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
