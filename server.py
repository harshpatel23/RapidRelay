from flask import Flask
import paho.mqtt.client as mqtt


app = Flask(__name__)
broker_address = "10.0.15.92"
client = mqtt.Client("P1")


@app.route('/data/read', methods=['GET', 'POST'])
def read():
    # Publish data to broker
    return None

