FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app
COPY ./init.sql /docker-entrypoint-initdb.d/

RUN pip3 install pika flask psycopg2-binary

ENTRYPOINT [ "python3" ]

CMD [ "-u", "./database_inserting.py" ]
