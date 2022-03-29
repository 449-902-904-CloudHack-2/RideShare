import json
from datetime import datetime

import pika
import psycopg2

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()


def callback(ch, method, properties, body):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processing...')

    data = json.loads(body)

    # establishing the connection
    conn = psycopg2.connect(
        database="rideshare_db", user='postgres', password='postgres', host='postgres_container',
        port='5432'
    )
    cursor = conn.cursor()

    # query = "INSERT INTO books JSON '" + json.dumps(data) + "'"

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processed !')


channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
