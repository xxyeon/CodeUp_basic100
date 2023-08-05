cols = 19
rows = 19
checkboard = [list(map(int, input().split())) for j in range(rows)] #2차원 배열 입력받기
n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    
    for j in range(19):
        if checkboard[x-1][j] == 0:
            checkboard[x-1][j] = 1
        else:
            checkboard[x-1][j] = 0
    
    for j in range(19):
        if checkboard[j][y-1] == 0:
            checkboard[j][y-1] = 1
        else:
            checkboard[j][y-1] = 0

for i in range(rows):
    for j in range(cols):
        print(checkboard[i][j], end = " ")
    print()
