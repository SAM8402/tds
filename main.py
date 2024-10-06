import tkinter as tk
import random

# Initialize the main game window
window = tk.Tk()
window.title("Tic Tac Toe")

# Game state variables
player_turn = "X"
board = ["", "", "", "", "", "", "", "", ""]
game_active = True
single_player = False

# GUI Elements
buttons = []

# Function to check if the current player has won


def check_winner(player):
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

# Function to check if the board is full


def is_board_full():
    return "" not in board

# Function to update the game status and decide the winner or draw


def update_status():
    global game_active
    if check_winner("X"):
        label.config(text="Player X wins!")
        game_active = False
    elif check_winner("O"):
        label.config(text="Player O wins!")
        game_active = False
    elif is_board_full():
        label.config(text="It's a Draw!")
        game_active = False

# Function for computer's move in single player mode


def computer_move():
    global player_turn
    empty_cells = [i for i, value in enumerate(board) if value == ""]
    if empty_cells:
        choice = random.choice(empty_cells)
        board[choice] = "O"
        buttons[choice].config(text="O", state="disabled")
        player_turn = "X"
        update_status()

# Function to handle button clicks


def on_button_click(index):
    global player_turn
    if game_active and board[index] == "":
        board[index] = player_turn
        buttons[index].config(text=player_turn, state="disabled")
        update_status()

        # Toggle player turn
        if player_turn == "X":
            player_turn = "O"
            if single_player and game_active:
                computer_move()
        else:
            player_turn = "X"

# Function to reset the game


def reset_game():
    global player_turn, board, game_active
    player_turn = "X"
    board = ["", "", "", "", "", "", "", "", ""]
    game_active = True
    for button in buttons:
        button.config(text="", state="normal")
    label.config(text="Player X's turn")

# Function to choose mode and set single_player flag


def choose_mode(mode):
    global single_player
    if mode == "single":
        single_player = True
        label.config(text="Player X's turn (Playing against Computer)")
    else:
        single_player = False
        label.config(text="Player X's turn (Two Player Game)")
    # Enable the buttons after mode selection
    for button in buttons:
        button.config(state="normal")


# Creating the game board buttons and layout
frame = tk.Frame(window)
frame.pack()

for i in range(9):
    button = tk.Button(frame, text="", font=("Arial", 24), width=5, height=2,
                       command=lambda i=i: on_button_click(i), state="disabled")
    button.grid(row=i//3, column=i % 3)
    buttons.append(button)

# Mode selection buttons
mode_frame = tk.Frame(window)
mode_frame.pack()

single_player_button = tk.Button(mode_frame, text="Single Player", font=(
    "Arial", 16), command=lambda: choose_mode("single"))
single_player_button.grid(row=0, column=0, padx=10)

two_player_button = tk.Button(mode_frame, text="Two Player", font=(
    "Arial", 16), command=lambda: choose_mode("two"))
two_player_button.grid(row=0, column=1, padx=10)

# Reset button
reset_button = tk.Button(window, text="Reset Game",
                         font=("Arial", 16), command=reset_game)
reset_button.pack(pady=10)

# Label for game status
label = tk.Label(window, text="Choose Mode to Start", font=("Arial", 16))
label.pack(pady=10)

# Start the GUI main loop
window.mainloop()
