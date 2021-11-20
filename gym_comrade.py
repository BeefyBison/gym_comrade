"""
This script is used to generate a random workout from a list
of workouts depending on the muscle group(s) selected.

Written by Beefybison

"""

import tkinter as tk
from tkinter import TOP, X, GROOVE
import random
from checkbar import Checkbar

if __name__ == "__main__":

    def write_workout():
        """This function is what posts the workout when the button is pressed"""

        workout_quantity_var = random.choice(range(2, 4))
        mgroup = list(lng.state())

        if mgroup[0] == 1:
            for _i in range(1):
                T.insert(tk.END, random.choice(range(2, 6)))
                T.insert(tk.END, " sets:\n")
                T.insert(tk.END, random.sample(biceps, workout_quantity_var))
                T.insert(tk.END, "\n")
        else:
            pass

        if mgroup[1] == 1:
            for _i in range(1):
                T.insert(tk.END, random.choice(range(2, 6)))
                T.insert(tk.END, " sets:\n")
                T.insert(tk.END, random.sample(triceps, workout_quantity_var))
                T.insert(tk.END, "\n")
        else:
            pass

        if mgroup[2] == 1:
            for _i in range(1):
                T.insert(tk.END, random.choice(range(2, 6)))
                T.insert(tk.END, " sets:\n")
                T.insert(tk.END, random.sample(chest, workout_quantity_var))
                T.insert(tk.END, "\n")
        else:
            pass

        if mgroup[3] == 1:
            for _i in range(1):
                T.insert(tk.END, random.choice(range(2, 6)))
                T.insert(tk.END, " sets:\n")
                T.insert(tk.END, random.sample(back, workout_quantity_var))
                T.insert(tk.END, "\n")
        else:
            pass

        if mgroup[4] == 1:
            for _i in range(1):
                T.insert(tk.END, random.choice(range(2, 6)))
                T.insert(tk.END, " sets:\n")
                T.insert(tk.END, random.sample(legs, workout_quantity_var))
                T.insert(tk.END, "\n")
        else:
            pass

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    T = tk.Text(root, height=30, width=100)
    T.pack(side=tk.LEFT)
    scroll = tk.Scrollbar(root, command=T.yview)
    T.configure(yscrollcommand=scroll.set)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    exit_button = tk.Button(frame, text="QUIT", fg="red", command=quit)
    exit_button.pack(side=tk.LEFT)

    begin_button = tk.Button(frame, text="Generate", fg="green", command=write_workout)
    begin_button.pack(side=tk.LEFT)

    muscles = ["Biceps", "Triceps", "Chest", "Back", "Legs"]
    lng = Checkbar(root, muscles)
    lng.pack(side=TOP, fill=X)
    lng.config(relief=GROOVE, bd=2)

    triceps = [
        "skullcrushers",
        "tricep kickback",
        "palms up triceps band kickback",
        "standing single arm triceps band extensions",
        "standing triceps band pushdowns",
        "kneeling triceps band pushdowns",
        "overhead triceps band extensions",
    ]

    biceps = [
        "barbell curls",
        "dumbbell curls",
        "hammber curls",
        "rope curls",
        "preacher curls",
    ]

    chest = [
        "bench press",
        "arnold press",
        "resistance band chest press",
        "banded crossover push up",
        "resistance band low to high crossovers",
    ]

    back = ["rows", "lat pulldown", "reverse flyes", "kettlebell swings"]

    legs = [
        "squats",
        "resistance band deadlift",
        "resistance band stiff-legged deadlift",
        "resistance band lunge to squat",
    ]
