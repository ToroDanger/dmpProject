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

def home(request):
    context={}
    return render(request, 'administrador/home.html', context)

def crud(request):
    administrador = Compra.objects.all()
    context= {"administrador": administrador}
    return render(request, 'administrador/alumnos_list.html', context)


    # no se sabe si esta completo
# def alumnosAdd(request):
#     if request.method != "POST":
#         generos = Compra.objects.all()
#         context = {"Compra": Compra}
#         return render(request, 'administrador/alumnos_add.html', context)
#     else:
#         nombre = request.POST["nombre"]
#         Detalle = request.POST["detalle"]
#         precio = request.POST["precio"]
       

#         objGenero = Compra.objects.get(nombre=Compra)
#         obj = Compra.objects.create(
#             nombre=nombre,
#             Detalle=Detalle,
#             precio=precio,
#         )
#         obj.save()
#         context = {'mensaje': "OK, datos grabados..."}
#         return render(request, 'administrador/alumnos_add.html', context)

# def alumnos_del(request, pk):
#      context={}
#      try:
#       alumno=Alumno.objects.get(rut=pk)
#       alumno.delete()
#       mensaje='Datos Eliminados'
#       alumnos=Alumno.objects.all()
#       context={"alumnos":alumnos, "mensaje": mensaje}
#       return render(request, 'alumnos/alumnos_list.html', context)
     
#      except:
#       mensaje="Error, no existe el rut..."
#       alumnos=Alumno.objects.all()
#       context={"alumnos":alumnos, "mensaje": mensaje}
#       return render(request, 'alumnos/alumnos_list.html', context)
    

# def alumnos_findEdit (request, pk):
#    if pk!="":
#       alumno=Alumno.objects.get(rut=pk)
#       generos = Genero.objects.all()
#       print(type(alumno.id_genero.genero))

#       context={'alumno':alumno, 'generos': generos}
#    if alumno:
#       return render(request, 'alumnos/alumnos_edit.html', context)
#    else:
#       context={'mensaje':"error, rut no existe"}
#       return render(request, 'alumnos/alumnos_edit.html', context)

# def alumnosUpdate(request):
#     if request.method == "POST":
#         rut = request.POST["rut"]
#         nombre = request.POST["nombre"]
#         apaterno = request.POST["apaterno"]
#         amaterno = request.POST["amaterno"]
#         fechaNac = request.POST["fechaNac"]
#         genero = request.POST["genero"]
#         telefono = request.POST["telefono"]
#         email = request.POST["email"]
#         direccion = request.POST["direccion"]
#         activo = "1"

#         objGenero = Genero.objects.get(id_genero=genero)
#         alumno = Alumno()
#         alumno.rut = rut
#         alumno.nombre = nombre
#         alumno.apellido_paterno = apaterno
#         alumno.apellido_materno = amaterno
#         alumno.fecha_nacimiento = fechaNac
#         alumno.id_genero = objGenero  # Asociar el genero correctamente
#         alumno.telefono = telefono
#         alumno.email = email
#         alumno.direccion = direccion
#         alumno.activo = activo
#         alumno.save()

#         generos = Genero.objects.all()
#         context = {
#             'mensaje': "Datos actualizados",
#             'generos': generos,
#             'alumno': alumno
#         }
#         return render(request, 'alumnos/alumnos_edit.html', context)
#     else:
#         alumnos = Alumno.objects.all()
#         context = {'alumnos': alumnos}
#         return render(request, 'alumnos/alumnos_list.html', context)