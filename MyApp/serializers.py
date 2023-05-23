#en este archivo crearemos los serializers, los cuales junto con el ViewSet creado en api.py nos permitirán crear API's

#importamos el módulo serializers
from rest_framework import serializers
#importamos el modelo Project
from .models import Project


#DESDE ESTE ARCHIVO, DJANGO SABRÁ QUE RESPONDER CUANDO SE HAGA UNA PETICIÓN POST, GET, Put y Delete

#creamos la clase que nos permita convertir el modelo en datos que puedan ser consultados
class ProjectSerializers(serializers.ModelSerializer) :
    class Meta :
        #en model ponemos el nombre de la app
        model = Project
        #ahora ponemos los campos que serán consultados dentro de una tupla. Los mismos serán los que tenemos dentro de la clase Project en el archivo models.py. También podemos verlos en las migraciones de la app Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        #ahora ponemos los campos de solo lectura, osea los que no queremos que el usuario pueda modificar
        read_only_fields = ('created_at', ) #debemos poner una coma para que no lo lea como string y no nos tire errores al ejecutar la web






