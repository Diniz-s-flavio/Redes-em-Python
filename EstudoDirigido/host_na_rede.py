import ipaddress
import subprocess
import concurrent.futures

rede = ipaddress.ip_network('192.168.0.0/24', strict=False)

def ping_no_ip(ip):
    try:
        result = subprocess.run(
            ['ping', '-n', '1', '-W', '1', str(ip)],
            stdout=subprocess.DEVNULL
        )
        if result.returncode == 0:
            return str(ip)
    except Exception:
        pass
    return None

print("Varredura de IPs ativos na rede...")

ips_ativos = []

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    resultados = executor.map(ping_no_ip, rede.hosts())
    for ip in resultados:
        if ip:
            ips_ativos.append(ip)

print("\nIPs ativos encontrados:")
for ip in ips_ativos:
    print(ip)