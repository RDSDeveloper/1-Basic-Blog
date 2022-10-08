#forms.py 
# traemos el modelo que queremos manipular, Post

#declaramos el formulario con class
#declaramos el modelo que queremos editar para este formulario, herencia?


from django import forms
from.models import Post

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=("title","contento")


#ahora este formulario creado lo tenemos que llevar a la vista, para que se vea no?
