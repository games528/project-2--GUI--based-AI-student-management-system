from frontend.GUI.sidebar import create_sidebar
import tkinter as tk

def show_dashboard(root):
    create_sidebar(root)
    print("sidebar created in dashboard")
    dashboard_frame = tk.Frame(root, bg="#f5f6fa")
    dashboard_frame.pack(side="right", fill="both", expand=True)

    # Main title
    title_label = tk.Label(
        dashboard_frame,
        text="Student Management Dashboard",
        font=("Arial", 24, "bold"),
        bg="#f5f6fa")
    title_label.pack(pady=(40, 10))

    # Welcome text
    welcome_label = tk.Label(
        dashboard_frame,
        text="Welcome to the AI Based Student Management System",
        font=("Arial", 14),
        bg="#f5f6fa"
    )
    welcome_label.pack(pady=(0, 30))

    # Main content area
    content_frame = tk.Frame(
        dashboard_frame,
        bg="white",
        width=800,
        height=300
    )
    content_frame.pack(padx=50, pady=20)

    content_frame.pack_propagate(False)

    content_label = tk.Label(
        content_frame,
        text="Dashboard Content",
        font=("Arial", 18, "bold"),
        bg="white"
    )
    content_label.pack(expand=True)

    return dashboard_frame

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Student Management System")
    root.geometry("900x600")
    show_dashboard(root)
    root.mainloop()