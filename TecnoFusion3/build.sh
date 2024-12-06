#!/usr/bin/env bash

set -o errexit

# Instalar las dependencias desde requirements.txt en el directorio TecnoFusion3
pip install -r TecnoFusion3/requirements.txt

# Ejecutar collectstatic desde el archivo manage.py dentro de TecnoFusion3
python TecnoFusion3/manage.py collectstatic --noinput

# Aplicar migraciones desde el archivo manage.py dentro de TecnoFusion3
python TecnoFusion3/manage.py migrate
