import random
import tkinter as tk
from tkinter import messagebox

# Game choices
choices = {"Snake": 1, "Water": 0, "Gun": -1}
outcomes = {
   (1, 0): "You won! Snake drinks Water.",   
    (0, 1): "You lost! Snake drinks Water.",  
    (-1, 1): "You won! Gun kills Snake.",     
    (1, -1): "You lost! Gun kills Snake.",    
    (0, -1): "You won! Gun sinks in Water.",  
    (-1, 0): "You lost! Gun sinks in Water."  
}


def play_game(user_choice):
    computer_choice = random.choice(list(choices.keys()))
    user_value, computer_value = choices[user_choice], choices[computer_choice]
    
    if user_value == computer_value:
        result = "It's a tie!"
    else:
        result = outcomes.get((user_value, computer_value), "Something went wrong.")
    
    messagebox.showinfo("Game Result", f"You chose {user_choice}\nComputer chose {computer_choice}\n{result}")

# Create GUI window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("480x480")

# Heading Label
tk.Label(root, text="Choose Snake, Water, or Gun", font=("Arial", 12)).pack(pady=10)

# Buttons for choices
for choice in choices.keys():
    tk.Button(root, text=choice, font=("Arial", 10), command=lambda c=choice: play_game(c)).pack(pady=10)

# Run the application
root.mainloop()
