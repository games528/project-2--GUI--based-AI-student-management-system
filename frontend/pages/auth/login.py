import customtkinter as ctk
from numpy import pad
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show = "")
    else:
        password_entry.configure(show = "*")

def authenticate_user(username,password):
    if username == "admin" and password == "1234":
        return True
    return False        

def validate_login():
    username = username_entry.get().strip()
    password = password_entry.get()
    if not username:
        error_label.configure(text = "please enter your email/username")
        return
    if not password:
        error_label.configure(text = "please enter your password")
        return
    if authenticate_user(username,password):
        error_label.configure(text = "Login successful")
    else:
        error_label.configure(text = "invalid username or password")



app = ctk.CTk()

app.title("AI student management system")

app.geometry("1000 * 650")

main_frame = ctk.CTkFrame(app, width = 500, height =  500)
main_frame.place(relx = 0.5, rely = 0.5, anchor = "center")

heading = ctk.CTkLabel(main_frame, text ="Welcome back,\n please sign in to continue", font = ctk.CTkFont(size = 28, weight = "bold"))

heading.pack(pady =(25,20))

username_entry = ctk.CTkEntry(main_frame, width= 340, height = 40, placeholder_text = "Email or Username")
username_entry.pack(pady = 10)

password_frame = ctk.CTkFrame(main_frame, fg_color = "transparent")
password_frame.pack(pady = 10)
password_entry = ctk.CTkEntry(password_frame, width= 300, height= 40, placeholder_text= "password", show="*")
password_entry.pack(side = "left")
show_password_button = ctk.CTkButton(password_frame, text = "(.)", width= 40, height = 40, command = toggle_password)
show_password_button.pack(side = "left", padx = (5,0))

remember_me = ctk.CTkCheckBox(main_frame, text = "Remember me")
remember_me.pack(anchor = "w", padx =75, pady = (5, 15))

error_label = ctk.CTkLabel(main_frame,text = "",text_color = "red", font = ctk.CTkFont(size = 14))
error_label.pack(pady = (0,5))

login_button = ctk.CTkButton(main_frame, text = "Login", width = 300, height = 40, command = validate_login)
login_button.pack(pady = (10, 20))

app.mainloop()