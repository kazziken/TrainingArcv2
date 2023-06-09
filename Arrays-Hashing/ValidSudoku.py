'''
Determine if a 9 x 9 Sudoku board is valid. 

Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A Sudoku board (partially filled) could be valid but is not necessarily solvable.

example 

[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

first column has 2 8s and has 2 8's in the 3x3 sub-box. making it False 
'''


'''
Explanation:

Create a set of cols, rows, and a set for the subset of 3x3 squares
sets need to be added using .add()

then we check r,c's in range(9) because thats how many indices are in a sudoku board(9x9)
if the board[r][c] is empty or '.' continue, if they're already in the sets
return False

hashset for squares is a {[r//3, c//3] : board[r][c]} since every 3x3 subsquare can only have
one unique element from 1-9

'''
import collections

def valid_sudoku(self, board):
    cols = collections.defaultdict(set)
    rows = collections.defaultdict(set)
    squares = collections.defaultdict(set) #key = ( row//3, col//3 )

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue 
            #if we already seen the value already within this current row
            if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]
                ):
                return False
            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r//3, c//3)].add(board[r][c])
    return True

