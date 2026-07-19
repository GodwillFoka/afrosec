#!/usr/bin/env bash
# Build script for Render.com Django deployment
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate --noinput

# Create superuser if not exists (optional)
python manage.py shell -c "
import os
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@afrosec.org', 'AfroSec2026!')
    print('Superuser created')
else:
    print('Superuser already exists')
"
