try:
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("This is line 1.\n")
        file.write("12345\n")
        file.write("Another line with some numbers: 42, 55, 78\n")
    print("File created and initial content written successfully.")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
    print("Additional content ppended to my_file.txt.")

except FileNotFoundError:
    print("Error: File not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Script execution completed.")
