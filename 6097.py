h, w = map(int, input().split())
n = int(input())

checkboard = [[0 for i in range(w)] for j in range(h)]

for i in range(n):
    l, d, x, y = map(int, input().split())

    if d == 0 :
        for j in range(l):
            checkboard[x-1][y-1+j] = 1
    else:
        for j in range(l):
            checkboard[x-1+j][y-1] = 1

for i in range(h):
    for j in range(w):
        print(checkboard[i][j], end = " ")
    print()