#!/bin/sh

echo "Starting Django server"
python manage.py runserver 0.0.0.0:$PORT
