def isValidSudoku(board):
    r = {}
    c = {}
    for i in range(9):
        c[i] = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i % 3 == 0:
                sub1 = sub2 = sub3 = {}
            if board[i][j] in r or board[i][j] in c[j] or (j < 3 and board[i][j] in sub1) or (j < 6 and board[i][j] in sub2) or (j < 3 and board[i][j] in sub3):
                return False

            if board[i][j] != ".":
                r[board[i][j]] = c[j][board[i][j]] = board[i][j]
        r = {}

    return True


# Path: 37. Sudoku Solver\index.py
# Compare this function from 36. Valid Sudoku\index.py:
print(isValidSudoku([[".", ".", ".", ".", "5", ".", ".", "1", "."], [".", "4", ".", "3", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "3", ".", ".", "1"], ["8", ".", ".", ".", ".", ".", ".", "2", "."], [".", ".", "2",
              ".", "7", ".", ".", ".", "."], [".", "1", "5", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", "2", ".", ".", "."], [".", "2", ".", "9", ".", ".", ".", ".", "."], [".", ".", "4", ".", ".", ".", ".", ".", "."]]))