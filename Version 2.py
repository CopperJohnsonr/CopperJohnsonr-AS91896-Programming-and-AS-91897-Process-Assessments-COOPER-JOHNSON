'''
This is the second version of the Workout Helper program. This program is still simplistic, however to enhance the users experience, this
version utilizes the module called EasyGui. This creates A simplistic Graphical User Interface in which the user may interact with.
In addition to the previous version this program asks the user for relevant information that may effect their experience, such as their
name, so that the program becomes more personalized. Aside from this, the program asks the user what muscle they would like to exercise,
and then provides them with either the exercises, or an error message depending on the users input. This versions primary purpose is to
further increase usability and user experience.
'''

import easygui

# Muscles and Exercise Dictionary

workouts = {

    "arms": [
        ("💪 Bicep Curls", "Curl weights towards your shoulders."),
        ("💪 Push Ups", "Lower yourself to the floor and push back up."),
        ("💪 Tricep Dips", "Lower your body using a chair or bench.")
    ],

    "legs": [
        ("🦵 Squats", "Lower your hips and stand back up."),
        ("🦵 Lunges", "Step forward and lower your back knee."),
        ("🦵 Calf Raises", "Raise your heels and slowly lower them.")
    ],

    "chest": [
        ("🏋 Bench Press", "Push a weight upwards while lying down."),
        ("🏋 Push Ups", "Lower yourself to the floor and push back up."),
        ("🏋 Chest Fly", "Move weights outwards then together.")
    ],

    "core": [
        ("🔥 Plank", "Hold your body straight on your forearms."),
        ("🔥 Sit Ups", "Lift your upper body towards your knees."),
        ("🔥 Crunches", "Raise your shoulders using your abdominal muscles.")
    ],

    "back": [
        ("🔙 Deadlifts", "Lift weight from the floor with a straight back."),
        ("🔙 Pull Ups", "Pull yourself upwards using a bar."),
        ("🔙 Rows", "Pull a weight towards your torso.")
    ],

    # Added after trialling feedback from Timmy Chang
    "general": [
        ("🏃 Jogging", "Run at a steady pace."),
        ("🏃 Star Jumps", "Jump while spreading your arms and legs."),
        ("🏃 Burpees", "Perform a squat, jump and push up sequence."),
        ("🏃 Mountain Climbers", "Alternate knees towards your chest quickly.")
    ]
}

easygui.msgbox(  # Gives the user a message
    "💪 Welcome to Workout Helper!\n\nSelect a muscle group to receive exercise suggestions.",
    title="Workout Helper"
)

# Name Validation Loop

while True:

    name = easygui.enterbox(  # Creates an input box for the user
        "👤 Please enter your name:\n\n(Type 'skip' if you would prefer not to enter one)"
    )

    # Cancel button
    if name is None:
        easygui.msgbox(
            "Thank you for using my program ☺️\nProgram Closed.",
            title="Goodbye"
        )
        quit()

    name = name.strip()  # Removes any spaces within the users input

    # Allows the user to skip entering their name
    if name.lower() == "skip":
        name = "User" # Defaults the name to "User" so they can be referred to
        break

    # Error message for blank input
    if name == "":
        easygui.msgbox(
            "❌ Please enter a valid name.",
            title="Error"
        )

    # Numbers verification
    elif not name.isalpha():
        easygui.msgbox(
            "❌ Names cannot be numbers.",
            title="Error"
        )

    else:
        break  # Ends the loop

easygui.msgbox(
    "💪 Welcome " + name + "!\n\nLet's find some exercises for you.",
    title="Workout Helper"  # Sets the title of the window itself to "Workout Helper"
)

# Loop for muscle users muscle information

while True:

    muscle = easygui.enterbox(
        "💪 Which muscle would you like to exercise?\n\n"
        "Arms, Legs, Chest, Core, Back, General"
    )

    # cancel button
    if muscle is None:
        easygui.msgbox(
            "Thank you for using my program ☺️\nProgram Closed.",  # provides nice message for user experience
            title="Goodbye"
        )
        quit()  # Closes the program

    muscle = muscle.strip().lower()

    # Error message for an empty input
    if muscle == "":
        easygui.msgbox(
            "❌ Please enter a muscle group.",
            title="Error"
        )
        continue

    # Int/Float validation
    if muscle.isdigit():
        easygui.msgbox(
            "❌ Please enter a valid muscle group.",
            title="Error"
        )
        continue

    if muscle == "abs":
        muscle = "core"  # Based off previous trialing feedback from Reuben Gedge, Core may be interpreted as abs.

    if muscle in workouts:

        exercise_list = ""

        # Displays exercises and descriptions
        for exercise, description in workouts[muscle]:

            exercise_list += exercise + "\n"
            exercise_list += "   " + description + "\n\n"

        easygui.msgbox(
            "🏋 " + name + ", here are some exercises for " + muscle + ":\n\n" + exercise_list,
            title="Workout Suggestions"
        )

        # Added after trialing feedback from Jia Eng Lee
        again = easygui.buttonbox(
            "Would you like to view another muscle group?",
            choices=["Yes", "No"]
        )

        if again == "No":

            easygui.msgbox(
                "Thank you for using my program ☺️",
                title="Goodbye"
            )

            break

    else:
        easygui.msgbox( # Specified message from stakeholder feedback
            "❌ Muscle group not found.\n\n"
            "Try broad muscle groups such as:\n\n"
            "• Arms\n"
            "• Legs\n"
            "• Chest\n"
            "• Core\n"
            "• Back\n"
            "• General",
            title="Error"
        )