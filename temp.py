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

temp_value=input("Enter your temperature value:")
print(temp_value)

mycursor.execute("INSERT INTO `temperature`(`Temperature`) VALUES ("+temp_value+")")
connection.commit()
print("Data inserted successfully")