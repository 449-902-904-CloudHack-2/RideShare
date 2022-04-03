import json
import time

import pika
import pymongo

time.sleep(20)


def callback(ch, method, properties, body):
    collection = dbConnection()
    body = json.loads(body)
    body["_id"] = properties.message_id
    print(f"Consumed {body} from database queue")

    collection.insert_one(body)

    ch.basic_ack(delivery_tag=method.delivery_tag)


def dbConnection():
    print("Database consumer starting...")
    client = pymongo.MongoClient("mongodb://mongodb_container:27017")
    db = client["ride_matching_db"]
    _collection = db["ride_details"]

    return _collection


def rabbitmqConnection():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbit_mq")
    )
    _channel = connection.channel()
    _channel.queue_declare(queue="database", durable=True)
    print("Database consumer started...")
    _channel.basic_qos(prefetch_count=1)
    _channel.basic_consume(queue="database", on_message_callback=callback)
    _channel.start_consuming()


rabbitmqConnection()
