import hashlib
import subprocess

arquivo = 'arquivo.zip'

for i in range(256):
    for j in range(256):
        data = bytes([i,j])
        cript = hashlib.md5(data).hexdigest()
        print(f"Testando a sneha: {cript}")
        resultado = subprocess.run(["unzip", "-P", cript, "-t",arquivo],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        if b"OK" in resultado.stdout:
            print(f"Senha encontrada:{cript}")
            subprocess.run(["unzip", "-P", cript, arquivo])
            exit()



"""
    In this lab, we had an archive with password. The tip is that the password is composed of the two byte md5.
    So what i did was to permutate and test every possibility of two bytes, and aplicate md5 (65.536)
    using subprocess lib to run .zip and hashlib to aplicate md5.

"""

"""
    Neste laboratório, tínhamos um arquivo com senha. A dica é que a senha é composta pelos dois bytes md5.
    Então o que eu fiz foi permutar e testar todas as possibilidades de dois bytes e aplicar md5 (65.536)
    usando subprocess lib para executar .zip e hashlib para aplicar md5.
    
"""
