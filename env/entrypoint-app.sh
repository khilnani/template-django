#!/bin/sh

cd /opt/{{ project_name }}

make start
make flower
tail -f uwsgi.log
