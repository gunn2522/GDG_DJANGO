import google.generativeai as genai
from django.conf import settings

genai.configure(api_key=settings.GOOGLE_API_KEY)

def get_ai_response(prompt):
    model = genai.GenerativeModel(model_name='models/gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text
