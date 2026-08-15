from services.password_service import hash_password, verify_password

def change_password(current_password, new_password, stored_hash):
    if not verify_password(current_password, stored_hash):
        return False, "Current password is incorrect."
    if current_password == new_password:
        return False, "New password must be different."
    if len(new_password) < 8:
        return False, "New password must be at least 8 characters."
    new_hash = hash_password(new_password)
    return True, new_hash

