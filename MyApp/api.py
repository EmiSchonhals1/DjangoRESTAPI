#En este archivo crearemos el ViewSet, que junto con los serializers nos permiten crear API's

#importamos el modelo Project
from .models import Project
#importamos viewsets y permissions
from rest_framework import viewsets, permissions
#importamos el modelo del serializer
from .serializers import ProjectSerializers

#creamos el ViewSet del modelo Project, el cuál heredará lo que ponemos dentro del parámetro
class ProjectViewSet (viewsets.ModelViewSet) :
    #ponemos las consultas que se podrán hacer
    
    #hacemos que el conjunto de datos contenga todos los datos de la tabla Project
    queryset = Project.objects.all()
    #ponemos en una lista quienes tendrán permisos (en este caso AllowAny significa que todos tendrán permiso)
    permission_classes = [permissions.AllowAny]
    #ponemos desde qué serializer convertirá los datos
    serializer_class = ProjectSerializers


# DE ESTA FORMA TENEMOS NUESTRA API CREADA, SOLO NOS FALTA UTILIZARLA A TRAVÉS DE UNA RUTA URL QUE EL CLIENTE PUEDA CONSULTAR 













