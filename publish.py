#!/usr/bin/env python

import pika
import time

credentials = pika.PlainCredentials('guest', 'guest')
conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost',credentials=credentials))
ch   = conn.channel()

ch.exchange_declare(exchange="e", exchange_type="x-consistent-hash", durable=True)

n = 100

for rk in list(map(lambda s: str(s), range(0, n))):
    ch.basic_publish(exchange="e", routing_key=rk, body="")
print("Done publishing.")

print("Waiting for routing to finish...")
# in order to keep this example simpler and focused,
# wait for a few seconds instead of using publisher confirms and waiting for those
time.sleep(5)

print("Done.")
conn.close()