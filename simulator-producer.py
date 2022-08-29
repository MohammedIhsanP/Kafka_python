import random
import time
from kafka import KafkaProducer

topic = "TempMonitoringSystem"
server = "localhost:9092"


while True:
    random_temp = random.randrange(10,40)
    print(random_temp)
    producer = KafkaProducer(bootstrap_servers = [server])
    message = producer.send(topic, bytes(str(random_temp), encoding='utf-8'))
    time.sleep(10.0)



