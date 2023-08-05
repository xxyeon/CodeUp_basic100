maze = [list(map(int, input().split())) for j in range(10)]

i, j = 1, 1
maze[i][j] = 9
while maze[i][j] != 2:
    
    if maze[i][j+1] != 1:
        j += 1
        if maze[i][j] == 2:
            maze[i][j] = 9
            break
        maze[i][j] = 9

    elif maze[i+1][j] != 1:
        i += 1
        if maze[i][j] == 2:
            maze[i][j] = 9
            break
        maze[i][j] = 9
    else:
        break


for i in range(10):
    for j in range(10):
        print(maze[i][j], end = " ")
    print()