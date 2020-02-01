import paho.mqtt.client as mqtt  # import the client1

broker_address = "10.0.15.92"

client = mqtt.Client("P1")  # create new instance
client.connect(broker_address, port=1883)  # connect to broker
client.publish("Mumbai", "OFF")  # publish
