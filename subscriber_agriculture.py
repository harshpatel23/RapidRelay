import paho.mqtt.client as mqtt  # import the client1
import time
import json
import mysql.connector as mysql


# Database connection
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = ""
)


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

    msg = json.loads(message)
    print(str(msg))




broker_address = "10.0.15.92"
queue_name = "queue_agriculture"

print("creating new instance")
client = mqtt.Client("P2")  # create new instance
client.on_message = on_message  # attach function to callback
print("connecting to broker")

client.connect(broker_address, port=1883)  # connect to broker
client.loop_start()  # start the loop
print("Subscribing to topic ", queue_name)
client.subscribe(queue_name)

time.sleep(4)  # wait
# client.loop_stop()  # stop the loop