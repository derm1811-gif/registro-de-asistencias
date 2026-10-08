from django.shortcuts import render
from .models import Estudiante
# Create your views here.
def estudiante_list(request):
    if request.method == 'POST':
        mensaje = Estudiante(
            tipo_documento=request.POST.get('tipo_documento'),
            numero_documento=request.POST.get('numero_documento'),
            nombre=request.POST.get('nombre'),
            apellido=request.POST.get('apellido'),
            whatsapp=request.POST.get('whatsapp'),
            asistencia=request.POST.get('asistencia') == 'true',
        )
        mensaje.save()
        return render(request, "estudiantes_gracias.html")

    return render(request, "estudiantes.html")
    
    