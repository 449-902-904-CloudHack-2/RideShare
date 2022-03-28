FROM ubuntu

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

RUN pip3 install pika flask

ENTRYPOINT [ "python3" ]

CMD [ "/producer/producer_abc.py" ]
