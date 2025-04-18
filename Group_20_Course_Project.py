# Tic-Tac-Toe Game
"""
TODO: Input the team number and names of the team members here.
Team Number: 20
Team Member 1: Sirjana Chauhan
Team Member 2: Akshit Bhandari
"""

# Initialize the board
def initialize_board():
    """
    Initialize the board with empty spaces
    Parameters:
            None
    Returns:
            list: The board with empty spaces
    """
    return [' '] * 9


# Display the board
def display_board(board):
    """
    Display the board on the screen
    Parameters:
            board (list): The current board
    Returns:
            None
    """
    print("\n " + board[0] + " | " + board[1] + " | " + board[2] + " ")
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + " ")
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + " ")


# Check if the board is full
def is_board_full(board):
    """
    Check if the board is full (no empty spaces)
    Parameters:
            board (list): The current board
    Returns:
            bool: True if the board is full, False otherwise
    """
    # Checking that the board is full or not: if any of the cell of the board is empty then it will return false otherwise it will return true
    for each_cell in board:    # using for loop to get to each empty space in the board
        if each_cell == " ":   # using if condition to check that any cell has empty space or not
            return False

    return True



# Check for a win
def check_win(board, player):
    """
    Check if the player has won in any of the possible ways/conditions
    Parameters:
            board (list): The current board
            player (str): The player ("X" or "O")
    Returns:
            bool: True if the player has won, False otherwise
    """

    # Checking for rows, columns, and diagonals
    win_conditions = [[board[0], board[1], board[2]],     # checking for the uppermost row
                      [board[3], board[4], board[5]],     # checking for the middle row
                      [board[6], board[7], board[8]],     # checking for the lowermost row
                      [board[0], board[3], board[6]],     # checking for the left column
                      [board[1], board[4], board[7]],     # checking for the Middle column
                      [board[2], board[5], board[8]],     # checking for the Right column
                      [board[0], board[4], board[8]],     # checking for the Diagonal from top-left
                      [board[2], board[4], board[6]]]     # checking for the Diagonal from top-right



    # checking for the win conditions
    for condition in win_conditions:       # using for loop to get in the every element of list for win_conditions
        if condition.count(player) == 3:   # using if condition to see that count of the moves done by the player is equals to 3 and matches to the win_conditions or not
            return True                    # it will return true if condition is fulfilled otherwise returns false
        else:
            return False



# Get player input
def get_player_input(board, player):
    """
    Get the player's move and check if it is valid
    Parameters:
        board (list): The current board
        player (str): The player ("X" or "O")
    Returns:
        int: The position of the player's move
    """

    while True:
        print("\nThe current player is: " + player)
        move = input("Enter your move (1-9): ")
        # using nested if statement to check that the move is between 1 and 9 and also corresponds to an empty space
        if move.isdigit():                              # Checking that the move given by the player must be a digit
            move = int(move) - 1                        # subtracting 1 from move after every move by the player majorly to match the indexing
            if 0 <= move <= 8 and board[move] == ' ':   # checks that the move by the player must be between the range 0 to 8 according to the indexing of the board as well as the move by the player must have empty space
                return move                             # it will returns true if the above conditions will be true
            else:                                       # using else statement according to the if condition
                print("This is an invalid move! Please enter a number between 1 and 9 which must have an empty space.")
        else:                                           # using else statement according to the if condition
            print("This is an invalid move! The move must be a positive integer between 1 and 9.")


# Main game loop
def play_game():
    """
    The main game loop where the game is played until completion
    """
    while True:
        board = initialize_board()
        player = "X"

        while True:
            display_board(board)
            move = get_player_input(board, player=player)
            board[move] = player

            # Checking if any player has won the game or not
            if check_win(board, player):                 # Checking that any of the player has won the game or not
                display_board(board)                     # Checking the winning of the player according to the conditions given in check_win function by calling the display_board function
                print("Player", player, "wins!")         # Using the print function to give the output that which player has won the game
                break                                    # Breaking the loop if any of the player has won

            # TODO: Check if the board is full and it is a draw
            # Note: this portion has been completed for you
            if is_board_full(board):
                display_board(board)
                print("It's a draw!")
                break

            # Switching the players at every move if game is not over
            if player == "X":                             # Using if condition to switch the players
                player = "O"                              # If player "X" has turn then turn will goes to "O"
            else:                                         # Otherwise the player remains "X"
                player = "X"

        # prompting user if they want to start a new game, otherwise do not start a new game
        play_again = input("Do you want to play again? (Y/N): ").upper()
        if play_again != 'Y':
            break


# This is the main function. You do not need to make any changes here
def main():
    """
    Main function to run the game.
    """
    print("Welcome to Tic-Tac-Toe!")
    play_game()
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
