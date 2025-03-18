import requests
from datetime import datetime
import json
from connections.Constant import constant

class Email:

    def mail_generator(description,status_flag):
        try:
            token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lc3BhY2VJZCI6IkRFVl8xMjMiLCJDTUxfTUFDX0lEIjoiREM6QTY6MzI6OTI6QzM6RjUiLCJDTUxfU1RBVFVTIjoiMSIsIkNNTF9TRVJJQUxfTk8iOiJQUkFWSU4tMTIzNCIsImlhdCI6MTcxOTQ5MjcxN30.HqDY5cSET9xq9LLBKH9yCMTdmDnFB8UchU8wDid40CPaUAevSkwfvAx1cbd263gyBwUU81n-E6-TeyPoOO56ui0MOWcdP-be-Bkg2fwQfKoHV-xzc9k_yj3YBN_fipLm3l09JUBADOUteq6A5_7C6UGVZ1wgteG0YDKIRuBTWQK7Dn0ekmxs_s3V3RDOJ4K88xYK9cnCQTeL9vTnMPAHzrBroUTj8C4OFSonzTaE5vfa6ea_4dLqem0mmh8JusEonDNP-4oYcbqbs69gz_7KOOiKiGIpEwz17EZ5ZaPJvv2u9hz_TC8Vzgew7IxB7hkNT_9Sbm_b1-LXg1BCXTAvTg"
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if status_flag == 0:
                payload = {
                    "body": f"{constant.hub_serial} - script execution - QC Execution sucess at {current_time}",
                    "subject": f"{constant.hub_serial}✅| QC status - QC Execution sucess"
                }
            else:
                payload = {
                    "body": f"{constant.hub_serial} - QC Execution fail - {description} - script execution failed at {current_time}",
                    "subject": f"{constant.hub_serial}❌| QC status - QC Execution fail"
                }

            api_url = "https://modus.clouzer.com/mailer"
            headers = {
                "Content-Type": "application/json",
                "Authorization": token
            }
            print("send mail -->",payload)
            try:
                response = requests.post(api_url, headers=headers, json=payload)
                print(f"send mail response - {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Failed to send email: {e}")
        except Exception as e:
                print(f"exception in mail_generator : {e}")