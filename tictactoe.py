
board = [['-','-','-'],['-','-','-'],['-','-','-']]

user = True

print("Start of Tic Tac Toe")
print("This is a two player game")

def printBoard(board):
    for row in board:
        for item in row:
            print(item,"", end="")
        print()

def currentUser(user):
    if user:
        return 'x'
    else:
        return 'o'

def quit(userInput):
    if userInput == 'q':
        print('You have exited the game.')
        return True
    else:
        return False

def checkNumber(userInput):
    if not userInput.isnumeric():
        print("This is not a Number")
        return False
    else:
        return True

def checkInput(userInput):
    if checkNumber(userInput) == False:
        return False
    if validNumber(int(userInput)) == False:
        return False
    return True
    
def validNumber(userInput):

    if userInput > 9 or userInput < 1:
        print("Number out outside parameter")
        return False
    else:
        return True

def positionTaken(position, board):
    row = position[0]
    column = position[1]
    if board[row][column] != '-':
        print("This position is taken")
        return True
    else:
        return False
         
def positionBoard(userInput):
    row = int(userInput/3)
    column = userInput
    if column > 2:
        column = int(column % 3)
    return(row,column)

def addBoard(position, board, currentPlayer):
    row = position[0]
    column = position[0]
    board[row][column] = currentPlayer

def checkWin(user, board):
    if checkRow(user,board):
        return True
    if checkColumn(user,board):
        return True
    if checkDiags(user,board):
        return True
    return False

def checkRow(user,board):
    for lane in board:
        winRow = True
        for i in lane:
            if i != user:
                winRow = False
                break
        if winRow == True:
            return True
    return False

def checkColumn(user,board):
    for col in range(3):
        winColumn = True
        for row in col:
            if board[row][col] != user:
                winColumn = False
                break
        if winColumn == True:
            return True
    return False

def checkDiags(user,board):
    if board[0][0] == user and baord[1][1] == user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] and board[2][0] == user:
        return True
    else:
        return False

turn = 0

while turn < 9:

    currentPlayer = currentUser(user)
    printBoard(board)
    print("Please enter a number 1 through 9 or \"q\" to quit")
    userInput = input()

    if quit(userInput):
        break

    if not checkInput(userInput):
        print("Enter another number")
        continue


    userInput = int(userInput) - 1
    position = positionBoard(userInput)

    if positionTaken(position, board):
        print('Please try again')
        continue
    
    addBoard(position, board, currentPlayer)

    turn += 1
    if turn == 9:
        print("The game has tied!")
    user = not user