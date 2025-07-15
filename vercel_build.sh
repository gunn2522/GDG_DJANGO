#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Migrate and collect static
python manage.py migrate --noinput
python manage.py collectstatic --noinput
