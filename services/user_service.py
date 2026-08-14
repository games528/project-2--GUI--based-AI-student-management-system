from services.password_service import hash_password

def prepare_user_password(password):
    password_hash = hash_password(password)
    return password_hash



