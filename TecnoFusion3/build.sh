#!/usr/bin/env bash

set -o errexit

pip install -r TecnoFusion3/requirements.txt

python manage.py collectstatic --noinput
python TecnoFusion3/manage.py migrate