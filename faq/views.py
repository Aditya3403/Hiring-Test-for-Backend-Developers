from rest_framework.response import Response
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse

def faq_list(request):
    # Fetch all FAQs from the database
    lang = request.GET.get("lang", "en")  # Default to "en" if no language is specified
    faqs = FAQ.objects.all()  # Get all FAQs

    # Translate FAQ content based on the selected language
    translated_faqs = []
    for faq in faqs:
        question, answer = faq.get_translation(lang)  # Assuming this method returns both translations

        # Append the translated FAQs to the list
        translated_faqs.append({
            "id": faq.id,
            "question": question,
            "answer": answer,
        })

    # Render the FAQ list template and pass the translated FAQ data
    return render(request, 'faq/faq_list.html', {'faqs': translated_faqs})

def home(request):
    return HttpResponse('''
        <html>
            <head>
                <style>
                    body {
                        text-align: center;  /* Centers the text */
                        font-family: Arial, sans-serif;
                        padding-top: 50px;
                    }
                    .button {
                        background-color: #4CAF50; /* Green */
                        border: none;
                        color: white;
                        padding: 15px 32px;
                        text-align: center;
                        text-decoration: none;
                        display: inline-block;
                        font-size: 16px;
                        margin-top: 20px;
                        cursor: pointer;
                        border-radius: 5px;
                    }
                    .button:hover {
                        background-color: #45a049;
                    }
                </style>
            </head>
            <body>
                <h1>Welcome to the FAQ App!</h1>
                <a href="/api/faqs/" class="button">Go to FAQ Page</a>
            </body>
        </html>
    ''')

def test_redis_cache(request):
    cached_value = cache.get("test_key")

    if not cached_value:
        cached_value = "Hello from Django Cache!"
        cache.set("test_key", cached_value, timeout=300)
        return JsonResponse({"message": "Stored in Redis", "data": cached_value})

    return JsonResponse({"message": "Retrieved from Redis", "data": cached_value})

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get("lang", "en")  # Default to "en" if no language is specified
        faqs = FAQ.get_cached_faqs()  # Get cached FAQs

        # Create a new list of FAQs with translations
        data = []
        for faq in faqs:
            question, answer = faq.get_translation(lang)  # Get both question and answer translations

            data.append({
                "id": faq.id,
                "question": question,
                "answer": answer,  # This will always be in English
            })

        return Response({"faqs": data})