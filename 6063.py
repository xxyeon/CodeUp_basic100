# 삼항 연산자 [true] if [condition] else [false]
a, b = input().split()
a = int(a)
b = int(b)

print(a if a > b else b)