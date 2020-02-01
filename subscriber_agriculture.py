import paho.mqtt.client as mqtt  # import the client1
import json
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='bugbox_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


broker_address = "10.0.15.92"
queue_name = "queue_agriculture"
count = 0


def on_message(client, userdata, message):
    global count
    msg = json.loads(str(message.payload.decode("utf-8")))
    # print(str(msg))
    with connection.cursor() as cursor:
        sql = "INSERT INTO `agriculture_data` (`time`, `greenhouse_id`, `humidity`, `temperature`, `moisture`) " \
              "VALUES ('"+str(msg['time'])+"',"+str(msg['greenhouse_id'])+","+ str(msg['humidity'])+","+str(msg['temperature'])+","+ str(msg['moisture'])+")"
        # print(sql)
        cursor.execute(sql)
        count = count + 1

    if count % 500 == 0:
        connection.commit()
        print(str(msg))
        count = 0


def on_connect(mqtt_client, obj, flags, rc):
    print("Subscribing to topic ", queue_name)
    mqtt_client.subscribe(queue_name)


print("creating new instance")
client = mqtt.Client("P2")  # create new instance
client.on_message = on_message  # attach function to callback
client.on_connect = on_connect
print("connecting to broker")
client.connect(broker_address, port=1883)  # connect to broker

client.loop_forever()
