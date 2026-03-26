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

"""In this lab, I had a .bin file that asked for a password to deliberate on the flag.
   But the file gives some hints. First it says about the password length and after the
   user gets it right, the file gives the first password index (char) which is incorrect.
   For that, first i create a size_discover fuction, which process the archive and sends an ever-increasing password,
   to discover len(real_password). After that, using the size_discover return, we permutate for each char,
   until find the correct password.
   """


"""Neste laboratório, eu tinha um arquivo .bin que pedia uma senha para mostrar o sinalizador.
 Mas o arquivo dá algumas dicas. Primeiro diz sobre o comprimento da senha e depois o o usuário acerta,
 o arquivo fornece o primeiro índice de senha (char), que está incorreto.
 Para isso, primeiro criei uma função size_discover, que processa o arquivo e envia uma senha cada vez maior, para descobrir len(real_password).
 Depois disso, usando o retorno size_discover, permutamos para cada char , até encontrar a senha correta.
"""





    

