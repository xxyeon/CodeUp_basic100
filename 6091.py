a, b, c = map(int, input().split())
d = 1

while d%a != 0 or d%b != 0 or d%c != 0: # d가 입력한 주기에 모두 나누어 떨어지면 최소 공배수 성립
    d += 1
print(d)