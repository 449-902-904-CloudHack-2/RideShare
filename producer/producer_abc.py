import json

import pika
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.route('/new_ride', methods=["POST"])
def add():
    request_data = request.get_json()
    channel, connection = get_rabbitmq_connection()
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body=json.dumps(request_data),
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    connection.close()
    return " [x] Sent: "


def get_rabbitmq_connection():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="rabbitmq_container"))
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    return channel, connection


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
