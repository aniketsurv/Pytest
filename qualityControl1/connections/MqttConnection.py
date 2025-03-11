#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:18:21 2025

@author: developers
"""

import paho.mqtt.client as mqtt
import json
import time
from connections.Network import IpAddresss
import logging
from connections.Response import ResponseMessage
from connections import mqttTopics

class FrontMqttConnection:
    
    logger = logging.getLogger("FrontMqttConnection")
    received_message = None
    __client = None
    
    @classmethod
    def get_client(cls):
        return cls.__client
    
    @classmethod
    def on_connect(cls, client, userdata, flags, rc):
        try:
            print(f"Connected with result code {rc}")
            if rc == 0:
                client.subscribe(mqttTopics.RequestTopic, qos=mqttTopics.QOS)
                print(f"Subscribed to topic: {mqttTopics.RequestTopic}")
            else:
                print(f"Connection failed with code {rc}. Check credentials or broker availability.")
        except Exception as e:
            print("Exception in on_connect method -->", e)

    @classmethod
    def on_disconnect(cls, client, userdata, rc):
        try:
            """This function is called when the client disconnects."""
            #print(f"Disconnected with code {rc}")
            if rc != 0:
                #print("Reconnecting...")
                client.reconnect()
            else:
                print("Gracefully disconnected.")
        except Exception as e:
            print("Exception in on_disconnect method -->", e)

    @classmethod
    def on_message(cls, client, userdata, msg):
        try:
            print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")
            obj = json.loads(msg.payload.decode())
            # Check if the 'type' from the received message exists as a key in 'response'
            if obj['type'] in ResponseMessage.response:
                ResponseMessage.response[obj['type']] = obj
                print(f"Updated response for {obj['type']}")
            else:
                print(f"Unknown type received: {obj['type']}")
        except Exception as e:
            print("Exception in on_message method -->", e)
    
    @classmethod        
    def on_publish(cls, client, userdata, mid):
        try:
            print(f"Message with mid {mid} successfully published.")
            FrontMqttConnection.received_message = {"type":"sucess"}
        except Exception as e:
            print("Error inside on_publish : ",e) 

    @classmethod
    def wait_for_message(cls, timeout):
        """Wait for a message to be received or timeout after a certain period."""
        start_time = time.time()
        while cls.received_message is None:
            if time.time() - start_time > timeout:
                raise TimeoutError("Message not received within the timeout period.")
            time.sleep(0.5)  # Check every 500ms
        
    @classmethod
    def test_sample(cls,topic,req_obj_provision):
        try:
            FrontMqttConnection.received_message = None
            for key in ResponseMessage.response.keys():
                ResponseMessage.response[key] = {}  # Empty each key's value
            print("Request_object: ", req_obj_provision)
            cls.__client.publish(topic, json.dumps(req_obj_provision))
        except Exception as e:
            print("Exception in test_sample method -->", e)
            
    @classmethod
    def client_connection(cls):
        """Test sample method that connects to broker, subscribes, and publishes a message."""
        BROKER_PORT = 8886
        BROKER_HOST = IpAddresss.get_ip_address()
        
        # Initialize the MQTT client
        cls.__client = mqtt.Client("PytestMqttConnector")
        cls.__client.username_pw_set(username="CEDPython", password="@$0uL|?yT#0n")
        
        # Bind events
        cls.__client.on_connect = cls.on_connect
        cls.__client.on_disconnect = cls.on_disconnect
        cls.__client.on_message = cls.on_message
        cls.__client.on_publish = cls.on_publish
        
        cls.__client.connect(BROKER_HOST, BROKER_PORT, 60)  # 60 seconds keep-alive
        cls.__client.loop_start()
        time.sleep(2)
            
    @classmethod
    def client_disconnect(cls):
        cls.__client.loop_stop()  # Stop the loop
        cls.__client.disconnect()  # Disconnect from the broker
