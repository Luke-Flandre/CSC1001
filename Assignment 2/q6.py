def place(board, row, col):# Check if there is a queen in the same column or diagonal
    for i in range(row):
        if board[i] == col or abs(board[i]-col)==abs(i-row):#if there is one case that fail to meet the requirement, the function will return False
            return False
    return True#the other case meet the requirement

def printboard(board, row):#print the chess board
    if row == 8:#there are 8 rows in the board
        for i in range(8):#8 rows
            for j in range(8):#8 coloums
                if board[i] == j:#the coloum where the queen stands
                    print('| Q', end=' ')#print the block with the queen
                else:#there is no Queen
                    print('|  ', end=' ')#print the empty block
            print('|')#print the outer right of the board
        return True
    

    for col in range(8):
        if place(board, row, col):#if it meet the requirement in the rows
            board[row] = col#value the row
            if printboard(board, row + 1):#if there is one solution
                return True
    return False

# Create an 8x8 empty chessboard
board = [0] * 8


# Solve and display a solution
printboard(board, 0)