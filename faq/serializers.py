# faq/serializers.py

from rest_framework import serializers
from .models import FAQ
from django.utils.html import strip_tags

class FAQSerializer(serializers.ModelSerializer):
    stripped_answer = serializers.SerializerMethodField()  # Serializer method for stripped answer

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn', 'stripped_answer']  # Add stripped_answer here

    def get_stripped_answer(self, obj):
        # Strip HTML tags from the answer field
        return strip_tags(obj.answer)