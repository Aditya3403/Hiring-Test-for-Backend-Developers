import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
<<<<<<< HEAD

SECRET_KEY = 'your-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

=======
SECRET_KEY = 'your-secret-key'
DEBUG = True
ALLOWED_HOSTS = []
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
CORS_ALLOW_ALL_ORIGINS = True
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'faq',
    'ckeditor',
    'django_ckeditor_5',
<<<<<<< HEAD
    'corsheaders',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
=======
    'corsheaders'
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
<<<<<<< HEAD
]
=======
    'corsheaders.middleware.CorsMiddleware',
]
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}
<<<<<<< HEAD
=======
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1", 
    }
}
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
CKEDITOR_5_CONFIGS = {
    'default': {
        'toolbar': [
            'heading', '|', 'bold', 'italic', 'underline', '|',
            'bulletedList', 'numberedList', '|', 'link', '|',
            'blockQuote', 'codeBlock', 'imageUpload'
        ],
        'image': {
            'toolbar': [
                'imageTextAlternative', '|',
                'imageStyle:full', 'imageStyle:side'
            ]
        }
    }
}
<<<<<<< HEAD

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
=======
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
<<<<<<< HEAD
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
=======
]
>>>>>>> cf9f1cb (feat: Add multilingual FAQ model with Redis caching)
