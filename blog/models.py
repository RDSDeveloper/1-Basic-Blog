from statistics import mode
from django.db import models

# Create your models here.
#Cada vez que hacemos cambios en este archivo, tenemos que hacer nuevas migraciones

#esto de abajo es lo primero que añadimos editable. 
#despues de las migraciones podemos crear posts
#class es modelo
#title es titulo, charfield es campo de caracteres
#text field es un campo de texto mas grande

#cada vez que cambiamos algo en archivos models.py hay que hacer migraciones.

#la funcion escrita demarca el nombre del archivo, cambio su codigo indice? no creo

class Post(models.Model):
    title = models.CharField(max_length=300)
    contento = models.TextField()

    def __str__(self):
        return self.title