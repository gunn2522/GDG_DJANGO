"""
URL configuration for GDG_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path,include

from GDG_project import settings
from dashboard.views import dashboard_view
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', lambda request: redirect('login')),  # 👈 Redirect to login page
    path('users/', include('users.urls')),
    path('events/', include('events.urls')),
    path('attendence/', include('attendence.urls')),
    path('tasks/', include('gdg_tasks.urls')),
    path('infra_issues/', include('infra_issues.urls')),
    path('performance/', include('performance.urls')),
    path('ai_assistant/', include('ai_assistant.urls')),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
