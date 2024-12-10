"""
Este archivo contiene la configuración principal de tu proyecto Django, incluyendo las rutas de archivos estáticos, configuraciones de base de datos, autenticación, y más.

- Seguridad:
    - `SECRET_KEY`: La clave secreta utilizada en producción debe mantenerse en secreto.
    - `DEBUG`: Debe estar en `False` en producción.
    - `ALLOWED_HOSTS`: Define los dominios permitidos para el proyecto.

- Instalación de aplicaciones:
    - Se incluyen aplicaciones estándar de Django como `admin`, `auth`, `sessions`, entre otras.
    - También se incluyen aplicaciones personalizadas como `Inicio`, `Tienda`, `Donaciones`, etc.
    - Se configura `django-allauth` para la autenticación de usuarios.

- Base de datos:
    - Se utiliza PostgreSQL como motor de base de datos. Configura los valores de nombre, usuario y contraseña de la base de datos.

- Configuración de archivos estáticos:
    - Configura las rutas para archivos estáticos y medios (como imágenes, videos, documentos).
    - Si `DEBUG` es `False`, los archivos estáticos se almacenan en `STATIC_ROOT`.

- Configuración de correo electrónico:
    - Se utiliza el backend SMTP de Gmail para enviar correos electrónicos, tanto en desarrollo como en producción.

- Otros ajustes:
    - `LOGIN_REDIRECT_URL` y `LOGOUT_REDIRECT_URL`: Redirige al usuario a la página de inicio después de iniciar o cerrar sesión.
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', default='eufgshjadfg3723rd')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = [
    'tecno-fusion-360.onrender.com', 
    'localhost', 
    '127.0.0.1'
]

RENDER_EXTERNA_HOSTNAME = os.environ.get('RENDER_EXTERNA_HOSTNAME')
if RENDER_EXTERNA_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNA_HOSTNAME)
# Application definition

STATICFILES_DIRS = [
    BASE_DIR / "static",  # Esto debe coincidir con la ruta donde están tus archivos estáticos.
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'Inicio',
    'Tienda',
    'Donaciones',
    'PreguntasFre',
    'contacto',
    'allauth',
    'garantia',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

]

SITE_ID = 1
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
        'OAUTH_PKCE_ENABLED': True,
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'TecnoFusion3.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'TecnoFusion3.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'prueba_mm6n',
    'USER': 'prueba_mm6n_user',
    'PASSWORD': 'TipG7Fyn8bgSzrpsfbUHXqT54V04YQWr',
    'HOST': 'dpg-ct99uit6l47c73ap9cf0-a',
    'PORT':'5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
# Directorios para archivos estáticos y de medios
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
if not DEBUG:
    STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuraciones adicionales de Django-Allauth
#pip install psycopg
#python -m pip install Pillow
#pip install requests
#pip install PyJWT
#pip install cryptography



# Creo el servidor de correo por consola
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Ruta adonde va a parar el usuario logueado
LOGIN_REDIRECT_URL = 'inicio'
LOGOUT_REDIRECT_URL = 'inicio'



# Configuración de correo electrónico
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tecnofusion360t@gmail.com'  
EMAIL_HOST_PASSWORD = 'vjjv xjgi xdaq jrqt' 