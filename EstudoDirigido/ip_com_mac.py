import psutil
import socket

interfaces = psutil.net_if_addrs()

for interface, addresses in interfaces.items():
    mac = None
    ip = None
    for addr in addresses:
        if addr.family == psutil.AF_LINK:
            mac = addr.address
        elif addr.family == socket.AF_INET:
            ip = addr.address
    if mac or ip:
        print(f"Interface: {interface}")
        if ip:
            print(f"  IP: {ip}")
        if mac:
            print(f"  MAC: {mac}")