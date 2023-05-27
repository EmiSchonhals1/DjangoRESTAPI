#El archivo "build.sh" es un script utilizado en el desarrollo de software y proyectos de programación. Este archivo suele utilizarse para automatizar el proceso de construcción de una aplicación o proyecto

#!/usr/bin/env bash
# exit on error
set -o errexit

#para ejecutar requirements.txt
pip install -r requirements.txt
#para que se genere la carpeta por defecto de archivos estáticos
python manage.py collectstatic --no-input
#para ejecutar las migraciones 
python manage.py migrate
















