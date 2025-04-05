import psutil

def getmac_in_pyton():
    mac_addresses = {}
    interfaces = psutil.net_if_addrs()
    
    for interface, addresses in interfaces.items():
        for addr in addresses:
            if addr.family == psutil.AF_LINK:  
                mac_addresses[interface] = addr.address
    
    return mac_addresses

macs = getmac_in_pyton()
for interface, mac in macs.items():
    print(f"Interface: {interface}, MAC: {mac}")