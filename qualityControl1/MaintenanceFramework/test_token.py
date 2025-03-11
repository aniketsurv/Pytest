import requests
import pytest
from connections.Network import IpAddresss
from connections.Constant import constant
import logging

logger = logging.getLogger("TestTokens")

class TestTokens:
            
    def test_set_client_token(self):
        try:
            necessaryData = IpAddresss.get_necessary_ids('admin@clouzer.com')
            BROKER_HOST = IpAddresss.get_ip_address()
            file_path = "/home/linaro/db/CODED_HUBID"
            password=""
            with open(file_path, 'r') as file:
                password = file.read().strip()
            url = f"http://{BROKER_HOST}:3000/getClientTokenauth"
            reqestObject = {
                "data":{
                    "type":"authenticate_user",
                    "requestId": necessaryData['requestId'],
                    "userId": IpAddresss.get_mac_address(),
                    "CallerInfo":{
                        "caller":"RemoteMqttConnection_background_call",
                        "portalAction":False,
                        "source":["iOS_ClouzerEdge"]
                    },
                    "clientId": constant.clientId,
                    "dataArray":[{
                        "deviceName":"Xiaomi21091116Iplkjhgvc",
                        "deviceType":"ioscrontroller",
                        "device_id":"TP1A.220624.54678",
                        "entity_type":"userConnectionMap",
                        "ip":BROKER_HOST,
                        "location":"India",
                        "password":password,
                        "userName":IpAddresss.get_mac_address(),
                        "version":"33"
                        }]
                },
                "communicationId":necessaryData['communicationId']
            }
            logger.trace("set_client_token - Request: %s", reqestObject)
            response = requests.post(url, json=reqestObject, timeout=20)
            logger.trace("set_client_token_response - Response: %s", response.text)
            response_json = response.json()
            assert response.status_code == 200, f"Expected status code 200 but got {response.status_code}"
            assert response_json['dataArray'][0]['userName'] == reqestObject['data']['dataArray'][0]['userName'] ,"userName missmatch"
            assert response_json['dataArray'][0]['password'] == reqestObject['data']['dataArray'][0]['password'] ,"password missmatch"
            constant.clientObjectCache.update(response_json)
       
        except Exception as e:
            pytest.fail(f"Error:{e}")