import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='restaurante')
str=input("Digite o seu pedido:")

channel.basic_publish(exchange='', routing_key='restaurante', body=str)
print(" Seu pedido está sendo preparado!!!")
connection.close()


