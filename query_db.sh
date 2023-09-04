#!/bin/bash
docker exec -it eikon-db-1 psql -U eikon -d eikondb -x -c "SELECT * FROM users;"
