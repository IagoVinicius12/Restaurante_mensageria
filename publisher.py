import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='restaurante')
str=input("Digite o pedido:")

channel.basic_publish(exchange='', routing_key='restaurante', body=str)
print(" O pedido está sendo preparado!!!")
connection.close()


