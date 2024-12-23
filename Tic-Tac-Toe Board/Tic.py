# Create an empty board

board = [[" " for _ in range(3)] for _ in range(3)]

# Display the board
def print_board():
    for row in board:
        print("|".join(row))
        print("-" * 5)
