'''This module stores all the code relating to the login feature of the program including creating an account or changing their password.'''

from tkinter import messagebox
from tkinter import simpledialog


def login(username_entry, password_entry, welcome_label, show_home):

    username = username_entry.get().strip()
    password = password_entry.get().strip() # Gets the password, and removes extra spaces from it

    if username == "":
        messagebox.showerror(
            "Error",
            "Please enter a username."
        )
        return

    if password == "":
        messagebox.showerror(
            "Error",
            "Please enter a password."
        )
        return

    file = open("users.txt","r")

    valid_login = False

    for line in file:

        if "," not in line: # This skips any blank lines, preventing crashes
            continue

        saved_username, saved_password = line.strip().split(",")

        if username == saved_username and password == saved_password:

            valid_login = True
            break

    file.close()

    if valid_login:

        welcome_label.config(
            text="Welcome " + username
        )

        show_home()

    else:

        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )


def create_account(username_entry,password_entry):

    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "":

        messagebox.showerror(
            "Error",
            "Please enter a username."
        ) # Gives the user an error message

        return

    if password == "":

        messagebox.showerror(
            "Error",
            "Please enter a password."
        )

        return

    file = open("users.txt","r")

    for line in file:

        saved_username,saved_password = line.strip().split(",") # Removes extra spaces and splits the pair

        if username == saved_username:

            messagebox.showerror(
                "Error",
                "That username already exists."
            ) # Error message for an already existent username

            file.close()

            return

    file.close()

    file = open("users.txt","a")

    file.write("\n"+username+","+password)

    file.close()

    messagebox.showinfo(
        "Account Created", # Notifies the user it was a success
        "Your account has been created successfully."
    )


def change_password(username_entry):

    username = username_entry.get().strip()

    new_password = simpledialog.askstring(
        "Change Password",
        "Enter your new password:"
    ).strip() # Removes extra spaces from the password

    if not new_password:

        messagebox.showerror(
            "Error",
            "Password cannot be blank."
        ) # If the password isn't viable, an error message occurs.

        return

    file = open("users.txt","r")

    lines = file.readlines()

    file.close()

    file = open("users.txt","w")

    for line in lines:

        saved_username,saved_password = line.strip().split(",")

        if saved_username == username:

            file.write(
                username+","+new_password+"\n"
            )

        else:

            file.write(line)

    file.close() # Closes the file

    messagebox.showinfo(
        "Success", # Notifies the user that the password was updated
        "Password updated successfully."
    )