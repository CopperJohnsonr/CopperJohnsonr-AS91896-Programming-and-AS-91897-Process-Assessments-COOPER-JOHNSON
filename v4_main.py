'''
This is the fourth version of my workout helper program. This version, in addition to the changes to Version 3, has a customizable 
background, which can switch colour for a better user experience. Each exercise is paired with a corresponding image. Additionally,
this program comes with pre-created generalized workouts for three levels of experience for it the user just wants to generally get
fitter. The purpose of this version is to further improve the users experience, and to make the program more visually appealing, and
 thus more appealing for the user. This version has an interactable diagram for finding muscle groups, to increase user experience. 
'''
# Importing Libraries & Modules (Many)
from v4_data import workouts
from v4_data import workout_plans
from v4_data import exercise_images
from v4_workout_functions import beginner_plan
from v4_workout_functions import intermediate_plan # Modular imports
from v4_workout_functions import advanced_plan
from v4_login import login
from v4_login import create_account
from v4_login import change_password
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog # uses simpledialog, allowing the user to change their password or create an account
import matplotlib.pyplot as plt
from datetime import date # Uses the date module for storing the date when the program is opened
import os # Uses the "os" module to check if files exist, or create them if they do not
from PIL import Image, ImageTk # Uses Pillow to display images

if os.path.exists("opens.txt"): # This checks if a the file "opens.txt" exists

    try:

        file = open("opens.txt", "r")
        count = int(file.read()) # Reads the number stored in the file
        file.close()

    except:

        count = 0 # Prevents possible crashes if the file is empty

else:
    count = 0 # If the file does not exist, it creates a new file, and sets its count to 0.
count += 1 # Adds to the count once the program is opened

file = open("opens.txt", "w") # Saves the updated count into the file
file.write(str(count))
file.close()

# Storing date everytime the program is opened.

today = str(date.today()) # This takes the current date, storing it into the usage log file.

file = open("usage_log.txt", "a")

file.write(today + "\n") # Adds the date to the file, and a new line for the next time the program is opened.

file.close()

# Main Window

root = tk.Tk()
root.title("Workout Helper") # Sets window title
root.geometry("660x550") # Sets the window dimensions

# MAkes the code remain in its theme
if os.path.exists("theme.txt"):

    file = open("theme.txt","r")

    theme = file.read().strip()

    file.close()

# Frame Functions

def show_home():

    login_frame.pack_forget()
    workout_frame.pack_forget()

    home_frame.pack() # Shows the home frame, and hides the other two frames

def muscle_click(event): # Runs whenever the mouse clicks (its considered an event)

    x = event.x # This reads the position of the mouse click using x and y axis
    y = event.y

    # Arms
    if 20 <= x <= 60 and 60 <= y <= 120:
        muscle_entry.delete(0, tk.END)
        muscle_entry.insert(0, "arms")

    # Chest
    elif 55 <= x <= 100 and 55 <= y <= 95: # Checks whether the click hit any of these coords
        muscle_entry.delete(0, tk.END)
        muscle_entry.insert(0, "chest") # If it does, it enters the muscle name, if not, it empties the entrybox (hence delete & insert)

    # Core
    elif 55 <= x <= 100 and 95 <= y <= 140: # Core Region
        muscle_entry.delete(0, tk.END)
        muscle_entry.insert(0, "core")

    # Legs
    elif 40 <= x <= 90 and 145 <= y <= 230:
        muscle_entry.delete(0, tk.END)
        muscle_entry.insert(0, "legs")

    # Back
    elif 200 <= x <= 270 and 45 <= y <= 150:
        muscle_entry.delete(0, tk.END)
        muscle_entry.insert(0, "back")
    
def show_workout():

    home_frame.pack_forget() # Hides the home frame, showing the workout frame

    workout_frame.pack()

def search_muscle():

    muscle = muscle_entry.get().lower().strip()

    if muscle == "":
        messagebox.showerror(
            "Error", # Provides an error message
            "Please enter a muscle group. Press OK to try again."
        )
        return

    if muscle == "abs":
        muscle = "core" # Sets an alternative answer

    if muscle in workouts:

        exercises = "\n".join(workouts[muscle])

        exercise_window = tk.Toplevel(root)
        exercise_window.title("Workout Suggestions")

        tk.Label(
            exercise_window,
            text=exercises, # Shows the user the stored exercises
            font=("Arial", 12)
        ).pack(pady=10)

        # Display the image for the first exercise (if one exists)
        first_exercise = workouts[muscle][0][2:]

        if first_exercise in exercise_images:

            image = Image.open(exercise_images[first_exercise])
            image = image.resize((220, 220))

            photo = ImageTk.PhotoImage(image)

            image_label = tk.Label(
                exercise_window,
                image=photo
            )

            image_label.image = photo
            image_label.pack(pady=10)

    else:

        messagebox.showerror(
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
    plt.xlabel("Date Opened")
    plt.ylabel("Times Opened")

    plt.xticks(rotation=45)

    plt.tight_layout() # Preventing labels from overlapping

    plt.show()

# Exercise Image Function

def show_exercise_image(exercise_name):

    if exercise_name not in exercise_images:

        return

    image_window = tk.Toplevel(root) # tk.Toplevel creates a new window, to display the image

    image_window.title(exercise_name)

    image = Image.open(exercise_images[exercise_name])

    image = image.resize((300, 300))

    photo = ImageTk.PhotoImage(image) # This is needed to convert the image into a format so Tkinter can display it

    image_label = tk.Label(
        image_window,
        image=photo
    )

    image_label.image = photo

    image_label.pack(pady=10)


# Theme Function
def dark_theme():

    root.configure(bg="#2c2c2c")

    login_frame.configure(bg="#2c2c2c")
    home_frame.configure(bg="#2c2c2c")
    workout_frame.configure(bg="#2c2c2c")

    file = open("theme.txt","w")
    file.write("dark")
    file.close()

def light_theme():

    root.configure(bg="SystemButtonFace")

    login_frame.configure(bg="SystemButtonFace")
    home_frame.configure(bg="SystemButtonFace")
    workout_frame.configure(bg="SystemButtonFace")

    file = open("theme.txt","w")
    file.write("light")
    file.close()

if os.path.exists("theme.txt"):

    file = open("theme.txt","r")
    theme = file.read().strip()
    file.close()

    if theme == "dark":
        dark_theme()

# Reset Program Usage

def reset_usage():

    global count # This allows the function to change the global count to 0 throughout the program

    count = 0

    file = open("opens.txt", "w")
    file.write("0")
    file.close()

    usage_label.config(
        text="Program opened 0 times"
    )

    messagebox.showinfo(
        "Reset Complete",
        "Usage data has been reset."
    )

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


# Help file
def show_help():

    file = open("help.txt","r")

    text = file.read()

    file.close()

    messagebox.showinfo(
        "Help",
        text
    )
tk.Button( # Creates the login button
    login_frame,
    text="Login",
    command=lambda: login(
    username_entry,
    password_entry,
    welcome_label,
    show_home
)
).pack(pady=10)

tk.Button(
    login_frame,
    text="Create Account",
    command=lambda: create_account(
    username_entry,
    password_entry
)
).pack(pady=5)

# Home Frame
home_frame = tk.Frame(root) # Creates the home frame (main menu)

# Organizing menu through columns

left_frame = tk.Frame(home_frame)
middle_frame = tk.Frame(home_frame)
right_frame = tk.Frame(home_frame)

left_frame.pack(side="left", padx=20)
middle_frame.pack(side="left", padx=20)
right_frame.pack(side="left", padx=20)

welcome_label = tk.Label(
    middle_frame,
    text="Welcome User",
    font=("Arial", 16)
)

welcome_label.pack(pady=10)
# Adding a welcome image to increase user experience, this is based on Timmy's feedback.
logo = Image.open("images/welcome.png")
logo = logo.resize((180,180))

logo_photo = ImageTk.PhotoImage(logo)

logo_label = tk.Label(
    middle_frame,
    image=logo_photo
)

logo_label.image = logo_photo
logo_label.pack(pady=10)

# Buttons

tk.Button(
    middle_frame,
    text="Help",
    command=show_help
).pack(pady=5)

usage_label = tk.Label(
    middle_frame,
    text="Program opened " + str(count) + " times"
)

usage_label.pack(pady=10)

tk.Button( # Creates the button to view the usage graph
    left_frame,
    text="View Usage Graph",
    command=show_graph
).pack(pady=5)

tk.Button(
    left_frame,
    text="Find Exercises",
    command=show_workout
).pack(pady=5)

# Workout Plans - creates a button for each workout plan

tk.Button(
    right_frame,
    text="Beginner Plan",
    command=beginner_plan
).pack(pady=5)

tk.Button(
    right_frame,
    text="Intermediate Plan",
    command=intermediate_plan
).pack(pady=5)

tk.Button(
    right_frame,
    text="Advanced Plan",
    command=advanced_plan
).pack(pady=5)

# Theme Buttons

tk.Button(
    left_frame,
    text="Dark Mode",
    command=dark_theme
).pack(pady=5)

tk.Button(
    left_frame,
    text="Light Mode",
    command=light_theme
).pack(pady=5)

# Button for changing passwords
tk.Button(
    home_frame,
    text="Change Password",
    command=lambda: change_password(
    username_entry
)
).pack(pady=5)

# Reset usage data button
tk.Button(
    home_frame,
    text="Reset Usage Data",
    command=reset_usage
).pack(pady=5)

# Workout Frame

workout_frame = tk.Frame(root)
muscle_image = Image.open("images/diagram.png")
muscle_image = muscle_image.resize((300,300))
muscle_photo = ImageTk.PhotoImage(muscle_image)
image_label = tk.Label(workout_frame, image=muscle_photo)
image_label.image = muscle_photo
image_label.bind("<Button-1>", muscle_click) # Allows for clicking on the diagram
image_label.pack()

tk.Label( # Creates the workout frame paired with a title and changed font
    workout_frame,
    text="Enter a Muscle Group"
).pack(pady=10)

muscle_entry = tk.Entry(workout_frame)
muscle_entry.pack() # Creates an entry-box for the user to input a muscle group.

tk.Button(
    workout_frame,
    text="Search",
    command=search_muscle # runs the search_muscle function when clicked
).pack(pady=5)

tk.Button(
    workout_frame,
    text="Back",
    command=show_home
).pack(pady=5)

# Starts the Program

login_frame.pack()

root.mainloop() # Runs the program, starting with the login frame