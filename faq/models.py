from django.db import models
from django.core.cache import cache
from googletrans import Translator
from django_ckeditor_5.fields import CKEditor5Field 

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field(config_name='default')
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = CKEditor5Field(config_name='default', blank=True, null=True)
    answer_bn = CKEditor5Field(config_name='default', blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.question_hi:
            translator = Translator()
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            translator = Translator()
            self.question_bn = translator.translate(self.question, dest='bn').text

        if not self.answer_hi:
            translator = Translator()
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.answer_bn:
            translator = Translator()
            self.answer_bn = translator.translate(self.answer, dest='bn').text

        cache.delete('faqs')
        super().save(*args, **kwargs)

    def get_translation(self, lang):
        """Returns translated question and always returns the English answer."""
        if lang == "hi":
            question = self.question_hi or self.question
        elif lang == "bn":
            question = self.question_bn or self.question
        else:
            question = self.question

        answer = self.answer
        
        return question, answer

    def __str__(self):
        return self.question

    @staticmethod
    def get_cached_faqs():
        """Fetch FAQs from cache; if not found, fetch from DB and cache it."""
        faqs = cache.get("faqs")
        if not faqs:
            faqs = list(FAQ.objects.all())
            cache.set("faqs", faqs, timeout=300) 
        return faqs