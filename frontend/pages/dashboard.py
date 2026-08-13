import customtkinter as ctk
from services.auth_service import logout

app = ctk.CTk()

app.title("Dashboard")
app.geometry("1000x650")


main_frame = ctk.CTkFrame(
    app,
    width=500,
    height=400
)

main_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center"
)


heading = ctk.CTkLabel(
    main_frame,
    text="Dashboard",
    font=ctk.CTkFont(
        size=28,
        weight="bold"
    )
)

heading.pack(pady=(40, 30))


logout_button = ctk.CTkButton(
    main_frame,
    text="Logout",
    width=200,
    height=40,
    command = logout
)

logout_button.pack(pady=20)


app.mainloop()