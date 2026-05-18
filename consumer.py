import pika

params = pika.ConnectionParameters('amqps://nhzsened:sghwS0lh1e9inlPPL40Zs2AU53RAVzCJ@capybara.lmq.cloudamqp.com/nhzsened   ')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main', durable=True)

def callback(ch, method, properties, body):
    pass

channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('start')

channel.start_consuming()

channel.close()