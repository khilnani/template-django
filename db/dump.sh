#!/bin/sh

echo "Dumping"
pg_dump --host 127.0.0.1 --username postgres --password DBNAME > DBNAME.sql

echo "Dumping clean"
pg_dump --host 127.0.0.1 --username postgres --password DBNAME --clean > DBNAME-clean.sql

echo "Dumping data"
pg_dump --host 127.0.0.1 --username postgres --password --data-only DBNAME > DBNAME-data.sql

echo "Dumping data-inserts"
pg_dump --host 127.0.0.1 --username postgres --password --data-only --column-inserts DBNAME > DBNAME-data-insert.sql
