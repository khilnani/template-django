#!/bin/sh

echo "Starting uwsgi"
exec uwsgi --ini uwsgi.ini:$ENV
