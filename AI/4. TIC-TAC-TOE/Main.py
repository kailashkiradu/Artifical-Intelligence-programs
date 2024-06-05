import numpy as np
import random
from time import sleep

def create_board():
    return np.zeros((3, 3), dtype=int)

def possibilities(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

def random_place(board, player):
    selection = possibilities(board)
    if selection:
        current_loc = random.choice(selection)
        board[current_loc] = player
    return board

def check_win(board, player):
    return any(np.all(board == player, axis=0) |  # Check rows
               np.all(board == player, axis=1) |  # Check columns
               np.all(np.diag(board) == player) |  # Check main diagonal
               np.all(np.diag(np.fliplr(board)) == player))  # Check secondary diagonal

def evaluate(board):
    for player in [1, 2]:
        if check_win(board, player):
            return player
    return -1 if np.all(board != 0) else 0

def play_game():
    board, winner, counter = create_board(), 0, 1
    print(board)
    sleep(2)

    while winner == 0:
        for player in [1, 2]:
            board = random_place(board, player)
            print(f"Board after {counter} move")
            print(board)
            sleep(2)
            counter += 1
            winner = evaluate(board)
            if winner != 0:
                break

    return winner

# Driver Code
print("Winner is:", play_game())