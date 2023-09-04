#!/bin/bash
docker exec -it backend_takehome-db-1 psql -U eikon -d eikondb -x -c "SELECT * FROM users;"
