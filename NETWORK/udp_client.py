import socket 

target_host = "8.8.8.8" #vou testar com o DNS server
target_port = 53
#aqui criamos o objeto socket, mas utilizando o SOCK_DGRAM (utilizado no udp)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#no udp não preciso chamar o conect, pois o UDP é um protocolo sem conexão (diferente do tcp)
client.sendto(b"AAAAAAABBBBB",(target_host,target_port))
#aqui recebo a response da conexão 
data,addr = client.recvfrom(4096)
print(data.hex())
