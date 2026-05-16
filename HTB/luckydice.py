import socket
import re

HOST = "154.57.164.70"
PORT = 30115
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

buffer = ""
while " >" not in buffer:
    data = client.recv(4096).decode()
    if not data:
        exit()
    buffer += data
    print(data, end="")

client.sendall(b"1\n")
buffer = ""
while True:
    data = client.recv(4096).decode()
    if not data:
        exit()
    buffer += data
    print(data,end="")
    if "Who wins this round?" in buffer:
        match = re.findall(r"Player (\d+): ([\d ]+)", buffer)
        scores = []
        for player,score in match:
            scr = list(map(int, score.split()))
            scores.append(sum(scr))
        max_score = max(scores)
        winner = max(i for i, score in enumerate(scores) if score == max_score)
        answer = str(winner+1)
        client.sendall(f"{answer}\n".encode())
        buffer = ""

        
