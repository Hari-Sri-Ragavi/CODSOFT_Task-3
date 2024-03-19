import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return "It's a tie!", 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
        return "You win!", 'user'
    else:
        computer_score += 1
        return "Computer wins!", 'computer'

# Function to play the game
def play_game():
    user_choice = user_choice_var.get().lower()
    if user_choice not in ['rock', 'paper', 'scissors']:
        result_label.config(text="Invalid choice. Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    computer_choice_label.config(text="Computer's choice: " + computer_choice)

    result, winner = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)
    score_label.config(text=f"User: {user_score} | Computer: {computer_score}")

    if winner != 'tie':
        play_again_button.config(state=tk.NORMAL)

# Function to reset the game
def reset_game():
    result_label.config(text="")
    computer_choice_label.config(text="")
    user_choice_var.set("")
    play_again_button.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# User choice Entry
user_choice_label = tk.Label(root, text="Enter your choice: ")
user_choice_label.grid(row=0, column=0, padx=5, pady=5)
user_choice_var = tk.StringVar()
user_choice_entry = tk.Entry(root, textvariable=user_choice_var)
user_choice_entry.grid(row=0, column=1, padx=5, pady=5)

# Play Button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.grid(row=0, column=2, padx=5, pady=5)

# Computer choice Label
computer_choice_label = tk.Label(root, text="")
computer_choice_label.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Score Label
score_label = tk.Label(root, text="")
score_label.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

# Play Again Button
play_again_button = tk.Button(root, text="Play Again", command=reset_game, state=tk.DISABLED)
play_again_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

# Run the main event loop
root.mainloop()
