import paho.mqtt.client as mqtt  # import the client1
import time


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)


broker_address = "10.0.15.92"

print("creating new instance")
client = mqtt.Client("P2")  # create new instance
client.on_message = on_message  # attach function to callback
print("connecting to broker")

client.connect(broker_address, port=1883)  # connect to broker
client.loop_start()  # start the loop
print("Subscribing to topic", "Mumbai")
client.subscribe("Mumbai")

time.sleep(4)  # wait
client.loop_stop()  # stop the loop
