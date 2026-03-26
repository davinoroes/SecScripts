import subprocess

password_list = []

for i in range(0,16**4):
    password_list.append(f"{i:04x}")

p = 1
for password in password_list:
    print(f'Testando senha: {password} - tentativa: {p}')
    p += 1

    output = subprocess.run(
        ["python", "flag5.py"],
        input=password,
        text=True,
        capture_output=True)
    
    if "Welcome" in output:
        print(f"\nSenha encontrada: {password}")
        print(output.stdout)
        break


"""
    In this lab, they give me a list of possibilities (all hex number with 4 digits),
    and the .py execution file that asks for the password. So what i did was to brute force the list of possibilites 
    until find the correct hex password, using subprocess lib to run the file. 
"""

"""
    Neste laboratório, eles me dão uma lista de possibilidades (todos números hexadecimais com 4 dígitos),
    e o arquivo de execução .py que solicita a senha. Então o que fiz foi forçar a lista de possibilidades
    até encontrar a senha hexadecimal correta, usando o subprocesso lib para executar o arquivo.
"""




    
