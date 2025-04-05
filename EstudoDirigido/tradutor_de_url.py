import socket

url = "www.ifgoiano.edu.br"
ip = socket.gethostbyname(url)

print(f"O IP de {url} é {ip}")