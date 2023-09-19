def isValidSudoku(board):
    r, c, sub = {}

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i+1 % 3 == 1 or j + 1 % 3 == 1:
                sub = {}
            if board[i][j] in r or board[i][j] in c or board[i][j] in sub:
                return False
        r[board[i][j]] = board[i][j]
        c[board[i][j]] = board[i][j]
        sub[board[i][j]] = board[i][j]

    return True


isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".",
              "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]])
