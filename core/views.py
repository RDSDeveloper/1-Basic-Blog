#Hay vistas de clases y vistas de funciones
# El view es una vista, permite controlar las vistas. 


from django.views.generic import View
from django.shortcuts import render


#vista de clase (mas complejas)
#Home view da acceso a Get y Post request, view es buena practica. 
#Get request es lo que pide la informacion para tu ver. El post request es lo que tu envias apra mandar al servidor y que el servidor haga algo con esa informacion
    
class HomeView(View):#usamos el view importado
    #vista de funcion (mas basicas)
    def get(self, request, *args, **kwargs):#get permite llamar. args y kwargs hacen referencia a cualquier parametro que el objeto del request pueda tener. 
        context={


        }
        return render(request, "index.html", context)

