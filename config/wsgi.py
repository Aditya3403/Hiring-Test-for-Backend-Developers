import os
<<<<<<< HEAD
=======

>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
