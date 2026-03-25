from pwn import *
import string

binary = './REV01.bin'
charset = string.printable
password = ""

def size_discover(archive):
    for i in range(1,100):
        p = process(binary)
        p.recvuntil("senha:")
        guess = 'A' * i
        p.sendline(guess)

        output = p.recvall().decode()
        if "tamanho errado" not in output.lower():
            return i
        p.close()

size = size_discover(binary)
for i in range(size):
    for c in charset:
        guess = password + c + "A"*(size-len(password)-1)
        p = process(binary)
        p.recvuntil("senha:")
        p.sendline(guess)
        out = p.recvall().decode()
        if f"indice: {i}" not in out:
            password += c
            print("Encontrado:", password)
            break

        p.close()

print("Senha :", password)





    

