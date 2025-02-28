import pytest
import json
from datetime import datetime
from connections.Network import IpAddresss
from connections.Constant import constant
from connections.MqttConnection import FrontMqttConnection
import time
from connections.Response import ResponseMessage
import os

class TestPercentage:
    
    # def test_send_percentage(self):
    #         sendPercentageObj = {
    #             "type": "send_percentage",
    #             "data": {
    #                 "operation": "process",
    #                 "process": "edgemaintenance",
    #                 "percentage": 100,
    #                 "status": "edgemaintenance is initiated",
    #                 "ts": 1739360908574,
    #                 "containerId": "edgemaintenance"
    #             }
    #         }
    #         received_response = False
    #         FrontMqttConnection.test_sample('percentage/send', sendPercentageObj)
    #         time.sleep(5)
    #         if 'update_percentage' in ResponseMessage.response and ResponseMessage.response['update_percentage']:
    #             try:
    #                 sysCredentials = ResponseMessage.response['update_percentage']
    #                 if sysCredentials.get('type') == 'update_percentage':
    #                     received_response = True
    #             except Exception as e:
    #                 pytest.fail(f"Error in parsing received message: {e}")
    #         assert received_response, "Expected response not received."
            
    # def test_get_hub_info_from_hub_db(self):
    #     necessaryData = IpAddresss.get_necessary_ids('get_network_info_from_hub_db')
        
    #     requestObj = {
    #         "data": {
    #             "entity_type": "hubInfo"
    #         },
    #         "communicationId": necessaryData['requestId'],
    #         "clientId": constant.clientId,
    #     }
    #     received_response = False
    #     FrontMqttConnection.test_sample('soulDb/fetch', requestObj)
    #     time.sleep(10)
    #     if 'dbFetch' in ResponseMessage.response and ResponseMessage.response['dbFetch']:
    #         try:
    #             sysCredentials = ResponseMessage.response['dbFetch']
    #             if sysCredentials.get('type') == 'dbFetch':
    #                 assert len(sysCredentials.get('data', [])) > 0, 'Some system credential values are not available'
    #                 received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
            
    # def test_get_network_info_from_hub_db(self):
    #     necessaryData = IpAddresss.get_necessary_ids('get_network_info_from_hub_db')
        
    #     requestObj = {
    #         "data": {
    #             "entity_type": "network"
    #         },
    #         "communicationId": necessaryData['requestId'],
    #         "clientId": constant.clientId,
    #     }
    #     received_response = False
    #     FrontMqttConnection.test_sample('soulDb/fetch', requestObj)
    #     time.sleep(10)
    #     if 'dbFetch' in ResponseMessage.response and ResponseMessage.response['dbFetch']:
    #         try:
    #             sysCredentials = ResponseMessage.response['dbFetch']
    #             if sysCredentials.get('type') == 'dbFetch':
    #                 assert len(sysCredentials.get('data', [])) > 0, 'Some system credential values are not available'
    #                 received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_get_firmware_info_from_hub_db(self):
    #     necessaryData = IpAddresss.get_necessary_ids('get_network_info_from_hub_db')
        
    #     requestObj = {
    #         "data": {
    #             "entity_type": "firmware"
    #         },
    #         "communicationId": necessaryData['requestId'],
    #         "clientId": constant.clientId,
    #     }
    #     received_response = False
    #     FrontMqttConnection.test_sample('soulDb/fetch', requestObj)
    #     time.sleep(10)
    #     if 'dbFetch' in ResponseMessage.response and ResponseMessage.response['dbFetch']:
    #         try:
    #             sysCredentials = ResponseMessage.response['dbFetch']
    #             if sysCredentials.get('type') == 'dbFetch':
    #                 assert len(sysCredentials.get('data', [])) > 0, 'Some system credential values are not available'
    #                 received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_get_system_credentials_info_from_hub_db(self):
    #     necessaryData = IpAddresss.get_necessary_ids('get_network_info_from_hub_db')
        
    #     requestObj = {
    #         "data": {
    #             "entity_type": "system_credentials"
    #         },
    #         "communicationId": necessaryData['requestId'],
    #         "clientId": constant.clientId,
    #     }
    #     received_response = False
    #     FrontMqttConnection.test_sample('soulDb/fetch', requestObj)
    #     time.sleep(10)
    #     if 'dbFetch' in ResponseMessage.response and ResponseMessage.response['dbFetch']:
    #         try:
    #             sysCredentials = ResponseMessage.response['dbFetch']
    #             if sysCredentials.get('type') == 'dbFetch':
    #                 assert len(sysCredentials.get('data', [])) > 0, 'Some system credential values are not available'
    #                 received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    def test_hub_registration(self):
        received_response = False
        file_path = "/home/linaro/db/hubKeyVal" 
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                if file.read().strip():
                    received_response = True
        assert received_response, "The file may be empty."
        
    def test_dbInit(self):
        received_response = False
        file_path = "/home/linaro/db/dbInit" 
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                if file.read().strip():
                    received_response = True
        assert received_response, "The file may be empty."
            
    # def test_get_scene_info_from_hub_db(self):
    #     necessaryData = IpAddresss.get_necessary_ids('get_network_info_from_hub_db')
    #     requestObj = {
    #         "data": {
    #             "entity_type": "scene"
    #         },
    #         "communicationId": necessaryData['requestId'],
    #         "clientId": constant.clientId,
    #     }
    #     received_response = False
    #     FrontMqttConnection.test_sample('soulDb/fetch', requestObj)
    #     time.sleep(10)
    #     ids_to_check = [730, 308]
    #     if 'dbFetch' in ResponseMessage.response and ResponseMessage.response['dbFetch']:
    #         try:
    #             sysCredentials = ResponseMessage.response['dbFetch']
    #             if sysCredentials.get('type') == 'dbFetch':
    #                 present_ids = [item["ID"] for item in sysCredentials["data"] if item["ID"] in ids_to_check]
    #                 assert len(sysCredentials.get('data', [])) > 0, 'Some system credential values are not available'
    #                 assert 308 in present_ids, "ID 308 should be present in data"
    #                 assert 730 in present_ids, "ID 730 should be present in data"
    #                 received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_get_userlist_info_from_hub_db(self):
    #     necessaryData = IpAddresss.get_necessary_ids('get_network_info_from_hub_db')
    #     requestObj = {
    #         "data": {
    #             "entity_type": "userlist"
    #         },
    #         "communicationId": necessaryData['requestId'],
    #         "clientId": constant.clientId,
    #     }
    #     received_response = False
    #     FrontMqttConnection.test_sample('soulDb/fetch', requestObj)
    #     time.sleep(10)
    #     macAdress = IpAddresss.get_mac_address()
    #     if 'dbFetch' in ResponseMessage.response and ResponseMessage.response['dbFetch']:
    #         try:
    #             sysCredentials = ResponseMessage.response['dbFetch']
    #             if sysCredentials.get('type') == 'dbFetch':
    #                 macUserFound = any(user["username"] == macAdress for user in sysCredentials["data"])
    #                 assert len(sysCredentials.get('data', [])) > 0, 'Some system credential values are not available'
    #                 assert macUserFound, f"MAC address {macAdress} not found in the response data"
    #                 received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    def test_get_userlist_info_from_hub_db(self):
        necessaryData = IpAddresss.get_necessary_ids('get_network_info_from_hub_db')
        requestObj ={
            "data":{
                "process":"all"
                },
            "type":"get_status",
            "userId": constant.mac_ID,
            "communicationId": necessaryData['communicationId'],
        } 
        received_response = False
        FrontMqttConnection.test_sample('process/status/get', requestObj)
        time.sleep(5)
        if 'get_status_hub' in ResponseMessage.response and ResponseMessage.response['get_status_hub']:
            try:
                hub_status = ResponseMessage.response['get_status_hub']
                if hub_status['type'] == 'get_status_hub':
                    for process in hub_status.values():
                        if isinstance(process, dict):  # Ensure it's a process object
                            action = process.get('action')
                            if action in ['connected', 'running', 'init', 'started']:
                                print(f"Process {process.get('process', 'Unknown')} is connected (status: {action}).")
                            elif action == 'disconnected':
                                # print(f"Process {process.get('process', 'Unknown')} is not connected.")
                                pytest.fail(f"Process {process.get('process', 'Unknown')} is not connected. Action: {action}")
                            else:
                                pytest.fail(f"Process {process.get('process', 'Unknown')} has an unknown action: {action}")
                    received_response = True
            except Exception as e:
                pytest.fail(f"Error in parsing received message: {e}")
        assert received_response, "Expected response not received."