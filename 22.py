def is_safe(x, y, board, n):
    return 0 <= x < n and 0 <= y < n and board[x][y] == -1


def knight_tour(n):
    board = [[-1]*n for _ in range(n)]
    moves_x = [2,1,-1,-2,-2,-1,1,2]
    moves_y = [1,2,2,1,-1,-2,-2,-1]

    board[0][0] = 0

    def solve(x, y, move):
        if move == n*n:
            return True

        for i in range(8):
            nx, ny = x + moves_x[i], y + moves_y[i]
            if is_safe(nx, ny, board, n):
                board[nx][ny] = move
                if solve(nx, ny, move+1):
                    return True
                board[nx][ny] = -1
        return False

    if solve(0, 0, 1):
        for row in board:
            print(row)
    else:
        print("No solution")


knight_tour(5)
