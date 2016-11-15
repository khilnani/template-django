#!/bin/sh

echo "Dumping"
pg_dump --host 127.0.0.1 --username postgres --password {{ project_name }} > {{ project_name }}.sql

echo "Dumping clean"
pg_dump --host 127.0.0.1 --username postgres --password {{ project_name }} --clean > {{ project_name }}-clean.sql

echo "Dumping data"
pg_dump --host 127.0.0.1 --username postgres --password --data-only {{ project_name }} > {{ project_name }}-data.sql

echo "Dumping data-inserts"
pg_dump --host 127.0.0.1 --username postgres --password --data-only --column-inserts {{ project_name }} > {{ project_name }}-data-insert.sql
