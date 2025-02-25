from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .models import Alumno
from .serializer import AlumnoSerializer

class AlumnoViewset(viewsets.ModelViewSet):
    # Conjunto de query's de la BD
    queryset = Alumno.objects.all()

    # Saber como empaquetar e enviar la informacion
    serializer_class = AlumnoSerializer

    # Saber como voy a renderizar las respuestas
    renderer_classes = [JSONRenderer]
