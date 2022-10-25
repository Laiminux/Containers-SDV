FROM postgres:14.5
COPY ./initdb.sql /docker-entrypoint-initdb.d/
RUN chmod 777 /docker-entrypoint-initdb.d/initdb.sql