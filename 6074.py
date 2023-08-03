# end 옵션 사용
n = ord(input())
a = ord('a')
while n >= a:
    print(chr(a), end=' ')
    a = a + 1
