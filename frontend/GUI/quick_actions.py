import tkinter as tk


def create_quick_actions(parent, refresh_total_students=None):

    quick_actions_frame = tk.Frame(
        parent,
        bg="#f5f6fa"
    )

    # Title
    title = tk.Label(
        quick_actions_frame,
        text="Quick Actions",
        font=("Arial", 18, "bold"),
        bg="#f5f6fa"
    )

    title.pack(pady=(10, 15))

    # Frame for buttons
    buttons_frame = tk.Frame(
        quick_actions_frame,
        bg="#f5f6fa"
    )

    buttons_frame.pack()

    # Add Student
    add_student_button = tk.Button(
        buttons_frame,
        text="Add Student",
        font=("Arial", 12, "bold"),
        bg="#3498db",
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        command=lambda: (
            refresh_total_students()
            if refresh_total_students else None
        )
    )

    add_student_button.pack(
        side="left",
        padx=5
    )

    # View Students
    view_students_button = tk.Button(
        buttons_frame,
        text="View Students",
        font=("Arial", 12, "bold"),
        bg="#2ecc71",
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        command=lambda: print("View Students clicked")
    )

    view_students_button.pack(
        side="left",
        padx=5
    )

    # Add Academic Record
    add_academic_record_button = tk.Button(
        buttons_frame,
        text="Add Academic Record",
        font=("Arial", 12, "bold"),
        bg="#9b59b6",
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        command=lambda: print("Add Academic Record clicked")
    )

    add_academic_record_button.pack(
        side="left",
        padx=5
    )

    # Mark Attendance
    mark_attendance_button = tk.Button(
        buttons_frame,
        text="Mark Attendance",
        font=("Arial", 12, "bold"),
        bg="#e67e22",
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        command=lambda: print("Mark Attendance clicked")
    )

    mark_attendance_button.pack(
        side="left",
        padx=5
    )

    # Generate Report
    generate_report_button = tk.Button(
        buttons_frame,
        text="Generate Report",
        font=("Arial", 12, "bold"),
        bg="#1abc9c",
        fg="white",
        relief="flat",
        padx=20,
        pady=10,
        command=lambda: print("Generate Report clicked")
    )

    generate_report_button.pack(
        side="left",
        padx=5
    )

    return quick_actions_frame