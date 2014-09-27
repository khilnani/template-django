#!/bin/sh -x

su - postgres -c "psql --set ON_ERROR_STOP=on DBNAME < /PATH/DBNAME.sql
