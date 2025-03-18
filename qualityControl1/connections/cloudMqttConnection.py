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
from connections.Network import IpAddresss
import ssl

CODED_HUBID = IpAddresss.read_file(f"/home/linaro/db/CODED_HUBID").strip()
server = IpAddresss.read_file(f"/home/linaro/db/server").strip()
SERIAL = IpAddresss.read_file(f"/home/linaro/db/serial").strip()
modelNumber = IpAddresss.read_file(f"/home/linaro/db/modelNumber").strip()

hive_options = {
    'broker_port': 31160,
    'username': f"{SERIAL}_{modelNumber}" ,
    'password': CODED_HUBID,
    'broker_url':server.split('//')[1],
    'tls': True  
}

class CloudMqttConnection:
    
    logger = logging.getLogger("CloudMqttConnection")
    received_message = None
    __client = None
    
    @classmethod
    def get_client(cls):
        return cls.__client
    
    @classmethod
    def on_connect(cls, client, userdata, flags, rc):
        try:
            print(f"Cloud connected with result code {rc}")
            if rc == 0:
                client.subscribe(mqttTopics.cloudTopic, qos=mqttTopics.QOS)
                print(f"Subscribed to topic: {mqttTopics.cloudTopic}")
            else:
                print(f"Connection failed with code {rc}. Check credentials or broker availability.")
        except Exception as e:
            print("Exception in on_connect method -->", e)

    @classmethod
    def on_disconnect(cls, client, userdata, rc):
        try:
            """This function is called when the client disconnects."""
            print(f"Disconnected cloud connection with code {rc}")
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
            if obj["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS":
                calmail_update = obj["dataArray"][0]["calmailUpdate"]
                for key in ResponseMessage.cloud_response:
                    if any(key in item for item in calmail_update):
                        ResponseMessage.cloud_response[key] = obj
                print(f"Updated cloud_response for {obj}")
            else:
                print(f"Unknown type received: {obj}")
        except Exception as e:
            print("Exception in on_message method -->", e)
    
    @classmethod        
    def on_publish(cls, client, userdata, mid):
        try:
            print(f"Message with mid {mid} successfully published.")
            cls.received_message = {"type":"sucess"}
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
            cls.received_message = None
            for key in ResponseMessage.cloud_response.keys():
                ResponseMessage.cloud_response[key] = {}  # Empty each key's value
            print(f"topic {topic}   Request_object: {req_obj_provision}")
            cls.__client.publish(topic, json.dumps(req_obj_provision))
        except Exception as e:
            print("Exception in test_sample method -->", e)
            
    @classmethod
    def cloud_connection(cls):
        """Test sample method that connects to broker, subscribes, and publishes a message."""

        # Initialize the MQTT client
        cls.__client = mqtt.Client("SOULSYSTEM_CloudConnector")
        cls.__client.username_pw_set(username=hive_options["username"], password=hive_options["password"])
        if hive_options['tls']:
            cls.__client.tls_set(certfile=None, keyfile=None, tls_version=ssl.PROTOCOL_TLSv1_2)
            cls.__client.tls_insecure_set(True)
        
        # Bind events
        cls.__client.on_connect = cls.on_connect
        cls.__client.on_disconnect = cls.on_disconnect
        cls.__client.on_message = cls.on_message
        cls.__client.on_publish = cls.on_publish
        
        cls.__client.connect(hive_options["broker_url"], hive_options['broker_port'], 60)  # 60 seconds keep-alive
        cls.__client.loop_start()
        time.sleep(2)
            
    @classmethod
    def client_disconnect(cls):
        cls.__client.loop_stop()  # Stop the loop
        cls.__client.disconnect()  # Disconnect from the broker
