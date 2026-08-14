import bcrypt

def hash_password(password):
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
    return hashed_password

def verify_password(password, password_hash):
    return bcrypt.checkpw(password.encode("utf-8"),password_hash)


