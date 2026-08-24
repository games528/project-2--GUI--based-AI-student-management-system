import tkinter as tk


def create_quick_actions(parent):
    quick_actions_frame = tk.Frame(
        parent,
        bg="#f5f6fa"
    )

    title = tk.Label(
        quick_actions_frame,
        text="Quick Actions",
        font=("Arial", 18, "bold"),
        bg="#f5f6fa"
    )

    title.pack(pady=(10, 15))
    add_student_button = tk.Button(
    quick_actions_frame,
    text="Add Student",
    font=("Arial", 12, "bold"),
    bg="#3498db",
    fg="white",
    relief="flat",
    padx=20,
    pady=10,
    command=lambda: print("Add Student clicked")
)

    add_student_button.pack(
    side="left",
    padx=10
)
    view_students_button = tk.Button(
    quick_actions_frame,
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
    padx=10
)
    add_academic_record_button = tk.Button(
    quick_actions_frame,
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
    padx=10
)
    mark_attendance_button = tk.Button(
    quick_actions_frame,
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
    padx=10
)
    generate_report_button = tk.Button(
    quick_actions_frame,
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
    padx=10
)
    return quick_actions_frame