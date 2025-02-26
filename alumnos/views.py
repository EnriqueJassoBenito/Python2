from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .serializer import AlumnoSerializer
from .forms import alumnoForms
from django.shortcuts import render, redirect

class AlumnoViewset(viewsets.ModelViewSet):
    # Conjunto de query's de la BD
    queryset = Alumno.objects.all()

    # Saber como empaquetar e enviar la informacion
    serializer_class = AlumnoSerializer

    # Saber como voy a renderizar las respuestas
    renderer_classes = [JSONRenderer]

def crudAlumnos(request):
    def registrar_alumno(request):
     if request.method == 'POST':
        form = alumnoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opciones')
        else:
            form = alumnoForms()
            return render(request, 'osorio_enrique.html', {'form': form})
            
    def ver_alumno(request):
        alumnos = Alumno.objects.all()
        return render(request, 'osorio_enrique.html', {'alumnos': alumnos})
    
    # Aquí puedes determinar qué acción tomar según el método de la solicitud
    if request.method == 'POST':
        return registrar_alumno(request)
    else:
        return ver_alumno(request)