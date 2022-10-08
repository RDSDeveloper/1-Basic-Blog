# contiene info del proyecto
#aca podemos excribir contraseñas

from pathlib import Path
import os
import environ 

env = environ.Env()
environ.Env.read_env()

#Hace referencia a donde se encuentra el directorio de nuestro archivo django
#Parent permite tener acceso a toda la carpeta del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

#Proteger secret key, como variable de ambiente
#Restringe el acceso a nuestro sitio 
SECRET_KEY = os.environ.get("SECRET_KEY")

#Cuando hagamos despliegue, hay que cambiarlo a False. 
DEBUG = os.environ.get("DEBUG")

#"*" Significa todo, podemos trabajar con cualquier HOST. 
ALLOWED_HOSTS = ["*"]

#Al agregar nuevas apps, tambien tenemos que migrarlas. 
# aca creamos las apps, como la logica de un blog, cursos, etc. 
# son extensiones de nuestra pagina, funcionalidades añadidas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', #de aca para arriba, vienen por defecto. 

    "core",#Asi instalamos core, le damos acceso a django de los archivos dentro de la carpeta CORE.
    "blog",

    "tailwind",
    "theme"
]

TAILWIND_APP_NAME = "theme"
INTERNAL_IPS = [
    "127.0.0.1",
]
#este path lo hicimos para que tailwind cencuentre el node js en nuestro pc. 
NPM_BIN_PATH = "C:/Program Files/nodejs/npm.cmd"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

#esta es la estetica de la app
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],#con esto le decimos de donde sacar la info. 
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


#nuestras imagenes se pueden entender en el servidor, importante al despegar, se usa al final para que el sitio funcione. 
WSGI_APPLICATION = 'core.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#validador de contraseñas, no se toca. 
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


#Esto sirve para que Django funcione en diferentes lenguages
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


#archivos estaticos, permite trabajar nuestras imagenes.
STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
