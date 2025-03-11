#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:31:02 2024

@author: developers
"""

import netifaces
import time
import random
import os

class IpAddresss:
    
    def read_file(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                return file.read()          
        else:
            print("file path not found")
        
    def get_network_creadentials():
        file_path = "/etc/network/interfaces"
        ssid = ""
        psk = ""
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if line.startswith("wpa-ssid"):
                        ssid = line.split(" ")[1].strip('"')
                    elif line.startswith("wpa-psk"):
                        psk = line.split(" ")[1].strip('"')
            return {
                'ssid': ssid,
                'psk': psk
            }
        else:
            print("file path not found")
    
    def get_necessary_ids(user_id):
        ts = int(time.time() * 1000)  # current timestamp in milliseconds
        request_id = f'/sync#{user_id}#{ts}r{random.randint(0, 999)}r{random.randint(0, 999)}'
        communication_id = f'{ts}setClientToken{random.randint(0, 999)}'
        
        return {
            'requestId': request_id,
            'communicationId': communication_id
        }

    def get_ip_address():
        try:
            interface_name = "wlan0"   #wlan0   wlp1s0
            ip_interface = netifaces.ifaddresses(interface_name)
            if netifaces.AF_INET in ip_interface.keys():
                ip_address = ip_interface[netifaces.AF_INET][0]['addr']
            # Check for IPv6 address
            elif netifaces.AF_INET6 in ip_interface:
                ip_address = ip_interface[netifaces.AF_INET6][0]['addr']
            else:
                ip_address = "0.0.0.0"
            return ip_address
        except Exception as e:
            return None
        
    def get_mac_address():
        try:
            interface = "wlan0"
            with open(f"/sys/class/net/{interface}/address") as f:
                mac_address = f.read().strip()
                return mac_address.upper()
        except FileNotFoundError:
            return None