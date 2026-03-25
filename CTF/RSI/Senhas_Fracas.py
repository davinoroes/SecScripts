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