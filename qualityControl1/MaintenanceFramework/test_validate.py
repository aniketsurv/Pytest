import pytest
import json
from datetime import datetime
from connections.Network import IpAddresss
from connections.Constant import constant
from connections.MqttConnection import FrontMqttConnection
from connections.cloudMqttConnection import CloudMqttConnection
from connections import mqttTopics
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
        
    # def test_hub_registration(self):
    #     received_response = False
    #     file_path = "/home/linaro/db/hubKeyVal" 
    #     if os.path.exists(file_path):
    #         with open(file_path, 'r') as file:
    #             if file.read().strip():
    #                 received_response = True
    #     assert received_response, "The file may be empty."
        
    # def test_dbInit(self):
    #     received_response = False
    #     file_path = "/home/linaro/db/dbInit" 
    #     if os.path.exists(file_path):
    #         with open(file_path, 'r') as file:
    #             if file.read().strip():
    #                 received_response = True
    #     assert received_response, "The file may be empty."
            
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
    #     necessaryData = IpAddresss.get_necessary_ids('get_userlist_info_from_hub_db')
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
        
    # def test_get_status_all_process(self):
    #     necessaryData = IpAddresss.get_necessary_ids('get_status_all_process')
    #     requestObj ={
    #         "data":{
    #             "process":"all"
    #             },
    #         "type":"get_status",
    #         "userId": constant.mac_ID,
    #         "communicationId": necessaryData['communicationId'],
    #     } 
    #     received_response = False
    #     FrontMqttConnection.test_sample('process/status/get', requestObj)
    #     time.sleep(5)
    #     if 'get_status_hub' in ResponseMessage.response and ResponseMessage.response['get_status_hub']:
    #         try:
    #             hub_status = ResponseMessage.response['get_status_hub']
    #             if hub_status['type'] == 'get_status_hub':
    #                 for process in hub_status.values():
    #                     if isinstance(process, dict):  # Ensure it's a process object
    #                         action = process.get('action')
    #                         if action in ['connected', 'running', 'init', 'started']:
    #                             print(f"Process {process.get('process', 'Unknown')} is connected (status: {action}).")
    #                         elif action == 'disconnected':
    #                             # print(f"Process {process.get('process', 'Unknown')} is not connected.")
    #                             pytest.fail(f"Process {process.get('process', 'Unknown')} is not connected. Action: {action}")
    #                         else:
    #                             pytest.fail(f"Process {process.get('process', 'Unknown')} has an unknown action: {action}")
    #                 received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_stop_all_process(self):
    #     necessaryData = IpAddresss.get_necessary_ids('stop_all_process')
    #     requestObj = {
    #         "socketId": "socketId-1739340905090",
    #         "dataArray": [
    #             {
    #             "stopAllProcessIndirect": True,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_LATEST": 1,
    #             "CML_PORT": 12312,
    #             "CML_PROCESS_SPEED": "1.80 GHz",
    #             "CML_TOTAL_MEMORY": "3.81 GB",
    #             "CML_VNC_FLAG": 2,
    #             "CREATED_BY": "",
    #             "CREATED_ON": "2025-01-28T05:51:04.915Z",
    #             "DEPT_PROJECT_ID": "cloudsmaintenance.clouzer.com#PRJ_ORG_WKS_1608705805848_7474",
    #             "EDGE_HUB": "1",
    #             "Fixed": False,
    #             "KEY_TYPE": "TSK",
    #             "KEY_VAL": mqttTopics.hubKeyVal,
    #             "publishDirect": False,
    #             "publishIndirect": False,
    #             "pythonLastUpdateTime": "2025-01-29T09:14:50.456Z",
    #             "rebootHubDirect": False
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId": necessaryData['requestId'],
    #         "serverAction": "FETCH_HUB_DETAILS_SERVER",
    #         "essentialList": [
                
    #         ],
    #         "moduleName": "IOE"
    #     } 
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'stopAllProcessIndirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['stopAllProcessIndirect']:
    #         try:
    #             stop_all_process = ResponseMessage.cloud_response['stopAllProcessIndirect']
    #             assert stop_all_process["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert stop_all_process["dataArray"][0]["calmailUpdate"]["stopAllProcessIndirect"] is False, "'stopAllProcessIndirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
        
    # def test_take_remote_access(self):  # set port
    #     necessaryData = IpAddresss.get_necessary_ids('take_remote_access')
    #     requestObj = {
    #         "socketId": "abcd",
    #         "dataArray": [
    #             {
    #             "visibility": 1,
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_PROPERTY_ID": "",
    #             "calmailObject": {
    #                 "CML_PORT": "54321",
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_BY": "monika.suryatale@cloudsmaintenance.clouzer.com",
    #                 "UPDATE_IP": "",
    #                 "CML_VNC_FLAG": 1,
    #                 "takeRemoteAccessDirect": True
    #             }
    #             }
    #         ],
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [],
    #         "requestId": necessaryData['requestId'],
    #         "userId": constant.mac_ID,
    #     }
    #     received_response = False
    #     # CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/CONTROLLER/{mqttTopics.modelNumber}/{mqttTopics.serial}/HUB_REQ', requestObj)
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'takeRemoteAccessDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['takeRemoteAccessDirect']:
    #         try:
    #             takeRemoteAccessResponse = ResponseMessage.cloud_response['takeRemoteAccessDirect']
    #             assert takeRemoteAccessResponse["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert takeRemoteAccessResponse["dataArray"][0]["calmailUpdate"]["takeRemoteAccessDirect"] is False, "'takeRemoteAccessDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_generate_ssh_key(self):  
    #     necessaryData = IpAddresss.get_necessary_ids('generate_ssh_key')
    #     requestObj = {
    #         "socketId": "gDov88xekYs8786NAAHL",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "jymuylyfhkqdd.cloudssbuilderss.clouzer.com#PRJ_ORG_WKS_1738761287736_9877",
    #             "calmailObject": {
    #                 "getSshKeysDirect": True,
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_ON": "2025-02-07T11:06:49.822Z",
    #                 "UPDATE_IP": "",
    #                 "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId":  necessaryData['requestId'],
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'getSshKeysDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['getSshKeysDirect']:
    #         try:
    #             sshKeyResponse = ResponseMessage.cloud_response['getSshKeysDirect']
    #             assert sshKeyResponse["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert sshKeyResponse["dataArray"][0]["calmailUpdate"]["getSshKeysDirect"] is False, "'getSshKeysDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_soft_reset(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('soft_reset')
    #     requestObj = {
    #         "socketId": "ncu5Xi9dbIo3VGspAAPG",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "qvfshrdmsttep.cloudssbuilderss.clouzer.com#PRJ_ORG_WKS_1738759493758_5938",
    #             "calmailObject": {
    #                 "softResetDirect": True,
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_ON": "2025-02-11T11:52:03.107Z",
    #                 "UPDATE_IP": "",
    #                 "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId":  necessaryData['requestId'],
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [
                
    #         ],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'softResetDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['softResetDirect']:
    #         try:
    #             softResetResponsne = ResponseMessage.cloud_response['softResetDirect']
    #             assert softResetResponsne["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert softResetResponsne["dataArray"][0]["calmailUpdate"]["softResetDirect"] is False, "'softResetDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_hard_reset(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('hard_reset')
    #     requestObj ={
    #         "type": "set_hard_reset",
    #         "communicationId": "1739355744233simplehardResethub116",
    #         "data": {
    #             "requestId": necessaryData['requestId'], 
    #             "userId": constant.mac_ID,
    #             "clientId": "v2admin1739355744234simpleclientIdhardResetReq22300"
    #         }
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'hardResetDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['hardResetDirect']:
    #         try:
    #             hardResetResponse = ResponseMessage.cloud_response['hardResetDirect']
    #             assert hardResetResponse["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert hardResetResponse["dataArray"][0]["calmailUpdate"]["hardResetDirect"] is False, "'hardResetDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_start_qc(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('start_qc')
    #     requestObj ={
    #         "socketId": "kAoszd8UDCzxmN1qAAPA",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "",
    #             "essentialList": {
    #                 "REQUEST_STATUS": "PENDING",
    #                 "requestOn": "2025-02-21T07:55:51.091Z",
    #                 "requestType": "direct"
    #             },
    #             "calmailObject": {
    #                 "takeQCReportBackupDirect": True,
    #                 "CML_STAGE": 1,
    #                 "CML_TYPE": "Raw Hub",
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_ON": "2025-02-21T07:55:51.529Z",
    #                 "UPDATE_IP": "",
    #                 "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId": necessaryData['requestId'], 
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'takeQCReportBackupDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['takeQCReportBackupDirect']:
    #         try:
    #             startQcResponse = ResponseMessage.cloud_response['takeQCReportBackupDirect']
    #             assert startQcResponse["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert startQcResponse["dataArray"][0]["calmailUpdate"]["takeQCReportBackupDirect"] is False, "'takeQCReportBackupDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_hub_sync(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('hub_sync')
    #     requestObj ={
    #         "socketId": "bilz35Hx8vkAWLwGAARm",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID":mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "vhcbqzbairafb.cloudssbuilderss.clouzer.com#PRJ_ORG_WKS_1740485664710_9832",
    #             "essentialList": {
    #                 "requestOn": "2025-02-25T13:18:09.166Z"
    #             },
    #             "calmailObject": {
    #                 "CML_ETH_MAC": "B8:2D:28:57:60:4C",
    #                 "CML_MAC_ID": "B8:2D:28:57:60:4C",
    #                 "TYPE": "hub_create_property_sync"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId": necessaryData['requestId'], 
    #         "serverAction": "RESYNC_PROPERTY_MTN_SERVER",
    #         "essentialList": [],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'bulk_update_hub' in ResponseMessage.response and ResponseMessage.response['bulk_update_hub']:
    #         try:
    #             syncResponse = ResponseMessage.response['bulk_update_hub']
    #             assert syncResponse["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert syncResponse["dataArray"][0]["calmailUpdate"]["bulk_update_hub"] is False, "'bulk_update_hub' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        

    # def test_user_crontab(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('user_crontab')
    #     requestObj = {
    #         "socketId": "ivWVfJKyZAGkemL2AAAD",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID":  mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "",
    #             "calmailObject": {
    #                 "resetCronTabUserDirect": True,
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_ON": "2025-02-12T06:03:59.276Z",
    #                 "UPDATE_IP": "",
    #                 "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId": necessaryData['requestId'], 
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [
                
    #         ],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'resetCronTabUserDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['resetCronTabUserDirect']:
    #         try:
    #             userCrontabObj = ResponseMessage.cloud_response['resetCronTabUserDirect']
    #             assert userCrontabObj["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert userCrontabObj["dataArray"][0]["calmailUpdate"]["resetCronTabUserDirect"] is False, "'resetCronTabUserDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_root_crontab(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('root_crontab')
    #     requestObj ={
    #         "socketId": "ivWVfJKyZAGkemL2AAAD",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "",
    #             "calmailObject": {
    #                 "resetCronTabRootDirect": True,
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_ON": "2025-02-12T06:03:59.276",
    #                 "UPDATE_IP": "",
    #                 "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId": necessaryData['requestId'], 
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [
                
    #         ],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'resetCronTabRootDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['resetCronTabRootDirect']:
    #         try:
    #             rootObj = ResponseMessage.cloud_response['resetCronTabRootDirect']
    #             assert rootObj["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert rootObj["dataArray"][0]["calmailUpdate"]["resetCronTabRootDirect"] is False, "'resetCronTabRootDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."
        
    # def test_db_backup_and_restore(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('db_backup_and_restore')
    #     requestObj ={
    #         "socketId": "ivWVfJKyZAGkemL2AAAD",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "",
    #             "calmailObject": {
    #                 "restoreLocalBackupDirect": True,
    #                 "rebootStartTime": "2025-02-12T05:53:12.017Z",
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_ON": "2025-02-12T05:53:14.043Z",
    #                 "UPDATE_IP": "",
    #                 "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId": necessaryData['requestId'], 
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [
                
    #         ],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     if 'restoreLocalBackupDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['restoreLocalBackupDirect']:
    #         try:
    #             rootObj = ResponseMessage.cloud_response['restoreLocalBackupDirect']
    #             rootObj["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
    #             assert rootObj["dataArray"][0]["calmailUpdate"]["restoreLocalBackupDirect"] is False, "'restoreLocalBackupDirect' value is incorrect"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."

    # def test_factory_reset(self): 
    #     necessaryData = IpAddresss.get_necessary_ids('db_backup_and_restore')
    #     requestObj ={
    #         "socketId": "WZ1P2IZz0qkG8Tr7AAPa",
    #         "dataArray": [
    #             {
    #             "CML_HUBSERIAL_ID": mqttTopics.serial,
    #             "CML_HUBAUTH_ID": constant.CODED_HUBID,
    #             "CML_PROPERTY_ID": "smnoplenlwawn.cloudssbuilderss.clouzer.com#PRJ_ORG_WKS_1741331876940_7957",
    #             "calmailObject": {
    #                 "factoryResetDirect": True,
    #                 "rebootStartTime": "2025-03-12T09:30:59.750Z",
    #                 "SYNC_PENDING_STATUS": 0,
    #                 "LAST_MODIFIED_ON": "2025-03-12T09:31:21.816Z",
    #                 "UPDATE_IP": "",
    #                 "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
    #             },
    #             "visibility": 1
    #             }
    #         ],
    #         "userId": constant.mac_ID,
    #         "requestId": necessaryData['requestId'], 
    #         "serverAction": "PERFORM_QUICK_ACTION_SERVER",
    #         "essentialList": [],
    #         "moduleName": "IOE"
    #     }
    #     received_response = False
    #     CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
    #     time.sleep(5)
    #     print("ResponseMessage.cloud_response['factoryresetDirect']",ResponseMessage.cloud_response['factoryresetDirect'])
    #     if 'factoryresetDirect' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['factoryresetDirect']:
    #         try:
    #             rootObj = ResponseMessage.cloud_response['factoryresetDirect']
    #             print("root obj --",rootObj)
    #             rootObj["dataArray"][0]["actionArray"][0] == 'QUICK_ACTION_SUCCESS',"QUICK_ACTION_ERROR generated"
    #             received_response = True
    #         except Exception as e:
    #             pytest.fail(f"Error in parsing received message: {e}")
    #     assert received_response, "Expected response not received."


    def test_reset_hub_network(self):
        necessaryData = IpAddresss.get_necessary_ids('stop_all_process')
        requestObj ={
            "socketId": "WZ1P2IZz0qkG8Tr7AAPa",
            "dataArray": [
                {
                "CML_HUBSERIAL_ID": mqttTopics.serial,
                "CML_HUBAUTH_ID": constant.CODED_HUBID,
                "CML_PROPERTY_ID": "smnoplenlwawn.cloudssbuilderss.clouzer.com#PRJ_ORG_WKS_1741331876940_7957",
                "calmailObject": {
                    "resetHubNetwork": True,
                    "rebootStartTime": "2025-03-12T09:30:59.750Z",
                    "SYNC_PENDING_STATUS": 0,
                    "LAST_MODIFIED_ON": "2025-03-12T09:31:21.816Z",
                    "UPDATE_IP": "",
                    "LAST_MODIFIED_BY": "ankita.chavan@cloudsmaintenance.clouzer.com"
                },
                "visibility": 1
                }
            ],
            "userId": constant.mac_ID,
            "requestId": necessaryData['requestId'], 
            "serverAction": "PERFORM_QUICK_ACTION_SERVER",
            "essentialList": [],
            "moduleName": "IOE"
        }
        received_response = False
        CloudMqttConnection.test_sample(f'{mqttTopics.NameSpaceId}/{mqttTopics.modelNumber}/{mqttTopics.serial}/MTN_TO_HUB', requestObj)
        time.sleep(15)
        if 'resetHubNetwork' in ResponseMessage.cloud_response and ResponseMessage.cloud_response['resetHubNetwork']:
            try:
                stop_all_process = ResponseMessage.cloud_response['resetHubNetwork']
                assert stop_all_process["dataArray"][0]["actionArray"][0] == "QUICK_ACTION_SUCCESS","QUICK_ACTION_ERROR generated"
                assert stop_all_process["dataArray"][0]["calmailUpdate"]["resetHubNetwork"] is False, "'resetHubNetwork' value is incorrect"
                received_response = True
            except Exception as e:
                pytest.fail(f"Error in parsing received message: {e}")
        assert received_response, "Expected response not received."

        
        
        
        