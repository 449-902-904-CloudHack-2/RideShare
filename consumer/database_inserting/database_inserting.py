import json
import os
from datetime import datetime

import pika
import psycopg2


def callback(ch, method, properties, body):
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    try:
        print(body)
        data = json.dumps(body)
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processing...' + data)
    except TypeError as e:
        return
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------")

    # establishing the connection
    conn = psycopg2.connect(
        database="rideshare_db", user='postgres', password="1234", host='postgres_container',
        port='5432'
    )
    cursor = conn.cursor()

    query = "INSERT INTO RideData JSON '" + json.dumps(data) + "'"

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processed !')


def get_rabbitmq_connection():
    print("Connecting")
    amqp_url = os.environ['AMQP_URL']
    url_params = pika.URLParameters(amqp_url)
    _connection = pika.BlockingConnection(url_params)
    _channel = _connection.channel()
    _channel.queue_declare(queue="task_queue", durable=True)
    _channel.basic_consume(queue="task_queue", on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    _channel.start_consuming()


print("Connecting")
get_rabbitmq_connection()
