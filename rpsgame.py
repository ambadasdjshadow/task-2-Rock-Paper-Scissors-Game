import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle the user's choice
def user_choice(choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = determine_winner(choice, computer_choice)
    result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

# Set up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x300")

# Instructions label
instructions = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
instructions.pack(pady=20)

# Buttons for user input
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: user_choice("Rock"))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=10, command=lambda: user_choice("Paper"))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: user_choice("Scissors"))
scissors_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()