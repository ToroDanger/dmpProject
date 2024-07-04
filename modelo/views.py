    from django.shortcuts import render

# Create your views here.

def index(request):
    context={}
    return render(request,'modelo/index.html',context)

def juegos(request):
    context={}
    return render(request,'modelo/juegos.html',context)


# proyecto_django/modelo/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'modelo/index.html')
