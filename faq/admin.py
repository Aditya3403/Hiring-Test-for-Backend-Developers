from django.contrib import admin
from .models import FAQ

<<<<<<< HEAD

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "question_hi", "question_bn")
=======
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "question_hi", "question_bn")
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
