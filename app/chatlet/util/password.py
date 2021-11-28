import bcrypt
from decouple import config

# salt = config('SALT').encode()

# cant import config from decouple so i did this way due to no time(i know this is bad practice)) )
salt = "$2b$12$ePxOWWs4EHKpEm0/Uudthu".encode()


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), salt).decode()
