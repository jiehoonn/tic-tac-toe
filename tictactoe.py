import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


# Printing the game board
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])


#take player input
def playerInput(board):
    while True:
        inp = int(input("Enter a number 1-9: "))
        if inp >= 1 and inp <= 9:
            if board[inp-1] == "-":
                board[inp-1] = currentPlayer
                break
            else:
                print("Oops, that spot is already taken. Try again.")
        else:
            print("Invalid input. Please enter a number between 1 and 9.")


#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board [1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board [8] and board[6] != "-":
        winner = board [6]
        return True
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board [6] and board [2] != "-":
        winner = board[2]
        return True
    
def checkTie(board):
    global gameRunning
    if "-" not in board and not (checkHorizontal(board) or checkRow(board) or checkDiagonal(board)):
        printBoard(board)
        print("It's a tie!")
        gameRunning = False

def checkWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        printBoard(board)
        print(f"The winner is {winner}")
        gameRunning = False
        
 
# Switch the player

def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# Computer
def computer(board):
    while currentPlayer == "O":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()


# Check for win or tie again

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    if gameRunning:  # Only proceed if the game is still running
        checkTie(board)
        switchPlayer()
        computer(board)
        checkWin()
        if gameRunning:  # Check again after the computer's turn
            checkTie(board)