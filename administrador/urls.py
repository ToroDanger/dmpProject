from django.urls import path, include
from  . import views

urlpatterns = [
    path('menu/',views.menu,name='menu'),
    path('home/', views.menu, name='home'),

    # crud
    path('crud', views.crud, name='crud'),
    path('juego', views.juego, name='juego'),
    path('alumnos_del/<str:pk>', views.alumnos_del, name='alumnos_del'),
    path('alumnosAdd', views.alumnosAdd, name='alumnosAdd'),
    path('alumnos_findEdit/<str:pk>', views.alumnos_findEdit, name='alumnos_findEdit'),
    path('perfil', views.perfil, name='perfil'),
    path('modificar/<str:pk>/', views.modificar, name='modificar'),
    path('registrar', views.registrar, name='registrar'),
    ]





