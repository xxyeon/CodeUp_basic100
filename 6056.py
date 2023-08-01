# a xor b 가 (a and (not b)) or ((not a) and b)와 동일하다
a, b = input().split()
a = bool(int(a))
b = bool(int(b))
print((a and (not b)) or ((not a) and b))