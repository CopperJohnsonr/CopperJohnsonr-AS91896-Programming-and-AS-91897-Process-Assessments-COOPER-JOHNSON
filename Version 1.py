'''
This is Version 1 of the Workout Helper program. This program is a simplistic version, in which it will 
assist the user, providing them information regarding an exercise, and allow them to try it in their own
time. Version 1 is the base layer of the program in which each other version will build upon, until the 
final version and thus program is created, ensuring it is effective. This version provides the user with
generalized muscle groups to choose from.
'''

# Muscles and Exercise Dictionary
workouts = {
    "arms": [
        ("Bicep Curls", "Hold a weight in each hand and curl them towards your shoulders."),
        ("Push Ups", "Lower your body towards the floor and push back up."),
        ("Tricep Dips", "Use a chair or bench and lower yourself using your arms.")
    ],

    "legs": [
        ("Squats", "Bend your knees and lower your hips before standing back up."),
        ("Lunges", "Step forward and lower your back knee towards the ground."),
        ("Calf Raises", "Raise your heels off the ground and slowly lower them.")
    ],

    "chest": [
        ("Bench Press", "Push a weight upwards while lying on a bench."),
        ("Push Ups", "Lower your body towards the floor and push back up."),
        ("Chest Fly", "Move weights outwards and back together while lying down.")
    ],

    "core": [ # Core is also mapped as abs, so that the user can enter either
        ("Plank", "Hold your body straight while resting on your forearms and toes."),
        ("Sit Ups", "Raise your upper body towards your knees while lying down."),
        ("Crunches", "Lift your shoulders slightly off the floor using your abdominal muscles.")
    ],

    "back": [
        ("Deadlifts", "Lift a weight from the ground while keeping your back straight."),
        ("Pull Ups", "Pull yourself upwards using a bar."),
        ("Rows", "Pull a weight towards your body while keeping your back straight.")
    ] # Provides the user with the name and description of the exercises recommended 
}

running = True # Sets the code to start (Starts running)

while running:

    print("\n------- WORKOUT HELPER -------")
    print("Muscle groups: Arms, Legs, Chest, Core, Back") # Provides the user with options 
    print("Type 'exit' to quit") # Gives the user a back-out option

    muscle = input("\nEnter a muscle group: ").strip().lower()

    if muscle == "exit":
        print("Hope our information provided useful!")
        running = False # Ends the code

    elif muscle == "abs":
        muscle = "core"

        print("\nExercises for", muscle, ":")

        for exercise, description in workouts[muscle]:
            print("-", exercise) # Prints the exercise of specified muscle group and its paired description
            print(" ", description)

    elif muscle in workouts:
        print("\nExercises for", muscle, ":")

        for exercise, description in workouts[muscle]:
            print("-", exercise)
            print(" ", description)

    elif muscle == "":
        print("Please enter a muscle group") # Error message if the user just presses enter

    else:
        print("Muscle group not found. Please try another muscle") # Error message for unknown input
