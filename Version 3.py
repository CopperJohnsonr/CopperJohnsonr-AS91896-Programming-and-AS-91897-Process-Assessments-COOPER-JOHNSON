'''
This is the third version of my workout helper program. This version utilizes the module Tkinter, which allows for a
more in-depth experience for the user. It is easier to interact with, and to increase this further, 
the program uses graphing software called Matploblib. This is aimed to help the user with their organization, 
seeing the flaws in their consistency, and allows them to track their progress over time. This version will 
also allow the user to log their times, and check how often they exercise, in a polite manner. This versions purpose
is to improve the useability of the program, and the users experience.
'''

# Importing Libraries
import tkinter as tk # Uses Tkinter for the GUI, to replace EasyGui.
from tkinter import messagebox
from tkinter import simpledialog
import matplotlib.pyplot as plt
from datetime import date
import os

# Creates a user file if they don't have one

if not os.path.exists("users.txt"):

    file = open("users.txt", "w")

    file.write(
        "Cooper,password123\n"
        "Admin,fitness\n"
        "Guest,guest"
    )
    file.close()
# Creates usage log file if it doesn't exist

if not os.path.exists("usage_log.txt"):

    file = open("usage_log.txt", "w")
    file.close()


# Exercise Dictionary

workouts = {

    "arms": [
        "💪 Bicep Curls",
        "💪 Push Ups",
        "💪 Tricep Dips"
    ], # Utilizes emojis to make the program more engaging

    "legs": [
        "🦵 Squats",
        "🦵 Lunges",
        "🦵 Calf Raises"
    ],

    "chest": [
        "🏋 Bench Press",
        "🏋 Push Ups",
        "🏋 Chest Fly"
    ],

    "core": [
        "🔥 Plank",
        "🔥 Sit Ups",
        "🔥 Crunches"
    ],

    "back": [
        "🔙 Deadlifts",
        "🔙 Pull Ups",
        "🔙 Rows"
    ]
}

# Counts how many times the program has been opened (For streaks)

if os.path.exists("opens.txt"): # This checks if a the file "opens.txt" exists

    try:

        file = open("opens.txt", "r")
        count = int(file.read()) # Reads the number stored in the file
        file.close()

    except:

        count = 0 # Prevents crashes if the file becomes corrupted

else:
    count = 0 # If the file does not exist, it creates a new file, and sets its count to 0.
count += 1

file = open("opens.txt", "w") # Saves the updated count into the file
file.write(str(count))
file.close()

# Storing date everytime the program is opened.

today = str(date.today())

file = open("usage_log.txt", "a")

file.write(today + "\n")

file.close()

# Main Window

root = tk.Tk()
root.title("Workout Helper") # Sets window title
root.geometry("500x400")

# Frame Functions

def show_home():

    login_frame.pack_forget()
    workout_frame.pack_forget()

    home_frame.pack() # Shows the home frame, and hides the other two frames


def show_workout():

    home_frame.pack_forget() # Hides the home frame, showing the workout frame

    workout_frame.pack()


def search_muscle(): # This function runs when the search button is clicked.

    muscle = muscle_entry.get().lower().strip() # This gets the text inputted by the user, removes any additional spaces and makes it all lowercase

    if muscle == "abs":
        muscle = "core" # As per version one feedback, the program takes "abs" as "core", as they equate to the same muscles.

    if muscle in workouts: # Checks if the muscle group is in the dictionary

        exercises = "\n".join(workouts[muscle])

        messagebox.showinfo(
            "Workout Suggestions",
            exercises # Displays exercises
        )

    elif muscle =="":
        messagebox.showerror( # Provides an error message for a blank input
            "Error",
            "Please enter a muscle group. Press ok to try again."
        )

    else:

        messagebox.showerror( # Displays error message for an invalid input
            "Error",
            "Muscle group not found.\nTry arms, legs, chest, core, or back."
        )


def show_graph(): # Displays a graph that plots time of day vs times opened

    file = open("usage_log.txt", "r")

    dates = file.readlines() # Reads all stored data

    file.close()

    usage_data = {} # Creating to store dates and their counts

    for entry in dates:

        entry = entry.strip()

        if entry in usage_data:

            usage_data[entry] += 1 # increases the count for that date by 1

        else:

            usage_data[entry] = 1

    x = list(usage_data.keys()) # Stores the dates for the x-axis, and the number of opens for the y-axis.
    y = list(usage_data.values())

    plt.plot(x, y, marker="o")

    plt.title("Program Usage By Date")
    plt.xlabel("Date")
    plt.ylabel("Times Opened")

    plt.xticks(rotation=45)

    plt.tight_layout() # Preventing labels from overlapping

    plt.show()

# Resets all the usage data collected

def reset_usage():

    global count # Allows the function to modify the count

    count = 0

    file = open("opens.txt", "w")

    file.write("0")

    file.close() # Clears stored usage dates

    file = open("usage_log.txt", "w")

    file.close()

    usage_label.config(
        text="Program opened 0 times" # Updates the label for the user
    )

    messagebox.showinfo(
        "Reset Complete",
        "Usage data has been reset."
    ) # Tells the user that the program has reset

# Login Frame

login_frame = tk.Frame(root) # Creates login frame

tk.Label( # Creates login title, increases its font size and adds padding for aesthetics
    login_frame,
    text="Workout Helper Login",
    font=("Arial", 16) # Sets font size and type
).pack(pady=10)

tk.Label(login_frame, text="Username").pack()

username_entry = tk.Entry(login_frame)
username_entry.pack()

tk.Label(login_frame, text="Password").pack()

password_entry = tk.Entry(
    login_frame,
    show="*" # Creates a entrybox for the password, puts the text as "*"s for privacy.
)
password_entry.pack()


def login(): # Creates the login function

    username = username_entry.get().strip() # Removes unnecessary spaces
    password = password_entry.get().strip()

    # Checks for blank usernames

    if username == "":

        messagebox.showerror(
            "Error",
            "Please enter a username before logging in."
        )

        return

    # Checks for blank passwords

    if password == "": # The blank input is "".

        messagebox.showerror(
            "Error",
            "Please enter a password before logging in."
        )

        return

    file = open("users.txt", "r")

    valid_login = False

    # Reads every username and password stored in users.txt

    for line in file:

        saved_username, saved_password = line.strip().split(",")

        if username == saved_username and password == saved_password:

            valid_login = True
            break

    file.close()

    # If both the username and password match 

    if valid_login:

        welcome_label.config(
            text="Welcome " + username # This updates the welcome message to include username, for a better user experience
        )

        show_home()

    # Incorrect login details

    else:

        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )

# Create account function
def create_account():

    username = username_entry.get().strip()
    password = password_entry.get().strip()

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

    file = open("users.txt", "r")

    for line in file:

        saved_username, saved_password = line.strip().split(",")

        if username == saved_username:

            messagebox.showerror(
                "Error",
                "That username already exists."
            )

            file.close()
            return

    file.close()

    file = open("users.txt", "a")

    file.write("\n" + username + "," + password)

    file.close()

    messagebox.showinfo(
        "Account Created",
        "Your account has been created successfully."
    )

# Allows users to change their password

def change_password():

    username = username_entry.get().strip()

    new_password = simpledialog.askstring(
        "Change Password",
        "Enter your new password:" # Asks the user to input a new password
    )

    if not new_password:

        return # Stops the function if the user cancels or inputs a blank password

    file = open("users.txt", "r")

    lines = file.readlines()

    file.close()

    file = open("users.txt", "w")

    for line in lines:

        saved_username, saved_password = line.strip().split(",")

        if saved_username == username:

            file.write(
                username + "," + new_password + "\n"
            ) # Replaces the old password with the users updated one

        else:

            file.write(line)

    file.close()

    messagebox.showinfo(
        "Success",
        "Password updated successfully."
    )

tk.Button(
    login_frame,
    text="Login",
    command=login
).pack(pady=10)

tk.Button(
    login_frame,
    text="Create Account",
    command=create_account
).pack(pady=5)

tk.Button(
    login_frame,
    text="Change Password",
    command=change_password
).pack(pady=5)

# Home Frame

home_frame = tk.Frame(root) # Creates the home frame (main menu)

welcome_label = tk.Label(
    home_frame,
    text="Welcome User",
    font=("Arial", 16)
)

welcome_label.pack(pady=10)

usage_label = tk.Label(
    home_frame,
    text="Program opened " + str(count) + " times"
)

usage_label.pack(pady=10)

tk.Button(
    home_frame,
    text="View Usage Graph",
    command=show_graph
).pack(pady=5)

tk.Button(
    home_frame,
    text="Find Exercises",
    command=show_workout
).pack(pady=5)

tk.Button(
    home_frame,
    text="Change Password",
    command=change_password
).pack(pady=5)

tk.Button(
    home_frame,
    text="Reset Usage Data",
    command=reset_usage
).pack(pady=5)

# Workout Frame

workout_frame = tk.Frame(root)

tk.Label( # Creates the workout frame paired with a title and changed font
    workout_frame,
    text="Enter a Muscle Group"
).pack(pady=10)

muscle_entry = tk.Entry(workout_frame)
muscle_entry.pack() # Creates an entrybox for the user to input a muscle group.

tk.Button(
    workout_frame,
    text="Search",
    command=search_muscle
).pack(pady=5)

tk.Button(
    workout_frame,
    text="Back",
    command=show_home
).pack(pady=5)

# Start Program

login_frame.pack()

root.mainloop() # Runs the program, starting with the login frame