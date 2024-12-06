#!/usr/bin/env bash

set -o errexit

# Cambiar al directorio que contiene manage.py
cd TecnoFusion3

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar collectstatic
python manage.py collectstatic --noinput

# Aplicar migraciones
python manage.py migrate