from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewset
from .views import *

# Definir un router
router = SimpleRouter()
router.register(r'alumnos',AlumnoViewset)

# ProductoViewset:
# ip:8000/productos/api/ <----- GET de todo
# ip:8000/productos/api/{id} <----- GET, POST, PUT, DELETE de uno

urlpatterns = [
    path('api/', include(router.urls)),
    path('alumnos-list', crudAlumnos, name = 'crud'),
]


