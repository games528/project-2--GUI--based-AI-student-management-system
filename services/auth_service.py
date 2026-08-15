current_user = None

def set_current_user(username):
    global current_user
    current_user = username

def get_current_user():
    return current_user

def logout_user():
    global current_user
    current_user = None

if __name__ == "__main__":
    set_current_user("admin")
    print("logged in user: ", get_current_user())
    logout_user()
    print("after logout: ", get_current_user())