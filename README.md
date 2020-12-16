# IoT Project
Connecting the Raspberry Pi with an ESP32 and BME280. Sensordata from the BME280 is sent via the ESP32 to the MQTT-broker of the Raspberry Pi (connection over SSL).
The Raspberry Pi saves the data in the SQLite3 database, which a small webserver on the Raspberry Pi will use to show data in graphs. 

# Libaries used
* Paho MQTT Client
* SQLite3
* Azure IoT Device
* SSL
