import tkinter as tk
from tkinter import messagebox

# Create an empty board
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'
moves_left = 9


# Function to check for a win
def check_win(player):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


# Function to handle button click
def handle_click(row, col, button):
    global current_player, moves_left

    # Check if the cell is empty
    if button["text"] == " ":
        # Make the move
        button["text"] = current_player
        board[row][col] = current_player
        moves_left -= 1

        # Check for a win
        if check_win(current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game()
        # Check for a draw
        elif moves_left == 0:
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game()
        else:
            # Switch players
            current_player = 'O' if current_player == 'X' else 'X'


# Function to reset the game
def reset_game():
    global current_player, moves_left
    current_player = 'X'
    moves_left = 9
    for row in range(3):
        for col in range(3):
            buttons[row][col]["text"] = " "
            board[row][col] = " "


# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")

# Create buttons
buttons = []
for row in range(3):
    row_buttons = []
    for col in range(3):
        button = tk.Button(window, text=" ", font=("Helvetica", 24), width=4, height=2)
        button.grid(row=row, column=col, padx=5, pady=5)
        button.config(command=lambda r=row, c=col, b=button: handle_click(r, c, b))  # Corrected lambda function
        row_buttons.append(button)
    buttons.append(row_buttons)

# Start the main event loop
window.mainloop()