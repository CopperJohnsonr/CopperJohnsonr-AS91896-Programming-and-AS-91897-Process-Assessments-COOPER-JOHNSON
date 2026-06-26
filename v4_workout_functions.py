'''This module stores all the generalized plans for A more organized code.'''

from tkinter import messagebox
from v4_data import workout_plans


def beginner_plan(): #

    exercises = "\n".join(workout_plans["Beginner"])

    messagebox.showinfo(
        "Beginner Workout Plan",
        exercises
    )


def intermediate_plan():

    exercises = "\n".join(workout_plans["Intermediate"])

    messagebox.showinfo(
        "Intermediate Workout Plan",
        exercises
    )


def advanced_plan():

    exercises = "\n".join(workout_plans["Advanced"])

    messagebox.showinfo(
        "Advanced Workout Plan",
        exercises
    )