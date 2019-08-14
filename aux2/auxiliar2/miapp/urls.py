from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('horario/', views.horario, name='horario'),
	path('equipodocente/', views.equipodocente, name='equipodocente'),
]