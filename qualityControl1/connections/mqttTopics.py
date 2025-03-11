from connections.Network import IpAddresss
from connections.Constant import constant

server = IpAddresss.read_file(f"/home/linaro/db/server").strip()
serial = IpAddresss.read_file(f"/home/linaro/db/serial").strip()
modelNumber = IpAddresss.read_file(f"/home/linaro/db/modelNumber").strip()
hubKeyVal = IpAddresss.read_file(f"/home/linaro/db/hubKeyVal").strip()



if server == 'https://dev.clouzer.com':
    cloud_broker_port = '31160'
    cloud_broker_host = 'dev.clouzer.com'
    NameSpaceId = 'DEV_123'
elif server == 'https://test.clouzer.com':
    cloud_broker_host = 'test.clouzer.com'
    cloud_broker_port = '31160'
    NameSpaceId = 'TEST_123'
elif server == 'https://modus.clouzer.com':
    cloud_broker_host = 'modus.clouzer.com'
    cloud_broker_port = '31160'
    NameSpaceId = 'AWS_123'
elif server == 'https://predev.clouzer.com':
    cloud_broker_host = 'predev.clouzer.com'
    cloud_broker_port = '31170'
    NameSpaceId = 'PREDEV_123'
    
QOS = 0
RequestTopic = [
    ("hubActionResponse/installer", QOS),
    ("hubActionResponse/controller", QOS),
    ("process/status/get_res", QOS),
    (constant.clientId, QOS),
    ("soulDb/dbResponse/systemdbresponse",QOS),
    ("soulDb/dbResponse",QOS),
    ("process/status/get_res",QOS),  
]

cloudTopic = [
    (f"{NameSpaceId}/HUB/INC_PRP_SYCN_SYS/{modelNumber}/{serial}", QOS),
    (f"{NameSpaceId}/HUB/HUB_TO_MTN/{modelNumber}/{serial}",QOS), 
]