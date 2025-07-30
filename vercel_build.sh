#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install Python dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput



