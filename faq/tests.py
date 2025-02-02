from django.test import TestCase
from .models import FAQ

class FAQTestCase(TestCase):
    def setUp(self):
        FAQ.objects.create(question="What is Django?", answer="Django is a web framework.")

    def test_faq_creation(self):
        faq = FAQ.objects.get(question="What is Django?")
<<<<<<< HEAD
        self.assertEqual(faq.answer, "Django is a web framework.")
=======
        self.assertEqual(faq.answer, "Django is a web framework.")
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
