"""
This script is used to generate a random workout from a list
of workouts depending on the muscle group(s) selected.

Written by Beefybison

"""

import random
from select import select
from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

MUSCLES = ("Biceps", "Triceps", "Chest", "Back", "Legs", "Shoulders", "Cardio")

BICEPS = [
    "barbell curls",
    "dumbbell curls",
    "hammber curls",
    "rope curls",
    "preacher curls",
    ]

TRICEPS = [
    "skullcrushers",
    "tricep kickback",
    "palms up triceps band kickback",
    "standing single arm triceps band extensions",
    "standing triceps band pushdowns",
    "kneeling triceps band pushdowns",
    "overhead triceps band extensions",
    ]

CHEST = [
    "bench press",
    "arnold press",
    "dumbbell flyes",
    "banded crossover push up",
    "resistance band low to high crossovers",
    ]

BACK = [
    "upright rows",
    "rows",
    "lat pulldown",
    "reverse flyes",
    "kettlebell swings"
    ]

LEGS = [
    "squats",
    "resistance band deadlift",
    "resistance band stiff-legged deadlift",
    "resistance band lunge to squat",
    ]

SHOULDERS = [
    "lateral raises",
    "military press",
    "incline benchpress",
    ]

CARDIO = [
    "star jumps",
    "jumping lunges",
    "high kness",
    ]

final_workout = []
workout_quantity_var = random.choice(range(2, 4)) # change theses numbers to add more or less workouts

class gym_comrade(App):
    """Configures window and adds checkboxes, widgets, and labels."""

    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.greeting = Label(
            text="What workout would you like today?",
            font_size = 25,
            color="#00FFCE"
            )
        self.window.add_widget(self.greeting)
    
        # Add checkbox, widget and labels
        self.window.add_widget(Label(text =''))
        self.active = CheckBox(active = False)
        self.window.add_widget(self.active)

        self.lbl_active = Label(text ='Biceps')
        self.window.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)
    
        self.window.add_widget(Label(text =''))
        self.active = CheckBox(active = False)
        self.window.add_widget(self.active)

        self.lbl_active = Label(text ='Triceps')
        self.window.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)
    
        self.window.add_widget(Label(text =''))
        self.active = CheckBox(active = False)
        self.window.add_widget(self.active)

        self.lbl_active = Label(text ='Chest')
        self.window.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)

        self.window.add_widget(Label(text =''))
        self.active = CheckBox(active = False)
        self.window.add_widget(self.active)

        self.lbl_active = Label(text ='Back')
        self.window.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)

        self.window.add_widget(Label(text =''))
        self.active = CheckBox(active = False)
        self.window.add_widget(self.active)

        self.lbl_active = Label(text ='Legs')
        self.window.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)

        self.window.add_widget(Label(text =''))
        self.active = CheckBox(active = False)
        self.window.add_widget(self.active)

        self.lbl_active = Label(text ='Shoulders')
        self.window.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)

        self.window.add_widget(Label(text =''))
        self.active = CheckBox(active = False)
        self.window.add_widget(self.active)

        self.lbl_active = Label(text ='Cardio')
        self.window.add_widget(self.lbl_active)

        self.active.bind(active = self.on_checkbox_Active)

        self.button = Button(
            text="GENERATE",
            bold = True,
            background_color = '#00FCE'
            )
        self.button.bind(on_press=self.on_press)
        self.window.add_widget(self.button)

        return self.window

    def on_checkbox_Active(checkbox, value, isActive):
        """Checks if the checkbox is active & primes the workout list."""
        if isActive == True:
            print(checkbox.lbl_active.text)
            if checkbox.lbl_active.text == 'Cardio':
                write_workout(CARDIO)
            return True
        else:
            return False

    def on_press(self, instance):
        """Updates the screen with the final workout."""
        self.greeting.font_size = 15
        self.greeting.text = str(final_workout)
        final_workout.clear()

def write_workout(muscle):
    """Generates the workout."""
    select_workout = str(random.sample(muscle, workout_quantity_var))
    final_workout.append(select_workout)

if __name__ == '__main__':
    gym_comrade().run()
