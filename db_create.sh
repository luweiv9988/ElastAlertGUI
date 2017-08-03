#!/usr/bin/env bash

SQLITE=`which sqlite3`
DATABASE='database.db'
SCHEMA='schema.sql'

echo "Creating DB..."
`$SQLITE $DATABASE < $SCHEMA`

echo "Inserting default data..."
echo 'insert into user values (1,"admin","8c55d1c8200ed4c67697ae8365279465602ca84112765e48898a033e");' | $SQLITE $DATABASE
