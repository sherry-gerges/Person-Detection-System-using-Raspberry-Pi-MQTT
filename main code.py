import paho.mqtt.client as mqtt 
import ssl 
import time 
from gpiozero import LineSensor 
from signal import pause  
 
sensor = LineSensor(17) 
 
MQTT_HOST="f7559e3e38f94eb7bfc2906b6be26633.s1.eu.hivemq.cloud"  
MQTT_PORT= 8883 
USERNAME="sherrymegally" 
PASSWORD="*********" 
 
client = mqtt.Client() 
client.username_pw_set(USERNAME, PASSWORD) 
client.tls_set(cert_reqs=ssl.CERT_REQUIRED) 
 
client.connect(MQTT_HOST, MQTT_PORT, 60) 
 
while True: 
    payload = sensor.value 
    client.publish("SIC/support", payload) 
 
    if payload == 1: 
        print("Person detected") 
         
    else: 
        print("No person detected")  
           
    time.sleep(3) 
    
