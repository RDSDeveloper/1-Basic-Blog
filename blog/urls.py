#aca creamos nuestros urls, permite acceder a vistas creadas para nuestro blog 


from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name="blog"

#todo archivo URL tiene que ser declarado con URLPATTERNS
#archivo de urls basico para acceder a las vistas
#pk es el private key, cada post tiene un ID numerico unico en la DB, 
urlpatterns = [ 
    path("", BlogListView.as_view(), name="home"),
    path("create/", BlogCreateView.as_view(), name="create"),
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="delete")
    ]
