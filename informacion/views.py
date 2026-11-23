
from django.shortcuts import render


# Página principal
def inicio(request):
    return render(request, 'informacion/inicio.html')


# Información sobre la composta
def que_es(request):
    return render(request, 'informacion/que_es.html')


# Tipos de composta
def tipos(request):
    return render(request, 'informacion/tipos.html')


# Materiales necesarios
def materiales(request):
    return render(request, 'informacion/materiales.html')


# Proceso de elaboración
def elaboracion(request):
    return render(request, 'informacion/elaboracion.html')


# Beneficios de la composta
def beneficios(request):
    return render(request, 'informacion/beneficios.html')


# Cuidados de la composta
def cuidados(request):
    return render(request, 'informacion/cuidados.html')


# Usos de la composta
def usos(request):
    return render(request, 'informacion/usos.html')


# Preguntas frecuentes
def preguntas(request):
    return render(request, 'informacion/preguntas.html')


# Cuestionario interactivo
def cuestionario(request):
    return render(request, 'informacion/cuestionario.html')


# Información del proyecto PAEC
def contacto(request):
    return render(request, 'informacion/contacto.html')
