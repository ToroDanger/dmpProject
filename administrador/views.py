from django.shortcuts import render

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