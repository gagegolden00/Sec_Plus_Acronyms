
import tkinter as tk
from tkinter import font
from random import randint, choice
from data_page import *
from PIL import Image, ImageTk

# Move the score outside of the next_game() function so it's not reset every time
root = tk.Tk()
root.attributes('-fullscreen', True)
root.title("Sec + Acronyms")
screen_width = 700
screen_height = 700

# Fonts
small_font = font.Font(family="systemfixed", size=12)
medium_font = font.Font(family="systemfixed", size=24)
large_font = font.Font(family="systemfixed", size=36)


# Colors
white = "#ffffff"
grey = "#bdbdbd"
blue = '#0000ff'
purple = '#800080'
red = '#cc0000'
green = '#00ff00'
yellow = '#ffff00'
orange = '#ffa500'
black = "#000000"

# Screen
screen = tk.Canvas(root, width=screen_width, height=screen_height, bg=grey)
screen.place(relx=0, rely=0, relheight=1, relwidth=1)

# Title
title_label = tk.Label(screen, text="Sec + Acronyms", bg=grey, font=large_font)
title_label.place(relx=.0, rely=.0, relheight=.1, relwidth=1)

score = 0
attempts = 0
acro = ""
meaning_entry = None
description = ""

instructions = Image.open("instructions_1475x699.png")

# Convert the image to JPEG format
instructions = instructions.convert("RGB")
# Create the score label
score_label = tk.Label(screen, text="Score: 0 / 0", font=medium_font)
score_label.place(relx=.8, rely=.2, height=75, width=300)



############## SUPER GREAT LOOP FOR DEBUGGING THE POSITION OF THE ARRAYS ###############
#for acronym, meaning, detailed_explinations in zip(acronyms, meanings, detailed_explinations):
#    print(acronym + ": " + meaning + ":  " + detailed_explinations)

def start_game():
    global score
    global attempts
    global acro
    global meaning_entry
    global description
    meaning_entry = tk.Entry(screen, font=medium_font)
    meaning_entry.place(relx=.25, rely=.8, height=75, width=1000)
    # Generate random number for index selection
    random_num = randint(0, 145)
    # Access the tenth acronym and its corresponding meaning
    acro = acronyms[random_num]
    meaning = meanings[random_num]
    meaning = meaning.lower()
    description = detailed_explinations[random_num]

    acro_label = tk.Label(screen, text=acro, font=large_font)
    acro_label.place(relx=.25, rely=.2, height=600, width=1000)
    # Now make them all lowercase to check against user input with less errors


def check_answers():
    global acro
    global meaning_entry
    global score
    global attempts
    global score_label

    user_meaning = meaning_entry.get().lower()
    meaning = meanings[acronyms.index(acro)].lower()
    if user_meaning == meaning:
        print("Correct")
        correct_label = tk.Label(screen, text="Correct", font=medium_font)
        correct_label.place(relx=.0, rely=.1, height=100, relwidth=1)
        score += 1
    else:
        print("Something is wrong")
        incorrect_label = tk.Label(screen, text="Incorrect:   " + meaning, font=medium_font)
        incorrect_label.place(relx=.0, rely=.1, height=100, relwidth=1)
    attempts += 1

    # Update the score and attempts labels
    score_label.config(text="Score: " + str(score) + " / " + str(attempts))

###################### BUTTON FUNCTIONS #####################################
def try_again():
    ## Redraw over the correct or incorrect answer because I still dont know how to make it properly reset. This will do for now.
    start_game()
    correct_label = tk.Label(screen, text="", bg=grey, font=medium_font)
    correct_label.place(relx=.0, rely=.1, height=100, relwidth=1)
##### Easy enough here
def exit_program():
    exit()
# Opening a new window to display the instructons of the game
def instructions_function():
    # Create a new window
    window = tk.Toplevel(root)
    window.geometry("{}x{}".format(instructions.width, instructions.height))
    # Convert the image to a Tkinter PhotoImage object
    image = ImageTk.PhotoImage(instructions)
    # Create a Label widget to display the image
    label = tk.Label(window, image=image)
    label.pack()
    # Update the label reference to prevent it from being garbage collected
    label.image = image
    # Start the event loop for the new window
    window.mainloop()
#open a new window to explain the acrony does in great detail so we can learn some stuff ya mean?
def help():
    global description
    print(description)
    new_window = tk.Toplevel(root)
    # add widgets and functionality to the new window
    new_window.title('Help Window')
    new_window.geometry('600x600')
    label = tk.Label(new_window, text=description, font=medium_font, wraplength=500)
    label.place(relx=0, rely=0, relheight=1, relwidth=1)
    print("Help Window")
    new_window.mainloop()


########## Buttons ###########
try_again_btn = tk.Button(screen, text="NEXT", command=try_again)
try_again_btn.place(relx=.9, rely=.9, relheight=.1, relwidth=.1)
submit_btn = tk.Button(screen, text="SUBMIT", command=check_answers)
submit_btn.place(relx=.8, rely=.9, relheight=.1, relwidth=.1)
submit_btn = tk.Button(screen, text="EXIT", command=exit_program)
submit_btn.place(relx=.0, rely=.9, relheight=.1, relwidth=.1)
submit_btn = tk.Button(screen, text="HELP", command=help)
submit_btn.place(relx=.9, rely=.0, relheight=.1, relwidth=.1)
submit_btn = tk.Button(screen, text="INSTRUCTIONS", command=instructions_function)
submit_btn.place(relx=.0, rely=.0, relheight=.1, relwidth=.1)

start_game()
root.mainloop()
