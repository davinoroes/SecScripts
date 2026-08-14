#this is a script that interacts with PORT 9100. I used to see if was vulnerabel to CVE-2017-2741

import socket

my_socket = socket.create_connection(("127.0.0.1",9100))
s.settimeout(2)

s.sendall(b"\x1b%-12345X@PJL INFO ID\r\n")
s.shutdown(socket.SHUT_WR)

try:
    print(repr(s.recv(8192)))
expect socket.timeout:
    print("SEM RESPOSTA")

s.close()