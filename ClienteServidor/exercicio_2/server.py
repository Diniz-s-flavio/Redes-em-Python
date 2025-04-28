from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print(message, clientAddress)

    decodedMessage = message.decode()
    modifiedMessage = decodedMessage.upper()

    vogais = 'AEIOUaeiou'
    numVogais = sum(1 for letra in decodedMessage if letra in vogais)

    numPalavras = len(decodedMessage.split())

    response = f"{modifiedMessage}\nVogais: {numVogais}\nPalavras: {numPalavras}"

    print(response)
    serverSocket.sendto(response.encode(), clientAddress)
