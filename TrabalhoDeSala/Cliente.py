import socket
import threading
from cryptography.fernet import Fernet

chave_secreta = b'Qv5jwkrmmuZ1lgGNOYyk7UCy4dlNHkSXiRjLBNn-HHY='
fernet = Fernet(chave_secreta)

def receber_mensagens(cliente):
    while True:
        try:
            dados = cliente.recv(4096)
            if not dados:
                print("Conexão encerrada pelo servidor.")
                break
            mensagem = fernet.decrypt(dados).decode()
            print(f"\n[Outro cliente]: {mensagem}")
        except Exception as e:
            print("Erro ao receber/descriptografar:", e)
            break

def main():
    host = 'localhost'
    porta = 12345

    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[DEBUG] Tentando conectar ao servidor...")
        cliente.connect((host, porta))
        print("[DEBUG] Conectado com sucesso ao servidor!")

        threading.Thread(target=receber_mensagens, args=(cliente,), daemon=True).start()

        while True:
            mensagem = input("Você: ")
            criptografada = fernet.encrypt(mensagem.encode())
            cliente.sendall(criptografada)
    except Exception as e:
        print("Erro ao conectar ou durante a comunicação:", e)

if __name__ == "__main__":
    main()
