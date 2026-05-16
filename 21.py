def solve_maze(maze, x, y, solution):
    n = len(maze)

    if x == n-1 and y == n-1:
        solution[x][y] = 1
        return True

    if 0 <= x < n and 0 <= y < n and maze[x][y] == 1:
        solution[x][y] = 1

        if solve_maze(maze, x+1, y, solution):
            return True
        if solve_maze(maze, x, y+1, solution):
            return True

        solution[x][y] = 0
    return False


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solution = [[0]*4 for _ in range(4)]

if solve_maze(maze, 0, 0, solution):
    for row in solution:
        print(row)
else:
    print("No path found")
