#!/usr/bin/env python

import pika
import time
import hashlib

credentials = pika.PlainCredentials('guest', 'guest')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
ch   = conn.channel()

queue_name="q4"
host_name="host_name4"

ch.queue_declare(queue=queue_name, durable=True)
#ch.queue_purge(queue=queue_name)

ch.queue_bind(exchange="e", queue=queue_name, routing_key="1")
ch.queue_bind(exchange="e", queue=queue_name, routing_key="2")

print(' [*] Waiting for logs. To exit press CTRL+C')
def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body,))

ch.basic_consume(callback,queue=queue_name,no_ack=True)
ch.start_consuming()
