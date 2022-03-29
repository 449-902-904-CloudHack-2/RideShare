FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

RUN pip3 install pika flask psycopg2

ENTRYPOINT [ "python3" ]

CMD [ "/database_inserting/database_inserting.py" ]
