from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat_assistant, name="ai_chat"),
]
