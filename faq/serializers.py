from rest_framework import serializers
from .models import FAQ
from django.utils.html import strip_tags

class FAQSerializer(serializers.ModelSerializer):
    stripped_answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'question_hi', 'question_bn', 'answer_hi', 'answer_bn', 'stripped_answer']

    def get_stripped_answer(self, obj):
        return strip_tags(obj.answer)