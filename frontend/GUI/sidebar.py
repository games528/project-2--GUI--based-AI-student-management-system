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