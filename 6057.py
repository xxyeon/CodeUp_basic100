# == 연산자를 사용해서 풀이할 수 있다
a, b = input().split()
a = bool(int(a))
b = bool(int(b))

print(not((a and (not b)) or ((not a) and b)))
# 모범답안
# print(a == b)