from django.urls import path
from .views import faq_list, test_redis_cache, FAQListView
from . import views

urlpatterns = [
    path('', faq_list, name='faq_list'),
    path('test-cache/', test_redis_cache, name='test-cache'),
    path('faqs/', views.faq_list, name='faq_list'),  # Keep only 'faqs/'
]