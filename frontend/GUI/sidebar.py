import tkinter as tk
def create_sidebar(root):
    sidebar = tk.Frame(
        root,
        width=220,
        bg="#2c3e50"
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    sidebar.pack_propagate(False)

    title = tk.Label(
        sidebar,
        text="Student Management",
        font=("Arial", 16, "bold"),
        bg="#2c3e50",
        fg="white"
    )

    title.pack(pady=30)
    dashboard_button = tk.Button(sidebar, text="Dashboard",command=lambda: print("Dashboard button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")  
    dashboard_button.pack(fill="x", padx=15, pady=5)
    student_button = tk.Button(sidebar, text="Students",command=lambda: print("Students button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")
    student_button.pack(fill="x", padx=15, pady=5)
    academic_button = tk.Button(sidebar, text="Academic Records",command=lambda: print("Academic Records button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")
    academic_button.pack(fill="x", padx=15, pady=5)
    attendance_button = tk.Button(sidebar, text="Attendance",command=lambda: print("Attendance button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")
    attendance_button.pack(fill="x", padx=15, pady=5)
    analytics_button = tk.Button(sidebar, text="Analytics",command=lambda: print("Analytics button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")
    analytics_button.pack(fill="x", padx=15, pady=5)
    report_button = tk.Button(sidebar, text="Reports",command=lambda: print("Reports button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")
    report_button.pack(fill="x", padx=15, pady=5)
    settings_button = tk.Button(sidebar, text="Settings",command=lambda: print("Settings button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")
    settings_button.pack(fill="x", padx=15, pady=5)
    logout_button = tk.Button(sidebar, text="Logout",command=lambda: print("Logout button clicked"), font=("Arial", 12), bg="#34495e", fg="white", relief="flat", anchor="w")
    logout_button.pack(fill="x", padx=15, pady=5)

    return sidebar

if __name__ == "__main__":
    print("SIDEBAR TEST STARTED")

    root = tk.Tk()
    root.title("Sidebar Test")
    root.geometry("1000x600")

    create_sidebar(root)

    print("SIDEBAR CREATED")

    root.mainloop()

    print("SIDEBAR TEST ENDED")