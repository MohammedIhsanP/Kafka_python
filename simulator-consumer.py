from kafka import KafkaConsumer
import sys
import mysql.connector

server_name="localhost"
db_username="root"
db_password=""
db_name="iot_db"

connection=mysql.connector.connect(host=server_name, 
                                    user=db_username, 
                                    password=db_password, 
                                    database=db_name)

mycursor=connection.cursor()

topic = "TempMonitoringSystem"
server = "localhost:9092"

consumer = KafkaConsumer(topic, bootstrap_servers=server, auto_offset_reset = 'earliest')
try :
    for message in consumer:
        data = message.value
        data_val=data.decode()
        print(data_val)
        mycursor.execute("INSERT INTO `temperature`(`Temperature`) VALUES ("+data_val+")")
        connection.commit()
except KeyboardInterrupt :
    sys.exit()