import os
import subprocess
import tarfile
import time
import json
from pathlib import Path
import requests
from connections.MqttConnection import FrontMqttConnection
from connections.cloudMqttConnection import CloudMqttConnection
from connections.Container import checkDocker
from connections.Network import IpAddresss

from utils import logConfig
logConfig.setup_logging()

class TestRunner:
    
    # def send_report_path(self,response):
    #     api_url = "http://0.0.0.0:3000/QCPath"
    #     headers = {
    #         "Content-Type": "application/json"
    #     }  
    #     data = json.dumps(response)
    #     print(f"report details - {data}")
    #     response = requests.post(api_url,data=data, headers=headers)
    #     print(f"report details response - {response}")
        
    def send_report_path(self,response):
        data = json.dumps(response)
        necessaryData = IpAddresss.get_necessary_ids('send_report_path')
        file_size_in_bytes = os.path.getsize("reports.tar.gz")
        file_size_in_mb = file_size_in_bytes / (1024 * 1024)
        requestObj= {
            "data": {
                "type": "send_path",
                "path": data['uploadFiles'][0]['path'],
                "FILE_SIZE": f"{file_size_in_mb} MB",
                "msg": "Upload QC Report Direct action performed successfully." 
            },
            "communicationId": necessaryData['requestId'],  
        }
        # requestObj = { 
        #             "type":"send_path",
        #             "data": data,
        #             "FILE_SIZE": f"{file_size_in_mb} MB",
        #             "msg": "Upload QC Report Direct action performed successfully." 
        # }
        print(f"report details - {requestObj}")
        FrontMqttConnection.test_sample('soulsystem/takeQCReportpath', requestObj)
    
    def create_tar_and_upload_report(self, report_files):
        tar_name = "reports.tar.gz"
        with tarfile.open(tar_name, "w") as tar:
            for report_file in report_files:
                if os.path.exists(report_file):
                    tar.add(report_file)
                    print(f"Added {report_file} to {tar_name}.")
                    
        file_size = os.path.getsize(tar_name)
        hubConfig_serial = Path("/home/linaro/db/serial").read_text().strip()
        server_url_string = Path("/home/linaro/db/server").read_text().strip()
        SERVER_MAP = {
            "https://dev.clouzer.com/upload": 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJub2RlLnVzZXJAY2xvdXplci5jb20iLCJ1c2VybmFtZSI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsInVzZXJFbWFpbCI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsInVzZXJVSUQiOiJub2RlLnVzZXJAY2xvdXplci5jb20iLCJ1c2VyTmFtZSI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsImZpcnN0TmFtZSI6Im5vZGUiLCJsYXN0TmFtZSI6InVzZXIiLCJzdGF0dXMiOiIxIiwicHJvZmlsZV9kYXRhIjoic3NzcyIsIkNNTF9MT0NBVElPTiI6IktvdGhydWQiLCJDTUxfQUREUkVTU19MSU5FMiI6IlB1bmUiLCJDTUxfQ09OVEFDVF9OTyI6InNkYWtzZGNrYSIsIlJFQ09WRVJZX01BSUwiOiJub2RldXNlcjk3QGdtYWlsLmNvbSIsImlhdCI6MTcxOTk3OTE3MH0.UT0jvFvSWJZQXouYwk0NHFjoFzjrY9G6tFC-7Xp8it3td2C2JrY9wEvKAg2bQ8dkhVNPPWHj5FrXHO4deAw_TiBEOF4T47u7hQSS_O3eOyPFYjggNf1ZAP2LSOhGq9lhVaJ7kWre21lf-aq3t3tuZtpfG_F9yVo58qNyEsqvwQy1B5RUmdFrPYZTmVoIIL8BTIdQEBfwDcn--TSW8tvJE6YKMKR8uptdGx6WWg9rCwPKJ6ylaxEursxTyUdapOkiuQpnTcGqP4f4v21G49yYSqFzhwyROmbPdtZrD_tQGZfGeK-m0tT1YO_qpZ5pO7iUWseJs54mscGuFrI0CCOGBA',
            "https://test.clouzer.com/upload": 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJub2RlLnVzZXJAY2xvdXplci5jb20iLCJ1c2VybmFtZSI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsInVzZXJFbWFpbCI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsInVzZXJVSUQiOiJub2RlLnVzZXJAY2xvdXplci5jb20iLCJ1c2VyTmFtZSI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsImZpcnN0TmFtZSI6Im5vZGUiLCJsYXN0TmFtZSI6InVzZXIiLCJzdGF0dXMiOiIxIiwicHJvZmlsZV9kYXRhIjoic3NzcyIsIkNNTF9MT0NBVElPTiI6IktvdGhydWQiLCJDTUxfQUREUkVTU19MSU5FMiI6IlB1bmUiLCJDTUxfQ09OVEFDVF9OTyI6InNkYWtzZGNrYSIsIlJFQ09WRVJZX01BSUwiOiJub2RldXNlcjk3QGdtYWlsLmNvbSIsImlhdCI6MTcxOTk3OTI4Mn0.AIdicmmsNVqk-_5FL7KE4ycZJYJTtUdBCFKG9982SU0S5I4yreYeHb1WLI4equ1CbNb8fHXs1d3_n9VNUqIK4n4AB18ZtJGg5qz5k9D1IlXzhCxEG8kphGiXn2yE4x_ccbdK3pzXsLwvc7GrUZn08acq9zY7KBqWzEB8b-0CUWK9eyW6H29zstVFzhMmq5om80CBZok92fvuCywzTL80RA66KMD3Xpo2ExUhE1ming5Z0VvF_YBRokjE3GZzhQm2CKnON0lJ5odxzuiNG3SNzKMJ2iX_pzZTp_CmND3jhTl7LBVC_2PB0iPcPKO_WxtW5Wv7B3xIcuEMu5IBZf_W0A',
            "https://clouzerweb.clouzer.com/upload": 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiJub2RlLnVzZXJAY2xvdXplci5jb20iLCJ1c2VybmFtZSI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsInVzZXJFbWFpbCI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsInVzZXJVSUQiOiJub2RlLnVzZXJAY2xvdXplci5jb20iLCJ1c2VyTmFtZSI6Im5vZGUudXNlckBjbG91emVyLmNvbSIsImZpcnN0TmFtZSI6Im5vZGUiLCJsYXN0TmFtZSI6InVzZXIiLCJzdGF0dXMiOiIxIiwicHJvZmlsZV9kYXRhIjoic3NzcyIsIkNNTF9MT0NBVElPTiI6IktvdGhydWQiLCJDTUxfQUREUkVTU19MSU5FMiI6IlB1bmUiLCJDTUxfQ09OVEFDVF9OTyI6InNkYWtzZGNrYSIsIlJFQ09WRVJZX01BSUwiOiJub2RldXNlcjk3QGdtYWlsLmNvbSIsImlhdCI6MTcxOTk3OTMzMH0.XjErAZvLGZi50PwKSNrXUtwjpycNZNcLHu-lOgB53V9ZPhEAHjkRveocJnWeFW0VS0TTLuwatm30UMM5BUMOy6r8hbbPv7hB6jnFEsVWu86Q_EwigSnF86KlA81ksEvhN6NhyfmIHHp9lGdbIaSZxH5aoZWlrPyIhQSLkZb8lPlAgAIwRtqtYua4UNo4mNiXkmC1aU1TjL6x02w_FvsMO2wRICQKUmfIPcDuvdAXaAfJ5t4bEBQ90dDMspwwvhJup-ftY8hms17rkdaI2SKAM5lMbJtrlAQXtKT_3ci687TG81VJdv88QvPgp2QpqtnEypuN5ZYvL0ScBOt-r6u9Fw'
        }
        if server_url_string == "https://modus.clouzer.com":
            url = "https://clouzerweb.clouzer.com/upload"
        else:
            url = f"{server_url_string}/uploserver Response for upload report error: Unexpected token o in JSON at position 1ad"
        jwt_token = SERVER_MAP[url]
        extra_params = {"scriptName": "TEST_REPORTS"}
        # Prepare payload
        form_data = {
            "windowId": int(time.time() * 1000),
            "name": "reports.tar.gz",
            "id": "edge.maintenance@clouzer.com",
            "size": file_size,
            "type": "mochaScriptReport",
            "hubId": hubConfig_serial,
            "extraParams": json.dumps({
                "hubId": hubConfig_serial,
            }),
            "keyVal": "asdfasfsa"
        }
        headers = {
            "Authorization": jwt_token,
            "beUserId": "dummyawstest1.userNew.com",
        }
        # Send the POST request
        print(url," server request for upload report",form_data," headers : ",headers)
        try:
            response = requests.post(url,data=form_data, files={'stream':open(tar_name,'rb')},  headers=headers)
            # print("server Response for upload report",response)
            response_json = response.json()
            print("server json Response for upload report",response_json)
            if response_json["uploadStatus"]:
                self.send_report_path(response_json)
        except Exception as e:
            print("exception :",e)
            print("Response content:", response.content)
            print("Response text:",response.text)

    def ensure_pytest_installed(self):
        """Ensure pytest is installed using pip if not present."""
        try:
            import pytest
        except ImportError:
            subprocess.check_call(["sudo", "pip", "install", "pytest", "pytest-html"])
    
    def run_tests(self):
        self.ensure_pytest_installed()
        import pytest
        runningContainer = checkDocker.checkRunningContainer()
        if runningContainer:
            FrontMqttConnection.client_connection()
            time.sleep(0.1)
            CloudMqttConnection.cloud_connection()
            time.sleep(0.1)
            
            container = {
                "MaintenanceFramework": ["test_token.py","test_validate.py"],
            }
            report_files = []
            for test_folder, test_files in container.items():
                report_path = f"{test_folder}_report.html"  # e.g., hubInstallationFramework_report.html
                report_files.append(report_path)
                test_paths = [os.path.join(test_folder, test_file) for test_file in test_files]
                print(f"Running tests for {test_folder}...")
                result = pytest.main(["-v", "-s", "--html", report_path, "--self-contained-html"] + test_paths)
                if result != 0:
                    print(f"Some tests failed in {test_folder}. Test result code: {result}")
                    break
                else:
                    print(f"All tests passed in {test_folder}.")
            self.create_tar_and_upload_report(report_files)
            FrontMqttConnection.client_disconnect()
            CloudMqttConnection.client_disconnect()
        else:
            print("Expected container not running-->",runningContainer)
            
if __name__ == "__main__":
    test_runner = TestRunner()
    test_runner.run_tests()
