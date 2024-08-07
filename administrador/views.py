from django.shortcuts import render, get_object_or_404
from modelo.models import DMPPROJECT
from .models import Compra
from django.contrib.auth.models import User

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

def perfil(request):
    context= {}
    return render(request, 'administrador/perfil.html', context)


def modificar(request, pk):
    user = get_object_or_404(User, username=pk)
    print(f"Username: {user.username}")

    if request.method == "POST":

        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        
       
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
            
        user.save()

        context = {
             
            'user': username}
        return render(request, 'administrador/modificar.html', context)
    else:
        
        context = {'user': user}
        return render(request, 'administrador/modificar.html', context)
    
def registrar(request):
    if request.method != "POST":
        context={"clase": "registro"}
        return render(request, 'administrador/registrar.html', context)
    else:
        nombre = request.POST["usernombre"]
        last_name = request.POST["last_name"]
        first_name = request.POST["first_name"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(nombre,email, password)
        user.last_name = last_name
        user.first_name = first_name
        user.save()
        context={"clase": "registro", "mensaje":"Los datos fueron registrados"}
        return render(request, 'administrador/registrar.html', context)


def alumnos_findEdit(request, pk):
    if pk:
        try:
            user = User.objects.get(username=pk)  # Busca al usuario por nombre de usuario
            context = {"user": user}
            return render(request, 'administrador/modificar.html', context)
        except User.DoesNotExist:
            context = {"mensaje": "Error, no existe el nombre de usuario."}
            return render(request, 'administrador/modificar.html', context)
    else:
        context = {"mensaje": "Error, no se proporcionó un nombre de usuario válido."}
        return render(request, 'administrador/modificar.html', context)

