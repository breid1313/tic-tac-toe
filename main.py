import collections


from collections import Counter, defaultdict


board = [" " for _ in range(9)]
demo_board = [i for i in range(1, 10)]
positions = defaultdict(list)


def print_board(board: list[int]):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("\t_____|_____|_____")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("\t     |     |")
    print("\n")


def print_setup():
    print(
        "Welcome to tic tac toe. The object of the game is to mark spaces on the board such that three X's or three O's"
        "appear in a row. Player X always goes first. Provider integer selections for which space to mark"
        "according to the following diagram."
    )
    print_board(demo_board)


def mark_space(board: list[int], space: int, char: str):
    board[space] = char
    return board


def space_is_empty(board: list[int], space: int):
    return board[space] == " "


def is_win(player_positions: list):
    wins = [
        [0, 1, 2],  # row
        [3, 4, 5],  # row
        [6, 7, 8],  # row
        [0, 3, 6],  # col
        [1, 4, 7],  # col
        [2, 5, 8],  # col
        [0, 4, 8],  # diag
        [2, 4, 6],  # diag
    ]

    for w in wins:
        if Counter(w) - Counter(player_positions) == Counter():
            return True
    return False


def is_tie(positions: list):
    total = 0
    for v in positions.values():
        total += len(v)
    return total == 9


# game init
current_player = "X"
print_setup()

# game play
while True:
    print("Current state of the board...")
    print_board(board)
    try:
        space = (
            int(input(f"Player {current_player}, please select a space on the board: "))
            - 1
        )  # zero index the selection
    except ValueError:
        print("Space selection must be an integer 1-9. Try again.")
        continue

    if space < 0 or space > 8:
        print("Space selection must be an integer 1-9. Try again.")
        continue

    if not space_is_empty(board, space):
        print("Space {space} is currently occupied. Try again")
        continue

    # selection has been validated. put it on the board and update player position
    board = mark_space(board, space, current_player)
    positions[current_player].append(space)

    if is_win(positions[current_player]):
        print(f"Player {current_player} has won :)")
        break
    elif is_tie(positions):
        print(f"Draw :(")
        break

    current_player = "O" if current_player == "X" else "X"

# post game
print("Final state of the board")
print_board(board)
print("Thanks for playing!")

