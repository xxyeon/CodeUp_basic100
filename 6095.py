# 2차원 배열 선언시 곱셈으로 선언하지 말자
# lst[row][col]
n = int(input())

cols = 19
rows = 19
checkboard = [[0 for i in range(cols)] for j in range(rows)]

for i in range(n):
    x, y = map(int, input().split())
    checkboard[x-1][y-1] = 1

for i in range(rows):
    for j in range(cols):
        print(checkboard[i][j], end=' ')
    print()