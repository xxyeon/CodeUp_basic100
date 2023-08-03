# int함수 base사용하기
n = input()
n = int(n, 16)

for i in range(1, 16):
    print('%X*%X=' %(n, i), end='')
    print('%X' %(n*i))