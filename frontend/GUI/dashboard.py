from frontend.GUI.sidebar import create_sidebar
from frontend.GUI.quick_actions import create_quick_actions
from backend.database import get_connection
from backend.database import create_student_table, create_academic_records_table
import tkinter as tk
from backend.database import(get_connection, create_student_table, create_academic_records_table,add_gender_column,get_boys_count,get_girls_count,create_attendance_table,get_average_attendance,get_average_percentage)

def get_total_students():
    conn = get_connection()
    if conn is None:
        return 0

    cursor = conn.cursor()

    cursor.execute("SELECT count(*) from students ")
    total = cursor.fetchone()[0]

    conn.close()

    return total

def show_dashboard(root):
    create_sidebar(root)
    dashboard_frame = tk.Frame(root, bg="#f5f6fa")
    dashboard_frame.pack(side="right", fill="both", expand=True)
    stats_frame = tk.Frame(
    dashboard_frame,
    bg="#f5f6fa"
)

    stats_frame.pack(
    fill="x",
    padx=30,
    pady=10
)
    
    

    # Main title
    title_label = tk.Label(
        stats_frame,
        text="Student Management Dashboard",
        font=("Arial", 24, "bold"),
        bg="#f5f6fa")
    title_label.pack(pady=(40, 10))

    # Welcome text
    welcome_label = tk.Label(
        stats_frame,
        text="Welcome to the AI Based Student Management System",
        font=("Arial", 14),
        bg="#f5f6fa"
    )
    welcome_label.pack(pady=(0, 30))

    # Main content area
    content_frame = tk.Frame(
        stats_frame,
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
    
    total_students_card = tk.Frame(
    stats_frame,
    bg="white",
    width=150,
    height=80
)

    total_students_card.pack(
    side="left",
    padx=10,
    pady=10
)

    total_students_card.pack_propagate(False)

    total_students_title = tk.Label(   
    total_students_card,
    text="Total Students",
    font=("Arial", 14, "bold"),
    bg="white"
)

    total_students_title.pack(pady=(5, 2))

    total_students_value = tk.Label(
    total_students_card,
    text=str(get_total_students()),
    font=("Arial", 24, "bold"),
    bg="white"
)

    total_students_value.pack()
    boys_card = tk.Frame(
    stats_frame,
    bg="white",
    width=150,
    height=80
)

    boys_card.pack(
    side="left",
    padx=10,
    pady=10
)

    boys_card.pack_propagate(False)

    boys_title = tk.Label(
    boys_card,
    text="Boys",
    font=("Arial", 14, "bold"),
    bg="white"
)

    boys_title.pack(pady=(5, 2))

    boys_value = tk.Label(
    boys_card,
    text=str(get_boys_count()),
    font=("Arial", 24, "bold"),
    bg="white"
)
    

    boys_value.pack()


    girls_card = tk.Frame(
    stats_frame,
    bg="white",
    width=150,
    height=80
)

    girls_card.pack(
    side="left",
    padx=10,
    pady=10
)

    girls_card.pack_propagate(False)

    girls_title = tk.Label(
    girls_card,
    text="Girls",
    font=("Arial", 14, "bold"),
    bg="white"
)

    girls_title.pack(pady=(20, 5))

    girls_value = tk.Label(
    girls_card,
    text=str(get_girls_count()),
    font=("Arial", 24, "bold"),
    bg="white"
)

    girls_value.pack()
    attendance_card = tk.Frame(
    stats_frame,
    bg="white",
    width=220,
    height=80
)

    attendance_card.pack(
    side="left",
    padx=20,
    pady=10
)

    attendance_card.pack_propagate(False)

    attendance_title = tk.Label(
    attendance_card,
    text="Average Attendance",
    font=("Arial", 14, "bold"),
    bg="white"
)

    attendance_title.pack(pady=(20, 5))

    attendance_value = tk.Label(
    attendance_card,
    text=str(get_average_attendance()) + "%",
    font=("Arial", 24, "bold"),
    bg="white"
)

    attendance_value.pack()
    percentage_card = tk.Frame(
    stats_frame,
    bg="white",
    width=220,
    height=80
)

    percentage_card.pack(
    side="left",
    padx=20,
    pady=10
)

    percentage_card.pack_propagate(False)

    percentage_title = tk.Label(
    percentage_card,
    text="Average Percentage",
    font=("Arial", 14, "bold"),
    bg="white"
)

    percentage_title.pack(pady=(20, 5))

    percentage_value = tk.Label(
    percentage_card,
    text=str(get_average_percentage()) + "%",
    font=("Arial", 24, "bold"),
    bg="white"
)

    percentage_value.pack()
    def refresh_dashboard_stats():
     total_students_value.config(
        text=str(get_total_students())
    )

    boys_value.config(
        text=str(get_boys_count())
    )

    girls_value.config(
        text=str(get_girls_count())
    )

    attendance_value.config(
        text=str(get_average_attendance()) + "%"
    )
    percentage_value.config(
       text=str(get_average_percentage()) + "%"
    )

    quick_actions_frame = create_quick_actions(dashboard_frame, refresh_dashboard_stats)
    quick_actions_frame.pack(side = "top", fill = "x", padx = 10, pady = (2,5))
    print("total students: ", get_total_students())
    
    return dashboard_frame

if __name__ == "__main__":
    create_student_table()
    create_academic_records_table()
    add_gender_column()
    create_attendance_table()
    root = tk.Tk()
    root.title("student management system")
    root.geometry("1700x1000")
    show_dashboard(root)
    root.mainloop()