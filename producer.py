import pika
import json

params = pika.URLParameters(
    'amqps://nhzsened:sghwS0lh1e9inlPPL40Zs2AU53RAVzCJ@capybara.lmq.cloudamqp.com/nhzsened'
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):

    properties = pika.BasicProperties(
        content_type='application/json'
    )

    channel.basic_publish(
        exchange='',
        routing_key='main',
        body=json.dumps(body),
        properties=properties
    )