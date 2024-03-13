import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk


from tkinter import messagebox
global username
username = "Abdul"
def Generate():
    third_window=tk.Toplevel(window)
    third_window.title("output window")
    third_window.configure(bg="#333")
    print("welcome")

    average_label=tk.Label(third_window,text="Outputs ",font=("Ariel",12,"bold"),bg="#333",fg="#ffffff")
    average_label.grid(row=0,column=1)

    average_label=tk.Label(third_window,text="Average number of students in class",font=("Ariel",12),bg="#333",fg="#ffffff")
    average_label.grid(row=1,column=0,pady=10)
    average_entry=tk.Entry(third_window)
    average_entry.grid(row=2,column=0,padx=20)

    Temp_label=tk.Label(third_window,text="Temperature ",font=("Ariel",12),bg="#333",fg="#ffffff")
    Temp_label.grid(row=1,column=1)

    Temp_entry=tk.Entry(third_window)
    Temp_entry.grid(row=2,column=1,padx=20)

    status_label=tk.Label(third_window,text="Status",font=("Ariel",12),bg="#333",fg="#ffffff")
    status_label.grid(row=1,column=2)
    status_entry=tk.Entry(third_window)
    status_entry.grid(row=2,column=2,padx=20)

    

def create_second_window():
    second_window = tk.Toplevel(window)
    second_window.title("Welcome Page")
   
    second_window.configure(bg="#333")

    # Widgets for the second window
    welcome_label = tk.Label(second_window, text="Welcome! " + str(username), font=("Arial", 20), bg="#333", fg="#ffffff", pady=20)
    welcome_label.grid(row=0, column=2)

    venue_label = tk.Label(second_window, text="Here Is The List Of All Venue You can select ", font=("Arial", 10), bg="#333", fg="#ffffff", pady=20)
    venue_label.grid(row=1, column=1)

    locate_label=tk.Label(second_window,text="Where do You want to Study?",font=("Ariel",12),bg="#333",fg="#ffffff")
    locate_label.grid(row=6,column=0,pady=20)

    locate_entry=ttk.Combobox(second_window,font=("Ariel",12),values=("W15/4","W7F","W8R","W15/1","W15/2","B12"))
    locate_entry.grid(row=6,column=1,padx=20,pady=10)
    locate_entry.set("select the option")

    generate_button=tk.Button(second_window,text="GANERATE",bg="#333",fg="#ffffff",command=Generate)
    generate_button.grid(row=7,column=1,pady=20)
    

    # Labels for images
    image1_label = tk.Label(second_window)
    image1_label.grid(row=3, column=0, pady=10)
    image1_heading = tk.Label(second_window, text="W15/4", font=("Arial", 12), bg="#333", fg="#ffffff")
    image1_heading.grid(row=2, column=0)

    image2_label = tk.Label(second_window)
    image2_label.grid(row=3, column=1, pady=10)
    image2_heading = tk.Label(second_window, text="W15/1", font=("Arial", 12), bg="#333", fg="#ffffff")
    image2_heading.grid(row=2, column=1)

    image3_label = tk.Label(second_window)
    image3_label.grid(row=3, column=2, pady=10)
    image3_heading = tk.Label(second_window, text="W15/2", font=("Arial", 12), bg="#333", fg="#ffffff")
    image3_heading.grid(row=2, column=2)

    image4_label = tk.Label(second_window)
    image4_label.grid(row=5, column=0,pady=10)
    image4_heading = tk.Label(second_window, text="W8R", font=("Arial", 12), bg="#333", fg="#ffffff")
    image4_heading.grid(row=4, column=0)

    image5_label = tk.Label(second_window)
    image5_label.grid(row=5, column=1,pady=10)
    image5_heading = tk.Label(second_window, text="W7F", font=("Arial", 12), bg="#333", fg="#ffffff")
    image5_heading.grid(row=4, column=1)

    image6_label = tk.Label(second_window)
    image6_label.grid(row=5, column=2,pady=10)
    image6_heading = tk.Label(second_window, text="B12", font=("Arial", 12), bg="#333", fg="#ffffff")
    image6_heading.grid(row=4, column=2)


    # Load and display the first image
    image1 = Image.open("logo.png")
    image1 = image1.resize((100, 100), Image.LANCZOS)
    photo1 = ImageTk.PhotoImage(image1)
    image1_label.configure(image=photo1)
    image1_label.image = photo1  # Keep a reference

    # Load and display the second image
    image2 = Image.open("logo.png")
    image2 = image2.resize((100, 100), Image.LANCZOS)
    photo2 = ImageTk.PhotoImage(image2)
    image2_label.configure(image=photo2)
    image2_label.image = photo2  # Keep a reference

    image3 = Image.open("logo.png")
    image3 = image3.resize((100, 100), Image.LANCZOS)
    photo3 = ImageTk.PhotoImage(image3)
    image3_label.configure(image=photo3)
    image3_label.image = photo3  # Keep a reference

    image4 = Image.open("logo.png")
    image4 = image4.resize((100, 100), Image.LANCZOS)
    photo4 = ImageTk.PhotoImage(image4)
    image4_label.configure(image=photo4)
    image4_label.image = photo4  # Keep a reference

    image5 = Image.open("logo.png")
    image5 = image5.resize((100, 100), Image.LANCZOS)
    photo5 = ImageTk.PhotoImage(image5)
    image5_label.configure(image=photo5)
    image5_label.image = photo5  # Keep a reference

    image6 = Image.open("logo.png")
    image6 = image6.resize((100, 100), Image.LANCZOS)
    photo6 = ImageTk.PhotoImage(image6)
    image6_label.configure(image=photo6)
    image6_label.image = photo6  # Keep a reference

    

def login():
    username = "Abdul"
    password = "1234"
    if username_entry.get() == username and password_entry.get() == password:
        print("Successfully logged in")
        messagebox.showinfo(title="Successfully logged in", message="You are logged in successfully.")
        create_second_window()  # Call function to create and display second window
    else:
        print("Invalid login")
        messagebox.showerror(title="Invalid login", message="Invalid username or password.")

window = tk.Tk()
frame = tk.Frame(bg="#333")
window.title("Login Page")
window.geometry("500x500")
window.configure(bg="#333")

LOGIN_label = tk.Label(frame, text="LOGIN", font=("Arial", 20), bg="#333", fg="#ffffff", pady=40)
LOGIN_label.grid(row=0, column=1, columnspan=2)

username_label = tk.Label(frame, text="Username", font=("Arial", 16), bg="#333", fg="#ffffff", pady=20)
username_label.grid(row=1, column=0)
username_entry = tk.Entry(frame, font=("Arial", 20), borderwidth=12)
username_entry.grid(row=1, column=1)

password_label = tk.Label(frame, text="Password", font=("Arial", 16), bg="#333", fg="#ffffff", pady=20)
password_label.grid(row=2, column=0)
password_entry = tk.Entry(frame, font=("Arial", 20), show="*", borderwidth=12)
password_entry.grid(row=2, column=1)

LOGIN_button = tk.Button(frame, text="LOGIN", font=("Arial", 20), bg="pink", command=login)
LOGIN_button.grid(row=4, column=1, columnspan=2)

frame.pack()
window.mainloop()
