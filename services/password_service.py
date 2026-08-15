import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def verify_password(password, password_hash):
    return bcrypt.checkpw(password.encode("utf-8"),password_hash)


