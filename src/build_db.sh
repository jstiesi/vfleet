#!/bin/bash

dropdb vfleet

createdb vfleet

psql -d vfleet -f create_tables.sql

psql -U postgres -d vfleet -c "\\copy VEHICLE FROM '~/vfleet/src/csv_files/vehicle.csv' csv header"
psql -U postgres -d vfleet -c "\\copy COST FROM '~/vfleet/src/csv_files/cost.csv' csv header"
psql -U postgres -d vfleet -c "\\copy FIN_INCENT FROM '~/vfleet/src/csv_files/fin_incent.csv' csv header"
psql -U postgres -d vfleet -c "\\copy POLLUTANT FROM '~/vfleet/src/csv_files/pollutant.csv' csv header"