import socket #lib socket que vou usar para conexão
import re
import math #lib para o calculo do triângulo
HOST = "192.168.78.9" #vou ter que usar no processo de conexao
PORT = 1338  
#função de calcular triangulo que peguei do github
def solve_triangle(first_deg, second_deg, third_side):
    C = 180 - first_deg - second_deg
    a = third_side * math.sin(math.radians(first_deg)) / math.sin(math.radians(C))
    return round(a, 2)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #aqui eu crio o objeto socket necessário para a comuncicação
client.connect((HOST, PORT)) #aqui utilizando o objeto socket criado, inicio uma conexão com o ip:porta
while True:
    chunk = client.recv(4096).decode() #usando o recv eu recebo a resposta do servidor (4096 indica a qtd de bytes que vai le)
    data += chunk
    print(chunk, end="")  
    #capturo a parte do data que contém as infos do triangulo (lados e angulos)
    match = re.search(
        r"Angulo A\s*=\s*(\d+).*?Angulo B\s*=\s*(\d+).*?Lado c\s*=\s*(\d+)",
        data, re.DOTALL | re.IGNORECASE
    )
    if match:
        A = int(match.group(1)) #vou pegar o angulo A, Angulo b, e lado do C do match, que estão separados em 3 "grupos"
        B = int(match.group(2))
        c = float(match.group(3))   
        answer = solve_triangle(A, B, c) #chamo a função que calcula a lei dos senos
        print(f"enviando a resp: {answer}")
        client.sendall(f"{answer}\n".encode()) #aqui usando o sendall, posso enviar um dado usando o objeto socket
        print(client.recv(4096).decode()) #aqui recebo com o recv novamente a resposta
        break