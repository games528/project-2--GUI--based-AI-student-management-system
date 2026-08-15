import json
from pathlib import Path

remeber_file = Path("remember_login.json")

def save_remember_login(username):
    data = {"remembered": True, "username": username}
    with open(remeber_file, "w") as file:
        json.dump(data,file)

def clear_remember_login():
    data = {"remembered": False, "username":""}
    with open(remeber_file, "w") as file:
        json.dump(data,file)

def load_remember_login():
    if not remeber_file.exists():
        return None
    with open(remeber_file, "r") as file:
        data = json.load(file)
    if data.get("remembered") is True:
        return data.get("username")
    return None 

save_remember_login("username")
clear_remember_login()
load_remember_login()
