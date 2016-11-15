#!/bin/sh -x

su - postgres -c "psql --set ON_ERROR_STOP=on {{ project_name }} < {{ project_name }}.sql
