a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print(c if (b if a > b else a) > c else (b if a > b else a))