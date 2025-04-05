import subprocess
import re

def get_mac_from_ip(ip_address):
    try:
        output = subprocess.check_output(f"arp -a {ip_address}", shell=True, text=True)
        mac_match = re.search(r'((?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]{2})', output)
        if mac_match:
            return mac_match.group(0)
        else:
            return "MAC não encontrado (talvez o IP não esteja na tabela ARP)"
    except Exception as e:
        return f"Erro: {e}"

ip1 = "192.168.0.101"
ip2 = "192.168.0.102"

print(f"{ip1} -> MAC: {get_mac_from_ip(ip1)}")
print(f"{ip2} -> MAC: {get_mac_from_ip(ip2)}")