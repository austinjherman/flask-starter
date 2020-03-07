# pull official base image
FROM postgres:12.1-alpine

# run create.sql on init
ADD scripts/database.sql /docker-entrypoint-initdb.d