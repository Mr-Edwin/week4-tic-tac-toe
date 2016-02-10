def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

    # TO DO #################################################################
    # Write code in this function that prints the game board.               #
    # The code in this function should only print, the user should NOT      #
    # interact with this function in any way.                               #
    #                                                                       #
    # Hint: you can follow the same process that was done in the textbook.  #
    #########################################################################

def checkWinner(board, player):    
    print('Checking if ' + player + ' is a winner...')
    if board['top-L'] == board['top-M'] == board['top-R'] == player:
        return True
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] == player:
        return True
    elif board['low-L'] == board['low-M'] == board['low-R'] == player:
        return True
    elif board['top-L'] == board['mid-L'] == board['low-L'] == player:
        return True
    elif board['top-M'] == board['mid-M'] == board['low-M'] == player:
        return True
    elif board['top-R'] == board['mid-R'] == board['low-R'] == player:
        return True
    elif board['top-L'] == board['mid-M'] == board['low-R'] == player:
        return True
    elif board['top-R'] == board['mid-M'] == board['low-L'] == player:
        return True
    else:
        return False
    # TO DO #################################################################
    # Write code in this function that checks the tic-tac-toe board         #
    # to determine if the player stored in variable 'player' currently      #
    # has a winning position on the board.                                  #
    # This function should return True if the player specified in           #
    # variable 'player' has won. The function should return False           #
    # if the player in the variable 'player' has not won.                   #
    #########################################################################
    
def startGame(startingPlayer, board):
    # TO DO #################################################################
    # Add comments to each line in this function to describe what           #
    # is happening. You do not need to modify any of the Python code        #
    #########################################################################

                                                                #####################################################################
    turn = startingPlayer                                       # setting variable turn equal to variable startingPlayer            #
    for i in range(9):                                          # making a loop for when i is in the range 9 it will                #
        printBoard(board)                                       # run the function to print the board                               #
        print('Turn for ' + turn + '. Move on which space?')    # asks user x or o to play                                          #
        move = input()                                          # takes the input of the user and assings it to the variable move   #
        if move not in board:
            print('Please enter a valid move')
            i = i-1
            continue
        #if board[move] != None:
            #print('Please make another move')
            #continue
        board[move] = turn                                      #                                                                   #
        if( checkWinner(board, 'X') ):                          # runs the checkWinner function to check is X won                   #
            print('X wins!')                                    # if X wins prints X wins!                                          #
            break                                               # breaks form the loop                                              #
        elif ( checkWinner(board, 'O') ):                       # if X isn't the winner it then checks if O is the winner           #
            print('O wins!')                                    # if O wins it prints O wins!                                       #
            break                                               # breaks from the loop                                              #
                                                                #                                                                   #
        if turn == 'X':                                         # checks if the variable turn is equal to X if so                   #
            turn = 'O'                                          # it sets the turn variable to O                                    #
        else:                                                   # if the variable turn isn't equal to X                             #
            turn = 'X'                                          # then it sets the variable turn equal to X                         #
                                                                #                                                                   #
    printBoard(board)                                           #runs the function printBoard witht the variable board              #
                                                                #####################################################################
