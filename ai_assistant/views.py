from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .gemini_client import get_ai_response

@login_required
def chat_assistant(request):
    answer = None
    if request.method == "POST":
        prompt = request.POST["prompt"]
        answer = get_ai_response(prompt)

    return render(request, "ai_assistant/chat.html", {
        "answer": answer
    })
