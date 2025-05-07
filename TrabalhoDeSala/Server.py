import socket
import threading
from cryptography.fernet import Fernet

chave_secreta = b'Qv5jwkrmmuZ1lgGNOYyk7UCy4dlNHkSXiRjLBNn-HHY='
fernet = Fernet(chave_secreta)

clientes_conectados = []

def broadcast(mensagem_criptografada, remetente):
    for cliente in clientes_conectados:
        if cliente != remetente:
            try:
                cliente.sendall(mensagem_criptografada)
            except:
                cliente.close()
                clientes_conectados.remove(cliente)

def lidar_com_cliente(conexao, endereco):
    print(f"Novo cliente conectado: {endereco}")
    clientes_conectados.append(conexao)

    try:
        while True:
            dados = conexao.recv(4096)
            if not dados:
                break

            try:
                mensagem = fernet.decrypt(dados).decode()
                print(f"Mensagem de {endereco}: {mensagem}")
                resposta_criptografada = fernet.encrypt(mensagem.encode())
                broadcast(resposta_criptografada, conexao)
            except Exception as e:
                print("Erro ao descriptografar:", e)
    finally:
        conexao.close()
        if conexao in clientes_conectados:
            clientes_conectados.remove(conexao)
        print(f"Cliente {endereco} desconectado.")

def main():
    host = 'localhost'
    porta = 12345

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((host, porta))
    servidor.listen()
    print(f"Servidor escutando em {host}:{porta}")

    while True:
        conexao, endereco = servidor.accept()
        thread = threading.Thread(target=lidar_com_cliente, args=(conexao, endereco))
        thread.start()

if __name__ == "__main__":
    main()
