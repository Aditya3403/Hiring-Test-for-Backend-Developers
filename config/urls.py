from django.contrib import admin
from django.urls import path, include
from faq.views import home  

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include('faq.urls')), 
    path('ckeditor5/', include('django_ckeditor_5.urls')),
]
