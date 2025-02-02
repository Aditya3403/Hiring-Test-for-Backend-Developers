from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from faq.views import home  
=======
from faq.views import home
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('api/', include('faq.urls')), 
=======
    path('api/', include('faq.urls')),
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
