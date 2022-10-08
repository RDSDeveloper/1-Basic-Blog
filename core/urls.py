
# aca tenemos todas las url que podemos aplicar en el navegador. 

from django.contrib import admin
from django.urls import path, include

from .views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls), #esta viene por defecto. con create superuser creamos el usuario administrador. 
    
    path('', HomeView.as_view(), name="home"),
    
    path('blog/', include("blog.urls", namespace="blog"))
]
