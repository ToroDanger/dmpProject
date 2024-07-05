from django.shortcuts import render
from modelo.models import DMPPROJECT
from .models import Compra

def mi_vista(request):
    objetos = MiModelo.objects.all()
# Create your views here.

# @login_required
def menu(request):
    request.session["usuario"]="Drobles"
    usuario=request.session["usuario"]
    context={'usuario':usuario}
    return render(request, 'administrador/menu.html', context)

def juego(request):
    context={}
    return render(request, 'administrador/juego.html', context)

def crud(request):
    administrador = Compra.objects.all()
    context= {"administrador": administrador}
    return render(request, 'administrador/alumnos_list.html', context)



def alumnosAdd(request):
    if request.method != "POST":
        administrador = Compra.objects.all()
        context = {"administrador": administrador}
        return render(request, 'administrador/alumnos_add.html', context)
    else:
        nombre = request.POST["nombre"]
        detalle = request.POST["detalle"]
        precio = request.POST["precio"]


      
        compra = Compra.objects.create(
            Nombre=nombre,
            Detalle=detalle,
            Precio=precio
        )
        compra.save()
        context = {'mensaje': "OK, datos grabados..."}
        return render(request, 'administrador/alumnos_add.html', context)
    

    




    # no se sabe si esta completo


def alumnos_del(request, pk):
      context={}
      try:
       alumno=Compra.objects.get(nombre=pk)
       alumno.delete()
       mensaje='Datos Eliminados'
       administrador=Compra.objects.all()
       context={"administrador":administrador, "mensaje": mensaje}
       return render(request, 'administrador/alumnos_list.html', context)
     
      except:
       mensaje="Error, no existe el nombre..."
       administrador=Compra.objects.all()
       context={"administrador":administrador, "mensaje": mensaje}
       return render(request, 'administrador/alumnos_list.html', context)
    

def alumnos_findEdit (request, pk):
    if pk!="":
       alumno=Compra.objects.get(nombre=pk)
       generos = Compra.objects.all()
       print(type(alumno.id_genero.genero))

       context={'alumno':alumno, 'generos': generos}
    if alumno:
       return render(request, 'administrador/alumnos_edit.html', context)
    else:
       context={'mensaje':"error, nombre no existe"}
       return render(request, 'administrador/alumnos_edit.html', context)

