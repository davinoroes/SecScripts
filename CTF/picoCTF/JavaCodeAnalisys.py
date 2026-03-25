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


