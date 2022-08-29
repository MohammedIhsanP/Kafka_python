from kafka import KafkaConsumer
import sys

topic = "nestDigital"
server = "localhost:9092"

consumer = KafkaConsumer(topic, bootstrap_servers=server, auto_offset_reset = 'earliest')
try :
    for message in consumer:
        data = message.value
        partition = message.partition
        print(data.decode())
        print(partition)
except KeyboardInterrupt :
    sys.exit()