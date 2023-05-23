#En este archivo crearemos las rutas de la API de forma sencilla usando el módulo routers de Django REST framework

#importamos el módulo routers
from rest_framework import routers
#importamos el ViewSet del modelo Project
from .api import ProjectViewSet

#la variable router toma el valor de DefaultRouter(), el cual crea el CRUD
router = routers.DefaultRouter()

#registraremos en primer lugar el nombre de la ruta y luego el nombre del ViewSet (podemos agregarle como en este caso el nombre de esta ruta)
router.register('api/projects', ProjectViewSet, 'projects')

#urlpatterns tomará todas las urls generadas por router
urlpatterns = router.urls

