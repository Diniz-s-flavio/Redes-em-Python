import psutil

addrs = psutil.net_if_addrs()
for interface, addr_list in addrs.items():
    for addr in addr_list:
        if addr.family == 2:
            print(f"Interface: {interface}")
            print(f"  IP: {addr.address}")
            print(f"  Máscara: {addr.netmask}")