import pika
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'OK'


@app.route('/new_ride')
def add():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.21.0.3"))
    channel = connection.channel()
    channel.queue_declare(queue="task_queue", durable=True)
    channel.basic_publish(
        exchange="",
        routing_key="task_queue",
        body="abcd",
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )
    connection.close()
    return " [x] Sent: "


if __name__ == "__main__":
    app.run(debug=True, host="localhost")
