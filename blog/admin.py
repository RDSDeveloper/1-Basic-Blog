import imp
from django.contrib import admin

# Registramos los modelos creados aca

from .models import Post

admin.site.register(Post)


