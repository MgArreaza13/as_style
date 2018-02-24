"""
Django settings for EstiloOnline project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import pymysql
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'tosmg$1jyf^8m64xi%gip&8=ei0&9^x7z@d!&bk#1k50^#kl^6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'estiloonline.pythonanywhere.com',
    'localhost'
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.Notificaciones',
    'apps.Turn',
    'apps.Client',
    'apps.Collaborator',
    'apps.PanelPrincipal',
    'apps.Product',
    'apps.Proveedores',
    'apps.Profile',
    'apps.Service',
    'apps.UserProfile',
    'apps.Configuracion',
    'apps.Caja',
    'apps.ReservasWeb',
    'social_django',
    'rest_auth',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    'corsheaders',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
]

ROOT_URLCONF = 'EstiloOnline.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect', 
                'apps.ContextProcesor.server_data.server_url',
                'apps.ContextProcesor.logo_data.render_logo',
            ],
        },
    },
]

WSGI_APPLICATION = 'EstiloOnline.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

""""
#para el servidor 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"EstiloOnline$as_style",
        "USER":"EstiloOnline",
        "PASSWORD":'miguel22702517',
        "PORT":'',
        'HOST':"EstiloOnline.mysql.pythonanywhere-services.com",
        },
    }

"""



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':"as_style",
        "USER":"root",
        "PASSWORD":'',
        "PORT":'',
        'HOST':"Localhost",
        },
    }





# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'static', 'media')

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATIC_ROOT = "/home/EstiloOnline/as_style/EstiloOnline/static" #esta linea es importante para que arranque el servidor pythonanywhere



AUTHENTICATION_BACKENDS = (

    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.yahoo.YahooOpenId',
  	'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',


    )

SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/login'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'
LOGIN_REDIRECT_URL = '/home'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = False
SOCIAL_AUTH_TWITTER_KEY = 'GKQe03bKfN0VnhMKWshj9qU2H'
SOCIAL_AUTH_TWITTER_SECRET = '3fVH418FdvjLj6kPZ9jkLCqZMSoUEKjCul8f6qZfEHA5dt7ItN' 
SOCIAL_AUTH_FACEBOOK_KEY = '306808163103691'
SOCIAL_AUTH_FACEBOOK_SECRET = 'eb5ee7f19bad1431f28d1684727c2cc9' 

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'as.estiloonline@gmail.com'
EMAIL_HOST_PASSWORD = 'asadmin123'
EMAIL_PORT = 587

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],


}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}

REST_USE_JWT = True

SITE_ID = 1

CORS_ORIGIN_WHITELIST = ('*')
CORS_URLS_REGEX = r'^/api/.*$'
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
)