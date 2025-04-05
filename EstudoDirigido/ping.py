import platform
import subprocess
from urllib.parse import urlparse
import socket

url = "www.ifgoiano.edu.br"
ip = socket.gethostbyname(url)

# print(f"O IP de {url} é {ip}")

def ping_host(ip):
    sistema = platform.system().lower()
    
    comando = ["ping", "-n", "1", ip]

    resultado = subprocess.run(comando, stdout=subprocess.DEVNULL)
    return resultado.returncode == 0


# ip = "192.168.0.106"
# if ping_host(ip):
#     print(f"192.168.0.101 respondeu ao ping.")
# else:
#     print(f"192.168.0.101 não respondeu ao ping.")
ip = "192.0.0.4"
if ping_host(ip):
    print(f"{ip} respondeu ao ping.")
else:
    print(f"{ip} não respondeu ao ping.")
# if ping_host(ip):
#     print(f"{ip} respondeu ao ping.")
# else:
#     print(f"{ip} não respondeu ao ping.")