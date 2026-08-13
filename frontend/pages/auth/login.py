import customtkinter as ctk
from numpy import pad
def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.configure(show = "")
    else:
        password_entry.configure(show = "*")
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

app.mainloop()