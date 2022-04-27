"""
Tic Tac Toe game for two players
Assignment W02 CSE210
Author Damian Hunt

"""

# Creating the game board (dictionary)
theBoard = {
    "7": " ", "8": " ", "9": " ",
    "4": " ", "5": " ", "6": " ",
    "1": " ", "2": " ", "3": " "
}


#Creates a list with all keys from theBoard.
board_keys = [key for key in theBoard]


def print_board(board):
    print(board['7'] + ' |' + board["8"] + ' |' + board["9"])
    print("--+--+--")
    print(board['4'] + ' |' + board["5"] + ' |' + board["6"])
    print("--+--+--")
    print(board['1'] + ' |' + board["2"] + ' |' + board["3"])


def main():
    turn = "X"
    count = 0
    # Using a while loop to ensure that wrong inputs are not counted for total turn count
    while count < 9:
        print_board(theBoard)
        print("It's your turn " + turn + ". Which place do you want to mark?")
        move = input()

        # Give the user the chance to exit the game
        if move.lower() == "exit":
            break
        # If user inputs anything other than a number, the game won't crash.
        # We show an error message and ask to try again.
        elif not move.isdigit():
            print("Invalid entry. Please enter a number from 1 to 9."
                  "\nTry again or type 'exit' to leave the game.")
            continue
        else:
            if theBoard[move] == " ":
                theBoard[move] = turn
                count += 1
            else:
                print("This is an invalid place. Try again!\nOr type 'exit' to leave the game.")
                continue

        #Checks inputs to see if there is a winner or game is a draw
        if count >= 5:
            if (theBoard["7"] == theBoard["8"] == theBoard["9"] != " ") or \
                    (theBoard["4"] == theBoard["5"] == theBoard["6"] != " ") or \
                    (theBoard["1"] == theBoard["2"] == theBoard["3"] != " ") or \
                    (theBoard["7"] == theBoard["4"] == theBoard["1"] != " ") or \
                    (theBoard["8"] == theBoard["5"] == theBoard["2"] != " ") or \
                    (theBoard["9"] == theBoard["6"] == theBoard["3"] != " ") or \
                    (theBoard["7"] == theBoard["5"] == theBoard["3"] != " ") or \
                    (theBoard["9"] == theBoard["5"] == theBoard["1"] != " "):
                print_board(theBoard)
                print("\nGame Over.\n")
                print("**** "+turn+" won. ****")
                break

        if count == 9:
            print("\nGame over.\n")
            print("It's a draw.\n")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"

    #Restart to play again
    restart = input("\nDo you want to play again?\nType Y for yes or anything else for no.")
    if restart.lower() == "y":
        for key in theBoard:
            theBoard[key] = " "
        main()


if __name__ == "__main__":
    main()