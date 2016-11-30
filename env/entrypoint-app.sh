#!/bin/sh

cd /opt/{{ project_name }}

make start
tail -f uwsgi.log
