import socket
import threading
import ssl
from cryptography.fernet import Fernet

# Será inicializado após receber a chave do servidor
fernet = None


def criptografar(texto):
    # return fernet.encrypt(texto.encode())
    return texto.encode()


def descriptografar(texto_criptografado):
    # return fernet.decrypt(texto_criptografado).decode()
    return texto_criptografado.decode()


def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Conexão encerrada pelo servidor.")
                break
            print(descriptografar(data))
        except Exception as e:
            print(f"Erro ao receber mensagem: {e}")
            break


def start():
    global fernet
    host = "10.44.132.10"
    port = 5555

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, port))

    # === Recebe a chave Fernet antes de qualquer mensagem ===
    chave_recebida = clientSocket.recv(1024).strip()
    fernet = Fernet(chave_recebida)

    # === Inicia a thread de recebimento ===
    threading.Thread(target=receive_messages, args=(clientSocket,), daemon=True).start()

    # === Loop de envio de mensagens ===
    while True:
        try:
            msg = input()
            clientSocket.send(criptografar(msg))
        except:
            break



if __name__ == "__main__":
    start()