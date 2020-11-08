from time import strftime
import paho.mqtt.client as mqtt
import sqlite3

temperature_topic = "temperature"
humidity_topic = "humidity"
pressure_topic = "pressure"
dbFile = "espData.db"

dataTuple = [-1,-1,-1]

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(temperature_topic)
    client.subscribe(humidity_topic)
    client.subscribe(pressure_topic)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    theTime = strftime("%Y-%m-%d %H:%M:%S")

    result = (theTime + "\t" + str(msg.payload))
    print(msg.topic + ":\t" + result)
    if msg.topic == temperature_topic:
        dataTuple[0] = double(msg.payload)[2:-1]
        print(str(msg.payload)[2:-1])
        print(str(msg.payload[2:-1]))
    if msg.topic == humidity_topic:
        dataTuple[1] = double(msg.payload)[2:-1]
        #return
    if msg.topic == pressure_topic:
        dataTuple[2] = double(msg.payload)[2:-1]
    if dataTuple[0] != -1 and dataTuple[1] != -1 and dataTuple[2] != -1:
        writeToDb(theTime, dataTuple[0], dataTuple[1], dataTuple[2])
    return

def writeToDb(theTime, temperature, humidity, pressure):
    conn = sqlite3.connect(dbFile)
    c = conn.cursor()
    print("Writing to db...")
    c.execute("INSERT INTO ESP_data VALUES (?,?,?,?)", (theTime, temperature, humidity, pressure))
    conn.commit()

    global dataTuple
    dataTuple = [-1, -1, -1]

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set("admin", "admin")
client.connect("192.168.2.24", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
