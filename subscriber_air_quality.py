import paho.mqtt.client as mqtt  # import the client1
import json

broker_address = "10.0.15.92"
queue_name = "queue_air_quality"


def on_message(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))
    print("message topic=", message.topic)
    print("message qos=", message.qos)
    print("message retain flag=", message.retain)

    msg = json.loads(message)
    print(str(msg))


def on_connect(mqtt_client, obj, flags, rc):
    print("Subscribing to topic ", queue_name)
    mqtt_client.subscribe(queue_name)


print("creating new instance")
client = mqtt.Client("P4")  # create new instance
client.on_message = on_message  # attach function to callback
client.on_connect = on_connect
print("connecting to broker")
client.connect(broker_address, port=1883)  # connect to broker

client.loop_forever()
