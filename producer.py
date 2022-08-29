from kafka import KafkaProducer
Output = input("Enter the data to be send:")
print(Output)

topic = "nestDigital"
server = "localhost:9092"

producer = KafkaProducer(bootstrap_servers = [server])
message = producer.send(topic, bytes(Output, encoding='utf-8'))
metadata = message.get()
print(metadata.topic)
print(metadata.partition)