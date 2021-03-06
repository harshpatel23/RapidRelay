from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json
from credentials import server_ip
import datetime

app = Flask(__name__)
broker_address = server_ip
client = mqtt.Client("P1")
client.connect(broker_address, port=1883)


def on_connect(mqtt_client, obj, flags, rc):
    print("ON CONNECT")

client.on_connect = on_connect


@app.route('/data/read', methods=['GET', 'POST'])
def read():
    # Publish data to broker
    data = request.json
    string_data = json.dumps(data)
    if data['type'] == "weather":
        client.publish("queue_weather", string_data)
    elif data['type'] == "agriculture":
        client.publish("queue_agriculture", string_data)
    elif data['type'] == "air":
        client.publish("queue_air_quality", string_data)

    return "OK"


if __name__ == "__main__":
    app.run('0.0.0.0')
