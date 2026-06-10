import ctypes
import tkinter as tk
from tkinter import messagebox
import mysql.connector
import hashlib

ctypes.windll.shcore.SetProcessDpiAwareness(0)

# DATABASE CONNECTION
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root", 
        password="root123", 
        database="student_system" 
    )


# MAIN APPLICATION CLASS
class StudentApp(tk.Tk):
    def _init_(self): 
        super()._init_()
        print("Main window created")
        self.title("Student Management System")
        self.geometry("600x500")
        self.configure(bg="#4B0082")

        self.current_user = None
        self.current_role = None
        self.current_student_id = None

        self.show_login_choice()

    def clear_screen(self):
        for widget in self .winfo_children():
            widget.destroy()

    def show_login_choice(self):
        self.clear_screen()
        tk.Label(
            self,
            text="Student Management System",
            font=("Arial", 20, "bold"),
            bg="#4B0082",
            fg="#4B0082"
        ).pack(pady=40)

        tk.Button(
            self,
            text="Student Login",
            font=("Arial", 14),
            width=20,
            bg="white",
            fg="#798200",
            activebackground="#5A0C9D",
            command=self.show_student_login
        ).pack(pady=10)

        tk.Button(
            self,
            text="Student Register",
            font=("Arial", 14),
            width=20,
            bg="white", 
            fg="#003482",
            activebackground="#0C939D",
            command=self.show_register
        ).pack(pady=10)

        tk.Button(
            self,
            text="Lecturer Login",
            font=("Arial", 14),
            width=20,
            bg="white",
            fg="#825F00",
            activebackground="#695D1F",
            command=self.show_lecturer_login
        ).pack(pady=10)
          
def show_student_login(self):
    self.clear_screen()

    tk.Label(self, text="Student Login", font=("Arial", 20)).pack(pady=20)

    tk.Label(self, text="Username").pack()
    username_entry = tk.Entry(self)
    username_entry.pack()

    tk.Label(self, text="Password").pack()
    password_entry = tk.Entry(self, show="*")
    password_entry.pack()

    def login():
        username = username_entry.get()
        password = password_entry.get()

        conn = get_connection()
        cursor = conn.cursor()

        hashed_password = hashlib.sha256(password.encode()).hexdigest()

        query = """ 
        SELECT student_id FROM login
        WHERE username=%s AND password_hash=%s AND role="student"
        """

        cursor.execute(query, (username, hashed_password))
        result = cursor.fetchone()

        if result:
            self.current_student_id = result[0]
            messagebox.showinfo("Success", "login successful")
            self.show_student_dashboard()
        else:
            messagebox.showerror("Error", "Invalid login")

        conn.close()

    tk.Button(self, text="Login", command=login).pack(pady=10)

    def show_student_dashboard(self):
        self.clear_screen()

        tk.Label(self, text="Student Dashboard", font=("Arial", 20)).pack(pady=20)

        tk.Button(self, text="View My Data").pack(pady=10)
        tk.Button(self, text="Update My Data").pack(pady=10)
        tk.Button(self, text="Logout", command=self.show_login_choice).pack(pady=10)
def show_register(self):
    pass

def show_lecturer_login(self):
    pass

if __name__=="__main__":
    app = StudentApp()
    app.mainloop()


