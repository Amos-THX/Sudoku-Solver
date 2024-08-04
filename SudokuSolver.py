from math import floor
#Sudoku solver

class SudokuSolution():

    def solveSudokuBoard(self, board):

        #Create a function that checks whether a number is eligible in the box and column
        def check_box_pos(row,col,number):
            row,col = int(row), int(col)
            for i in range(9): #loop across board
                # If row or column contains number you want to slot in, return False
                if board[row][i] == number:
                    return False
                if board[i][col] == number:
                    return False

            #if box contains number you want to slot in, return False. else number is eligible to be placed in box, return True
            box = ( floor(row/3),floor(col/3) )

            box_positions = [(x,y) for x in range(box[0]*3, (box[0]+1)*3 ) for y in range(box[1]*3, (box[1]+1)*3 ) ]

            #If any position of box already has number, return False
            for x,y in box_positions:
                if board[x][y] == number:
                    return False
            return True


        #Create a solver which loops through all possible combinations
        # Once the first possible solution reaches a dead end, reverse back to next solution

        def solver(row,col): #loop through every single row and col.
            if row == 9:
                return True # i.e. return this board as correct result
            if col ==9:
                return solver(row+1,0) # go to next row.

            if board[row][col] != '.': #If board already has number, just skip
                return solver(row,col+1)

            else:

                for i in range(1,10): #loop through actual numbers 1-9 to check validity
                    if check_box_pos(row,col,str(i)): #Check validity of number in box
                        board[row][col] = str(i)

                        if solver(row,col+1): #if next box and forward is correct
                            return True
                        else: #When function returns to current row because it isnt correct, change
                            board[row][col] = "."

                return False

        return solver(0,0)



board = [[".",".",".","8",".",".",".","9","7"],[".","6",".","3",".",".",".",".","5"],[".",".",".",".",".",".",".","2","."],[".",".",".","6",".",".","4",".","."],["7",".",".",".","2",".",".",".","."],["9",".",".",".",".",".",".",".","."],[".","4",".",".",".","7",".",".","."],[".",".","3",".",".",".","8",".","."],[".",".",".",".","9",".",".",".","."]]


sol = SudokuSolution()
sol.solveSudokuBoard(board)

# To print output in a nicer format
for board_row in board:
    print(board_row)

