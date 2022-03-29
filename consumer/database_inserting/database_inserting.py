import json
from datetime import datetime

import pika
import psycopg2


def get_rabbitmq_connection():
    _connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq_container"))
    _channel = connection.channel()
    return _channel, _connection


channel, connection = get_rabbitmq_connection()


def callback(ch, method, properties, body):
    # print("-----------------------------------------------------------------------------")
    # print("-----------------------------------------------------------------------------")
    # print("-----------------------------------------------------------------------------")
    # print("-----------------------------------------------------------------------------")
    # print("-----------------------------------------------------------------------------")
    # data = json.dumps(body)
    # print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processing...' + data)
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processing...')
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

    # query = "INSERT INTO books JSON '" + json.dumps(data) + "'"

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processed !')


channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
