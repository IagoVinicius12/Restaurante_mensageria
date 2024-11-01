import pika, sys, os

def main():
#    connection = pika.BlockingConnection(pika.ConnectionParameters(host='172.17.0.5'))
#    channel = connection.channel()
    credentials = pika.PlainCredentials('guest', 'guest')
    parameters = pika.ConnectionParameters('localhost',
                                       5672,
                                       '/',
                                       credentials)

    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='restaurante')

    def callback(ch, method, properties, body):
        print(" [x] Entregue o pedido %r" % body.decode())

    channel.basic_consume(queue='restaurante', on_message_callback=callback, auto_ack=True)

    print(' Esperando por mais pedidos')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)