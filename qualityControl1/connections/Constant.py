from connections.Network import IpAddresss

class constant:
    
    clientId = "pyest_client1"
    clientObjectCache = {}
    mac_ID=IpAddresss.get_mac_address()
    CODED_HUBID = IpAddresss.read_file(f"/home/linaro/db/CODED_HUBID").strip()
    hub_serial = IpAddresss.read_file(f"/home/linaro/db/serial").strip()