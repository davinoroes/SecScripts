import socket
import threading

#aqui eu vinculo o ip e a porta ao servidor tcp
bind_ip = "0.0.0.0"
bind_port = 9999
#criação do objeto socket do servidor (na comunicação tcp client-server, existe a criação de um par socket, cada um de um lado)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#com o bind eu associo ao objeto socket o ip e a porta que vai ser utilizado
server.bind((bind_ip,bind_port))
#aqui eu habilito o servidor a receber conexões, até 5 conexões simultâneas
server.listen(5)
print(f"Listening: {bind_ip}-{bind_port}")

#função de lidar com o objeto cliente, recebendo sua request e enviando uma response ("ACK!")
def handle_client(socket_client):
    request = socket_client.recv(4096)
    print(f"Requisição: {request}")
    socket_client.send(b"ACK!")
    socket_client.close()

while True:
    #aqui faço o objeto socket aceitar conexões, e tenho a criação de um novo socket, que vou usar no multithreading
    client, addr = server.accept()
    print(f"Conexão aceita {addr[0]}-{addr[1]}")
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()



