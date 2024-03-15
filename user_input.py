import tkinter
from tkinter import *
from tkinter import messagebox

window = tkinter.Tk()
frame = tkinter.Frame(bg="#333")
window.title("Login Page")
window.geometry("500x500")
window.configure(bg="#333")

def Login():
    username = "Abdul"
    password = "1234"
    if username_entry.get() == username and password_entry.get() == password:

        print("successfully logged in")
        messagebox.showinfo(title="successfully login page ",message="your successfully logged in")
    else:
        Label(frame,text="invalid logged in").grid(row=6,column=0)
        print("invalid logged in")
        messagebox.showerror(title="invalid login page",message="invalid logged in")

LOGIN_label = Label(frame, text="LOGIN", font=("Arial", 20), bg="#333", fg="#ffffff", pady=40)
LOGIN_label.grid(row=0, column=1, columnspan=2)

username_label = Label(frame, text="Username", font=("Arial", 16), bg="#333", fg="#ffffff", pady=20)
username_label.grid(row=1, column=0)
username_entry = Entry(frame, font=("Arial", 20), borderwidth=12)
username_entry.grid(row=1, column=1)

password_label = Label(frame, text="Password", font=("Arial", 16), bg="#333", fg="#ffffff", pady=20)
password_label.grid(row=2, column=0)
password_entry = Entry(frame, font=("Arial", 20), show="*", borderwidth=12)
password_entry.grid(row=2, column=1)

LOGIN_button = Button(frame, text="LOGIN", font=("Arial", 20), bg="pink", command=Login)
LOGIN_button.grid(row=4, column=1, columnspan=2)

frame.pack()
window.mainloop()
