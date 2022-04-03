import json
from uuid import uuid4
import pika
from flask import Flask, request

consumers = []

app = Flask(__name__)

def createConnections():
    _connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="rabbit_mq")
    )
    # Create channel to publish to ride_match queue
    _channel = _connection.channel()
    _channel.queue_declare(queue="ride_match", durable=True)
    _channel.queue_declare(queue="database", durable=True)

    return _connection, _channel

def sendDataToQueue(queue, data, task_id, channel):
    channel.basic_publish(
        exchange="",
        routing_key=queue,
        body=data,
        properties=pika.BasicProperties(
            delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE,
            message_id=task_id
        )
    )



@app.route("/new_ride", methods=["POST"])
def new_ride():
    connection, channel=createConnections()
    body = json.dumps(request.form)
    task_id = "task_" + uuid4().hex
    sendDataToQueue("ride_matching", body, task_id, channel)
    print(f"Received task {body} via POST, published to queue", flush=True)

    # Create new channel to publish to database queue

    sendDataToQueue("database", body, task_id, channel)

    connection.close()

    return ""


@app.route("/new_ride_matching_consumer", methods=["POST"])
def new_ride_matching_consumer():
    consumers.append({**request.form, "ip_address": request.remote_addr})

    print(f"List of consumers: {consumers}", flush=True)

    return ""
