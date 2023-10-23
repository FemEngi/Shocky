# python 3.8

import random
import time

import customtkinter
import random
import socket
import requests
import logging

import esptool
import multiprocessing
from multiprocessing import freeze_support


import gui

from paho.mqtt import client as mqtt_client

import requests
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

broker = 'o3c314d6.ala.us-east-1.emqxsl.com'
port = 8883

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'data'
password = 'HcYJiB5QeuJPpgC'


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    def on_publish(client, userdata, mid):
        print("haiii12345")

    client = mqtt_client.Client(client_id)
    client.tls_set(ca_certs=resource_path('emqxsl-ca.crt'))
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_publish = on_publish
    
    client.connect(broker, port)
    
    return client


def publish(client: mqtt_client, key, msg):
    topic = key #"+ mqtt/python/mqtt/" 
    msg_count = 0
    time.sleep(1)
    result = client.publish(topic, msg)
    # result: [0, 1]
    status = result[0]
    if status == 0:
        print(f"Send `{msg}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")


def init(key=-1):
    if key==-1:
        key = str(random.randint(0, 9999))
    if key=="":
        return "no"
    topic = key #+ "mqtt/python/mqtt/"
    client = connect_mqtt()
    # publish(client, key, bytearray([128,128,128]))
    return client, key

def senddata(client, key, message):
    topic = "mqtt/python/mqtt/"+key
    publish(client, topic, message)
    print(topic)
 
def on_message(client, userdata, msg):
    print("gay")
    print(gui.URL1+msg.payload.decode())
    requested=msg.payload.decode()
    gui.nbrq2(requested)
    
def subscribesys(client: mqtt_client, key):
    topic = "mqtt/python/mqtt/"+key

    client.subscribe(topic)
    client.on_message = on_message
    print("subscribed to "+broker+topic)
    client.loop_start()


def unsubscribe(client: mqtt_client, topic):
    client.unsubscribe(topic)
    client.loop_stop(force=False)

# def on_subscribe(client, userdata, msg):
#     requests.get(url = (gui.URL1+str(msg.payload.decode())))


    

if __name__ == '__main__':
    
    gui.init_customtkinter()
    # client, key = init()
    while True:
        gui.customtkinterloop()
    print("haii")
    

    # subscribe(client, "mqtt/python/mqtt/" + key)
    # senddata(client, key, bytearray([1,2,3]))

