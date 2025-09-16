#!/bin/bash

# Create and activate virtual environment
echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate
echo "Virtual environment activated."

# Equivalent PowerShell steps for Windows
echo "For Windows, use the following PowerShell commands:"
echo "python -m venv venv"
echo "venv\\Scripts\\Activate.ps1"

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Create superuser non-interactively if none exists
if ! python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(is_superuser=True).exists()"; then
  echo "Creating superuser..."
  DJANGO_SUPERUSER_EMAIL=admin@example.com DJANGO_SUPERUSER_PASSWORD=adminpassword python manage.py createsuperuser --noinput
fi

# Start server
echo "Starting server on port 8000..."
python manage.py runserver 8000
