from django.urls import path
from . import views


urlpatterns = [

    path('', views.inicio, name='inicio'),

    path('que-es/', views.que_es, name='que_es'),

    path('tipos/', views.tipos, name='tipos'),

    path('materiales/', views.materiales, name='materiales'),

    path('elaboracion/', views.elaboracion, name='elaboracion'),

    path('beneficios/', views.beneficios, name='beneficios'),

    path('cuidados/', views.cuidados, name='cuidados'),

    path('usos/', views.usos, name='usos'),

    path('preguntas/', views.preguntas, name='preguntas'),

    path('cuestionario/', views.cuestionario, name='cuestionario'),

    path('contacto/', views.contacto, name='contacto'),

]
