
board = [['-','-','-'],['-','-','-'],['-','-','-']]

print("Start of Tic Tac Toe")
print("This is a two player game")

def printBoard(board):
    for row in board:
        for item in row:
            print(item,"", end="")
        print()


printBoard(board)

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

def addBoard(position, board):
    row = position[0]
    column = position[0]
    board[row][column] = 'x'
    print(printBoard(board))


while True:
    print("Please enter a number 1 through 9 or \"q\" to quit")
    userInput = input()

    if quit(userInput):
        break

    if not checkInput(userInput):
        print("Enter another number")
        continue


    userInput = int(userInput) -1
    position = positionBoard(userInput)

    if positionTaken(position, board):
        print('Please try again')
        continue
    else:
        addBoard(position, board)