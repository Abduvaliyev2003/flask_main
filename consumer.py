import pika

from main import Product, db

params = pika.ConnectionParameters('amqps://nhzsened:sghwS0lh1e9inlPPL40Zs2AU53RAVzCJ@capybara.lmq.cloudamqp.com/nhzsened   ')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main', durable=True)


def callback(ch, method, properties, body):
    print('Received')
    data = json.loads(body)

    print(data)
    if properties.content_type == 'product_created':
        product = Product.objects.get(id=data['id'], title=data['title'], image=data['image'])
        db.session.commit(product)
    elif properties.content_type == 'product_updated':
        product = Product.objects.get(id=data['id'])
        product.title = data['title']
        product.image = data['image']
        db.session.commit(product)
    elif properties.content_type == 'product_deleted':
        product = Product.objects.get(data)
        db.session.delete(product)
        db.session.commit(product)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('start')

channel.start_consuming()

channel.close()