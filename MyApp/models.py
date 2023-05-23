from django.db import models

# Create your models here.

#creamos la tabla Project en la base de datos, la misma tendrá 4 columnas
class Project(models.Model) :
    #el título sera un string de máximo 200 caracteres
    title = models.CharField(max_length=200)
    #la descripción será un texto extenso, por ende es un TextField
    description = models.TextField()
    #para saber que tecnología se usó. es un string de máximo 200 caracteres
    technology = models.CharField(max_length=200)
    #para saber cuando se creó el proyecto. con esto hacemos que la fecha y hora se ponga automáticamente al crear el proyecto y el parámetro auto_now_add=True hace que se guarden automáticamente estos datos
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    
    