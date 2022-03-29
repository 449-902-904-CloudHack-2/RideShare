import pika
import json
import psycopg2
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters(host='127.0.0.1'))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processing...')

    data = json.loads(body)

    #establishing the connection
    conn = psycopg2.connect(
       database="rideshare_db", user='postgres', password='postgres', host='postgres_container', port= '5432'
    )
    cursor = conn.cursor()

    #query = "INSERT INTO books JSON '" + json.dumps(data) + "'"

    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ' Processed !')


channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()





'''import time

import pika

sleepTime = 10
print(' [*] Sleeping for ', sleepTime, ' seconds.')
time.sleep(30)

print(' [*] Connecting to server ...')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

print(' [*] Waiting for messages.')


def callback(ch, method, properties, body):
    print(" [x] Received %s" % body)
    cmd = body.decode()

    if cmd == 'hey':
        print("hey there")
    elif cmd == 'hello':
        print("well hello there")
    else:
        print("sorry i did not understand ", body)

    print(" [x] Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)
channel.start_consuming()
'''
