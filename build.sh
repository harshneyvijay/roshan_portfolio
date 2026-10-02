#!/bin/bash
set -o errexit

# Install dependencies (including Cloudinary and Supabase drivers)
pip install -r requirements.txt

# Upload assets to Cloudinary
python manage.py collectstatic --no-input

# Safely push database schemas to Supabase
python manage.py migrate
