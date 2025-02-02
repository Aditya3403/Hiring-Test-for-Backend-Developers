from rest_framework.response import Response
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.views import APIView
from .models import FAQ
from .serializers import FAQSerializer
from django.http import HttpResponse

def faq_list(request):
    lang = request.GET.get("lang", "en") 
    faqs = FAQ.objects.all()
    translated_faqs = []
    for faq in faqs:
        question, answer = faq.get_translation(lang)
        translated_faqs.append({
            "id": faq.id,
            "question": question,
            "answer": answer,
        })
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
        lang = request.GET.get("lang", "en")
        faqs = FAQ.get_cached_faqs()

        data = []
        for faq in faqs:
            question, answer = faq.get_translation(lang)

            data.append({
                "id": faq.id,
                "question": question,
                "answer": answer,
            })

        return Response({"faqs": data})