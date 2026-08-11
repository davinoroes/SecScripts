import socket
import sys

if len(sys.argv) <= 1:
    print("Modo de uso -> python portscan.py ip")

else:
    for porta in range(1,65535):
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if my_socket.connect_ex((sys.argv[1],porta)) == 0:
            print(f"Porta {porta} aberta")
            my_socket.close()

