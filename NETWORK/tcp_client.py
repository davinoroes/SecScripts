import socket

host_name = "www.google.com"
target_port = 80 #porta padrao do http -> vou utilizar essas variaveis no processo de conexão

#aqui faço a criação do objeto socket. o AF_INET indica que na conexão vou usar ipv4 ou hostname
# SOCK_STREAM indica que vai ser um cliente tcp
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#aqui utilizo do objeto para fazer a conexão, passando como parametro o nome do host e a porta de comunicação
client.connect((host_name,target_port))
#usando o send eu posso enviar algum data através da conexão (presumindo que a conexão teve sucesso)
client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
#aqui obtemos a response do processo, 4096 indica o tamanho maximo de addos a ser lidos por vez
response = client.recv(4096)
print(response.decode("utf-8"))

