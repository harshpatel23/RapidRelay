from flask import Flask, request, jsonify
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)
broker_address = "10.0.15.92"
client = mqtt.Client("P1")
client.connect(broker_address, port=1883)


@app.route('/data/read', methods=['GET', 'POST'])
def read():
    # Publish data to broker
    data = request.json
    string_data = json.dumps(data)
    print(string_data)
    if data['type'] == "weather":
        client.publish("queue_weather", string_data)
    elif data['type'] == "agriculture":
        client.publish("queue_agriculture", string_data)
    elif data['type'] == "air":
        client.publish("queue_air_quality", string_data)

    return None
