import netifaces

def get_default_gateway():
    gateways = netifaces.gateways()
    default_gateway = gateways.get('default', {})
    ipv4_gateway = default_gateway.get(netifaces.AF_INET)

    if ipv4_gateway:
        gateway_ip, interface = ipv4_gateway
        print(f"Gateway padrão: {gateway_ip}")
        print(f"Interface de saída: {interface}")
    else:
        print("Nenhum gateway IPv4 padrão encontrado.")

get_default_gateway()
