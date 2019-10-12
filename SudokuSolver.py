#Eren Ekren
#Yildiz Technical University
#4th Grade Student
import math

def findEmptyCell(board,coordinates): #Find an empty cell in given board, and writes coordinates on coordinates parameter
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                coordinates[0] = i
                coordinates[1] = j
                return True
    return False

def isAnyError(board,x,y,num): #Control the board if given number into empty cell makes an error
    for i in range(9):
        if board[x][i] == num:
            return True
        if board[i][y] == num:
            return True
    box_row = math.floor(x/3)
    box_row *= 3
    box_col = math.floor(y/3)
    box_col *= 3
    for i in range(box_row,box_row+3):
        for j in range(box_col,box_col+3):
            if board[i][j] == num:
                return True
    return False


def solveBoard(board): #Backtrack solver if no solution in all possibilities then it returns false
    coordinates = [-1,-1]
    isEmptyCell = findEmptyCell(board,coordinates)
    if not isEmptyCell:
        return True
    row = coordinates[0]
    col = coordinates[1]
    for i in range(1,10):
        error = isAnyError(board,row,col,i)
        if not error:
            board[row][col] = i
            solved = solveBoard(board)
            if solved:
                return True
            board[row][col] = 0
    return False

def readRow(row): #reads board row by row given txt file
    data = []
    returnVector = []
    data = row.split(',')    
    for value in data:
        returnVector.append(int(value))
    return returnVector
    


def main():    
    board = []
##    board = [[8,0,0,0,0,0,0,0,0],
##             [0,0,3,6,0,0,0,0,0],
##             [0,7,0,0,9,0,2,0,0],
##             [0,5,0,0,0,7,0,0,0],
##             [0,0,0,0,4,5,7,0,0],
##             [0,0,0,1,0,0,0,3,0],
##             [0,0,1,0,0,0,0,6,8],
##             [0,0,8,5,0,0,0,1,0],
##             [0,9,0,0,0,0,4,0,0]]

    print("Enter the directory of board:")
    path = str(input())
    fileNotFound = False
    try:
        f = open(path,'r')
        rows = f.readlines()
        f.close()
    except:
        print("Program terminated due to no file in given directory!")
        return
    
    for row in rows:
        board.append(readRow(row))
    isSolved = solveBoard(board)
    if isSolved:
        for i in range(9):
            print(board[i])
    else:
        print("This board is unsolvable")
    
        
    
    
    

main()
    
     
    
    
