from django.db import models
from django.core.cache import cache
from googletrans import Translator
from django_ckeditor_5.fields import CKEditor5Field  # Import CKEditor5

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field(config_name='default')  # Use CKEditor5Field for WYSIWYG editor
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation for question
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation for question
    answer_hi = CKEditor5Field(config_name='default', blank=True, null=True)  # Hindi translation for answer
    answer_bn = CKEditor5Field(config_name='default', blank=True, null=True)  # Bengali translation for answer

    def save(self, *args, **kwargs):
        # Translate questions if not already translated
        if not self.question_hi:
            translator = Translator()
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            translator = Translator()
            self.question_bn = translator.translate(self.question, dest='bn').text

        # Translate answers if not already translated
        if not self.answer_hi:
            translator = Translator()
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            translator = Translator()
            self.answer_bn = translator.translate(self.answer, dest='bn').text

        # Clear the FAQ cache whenever saving the FAQ
        cache.delete('faqs')
        super().save(*args, **kwargs)

    def get_translation(self, lang):
        """Returns translated question and always returns the English answer."""
        # Get the question in the requested language, defaulting to English if not available
        if lang == "hi":
            question = self.question_hi or self.question
        elif lang == "bn":
            question = self.question_bn or self.question
        else:
            question = self.question  # Default to English if no translation is available

        # Always return the answer in English
        answer = self.answer
        
        return question, answer

    def __str__(self):
        return self.question

    @staticmethod
    def get_cached_faqs():
        """Fetch FAQs from cache; if not found, fetch from DB and cache it."""
        faqs = cache.get("faqs")  # Try to get FAQs from Redis cache
        if not faqs:
            faqs = list(FAQ.objects.all())  # Query DB if not in cache
            cache.set("faqs", faqs, timeout=300)  # Cache results for 5 minutes
        return faqs