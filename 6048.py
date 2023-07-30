# print(a<b) boolean 값이 출력된다.조건문을 사용해도 되고 boolean 값을 이용해서 출력해도 된다.
a, b = input().split()

a, b = int(a), int(b)
if(a < b):
    print("True")
else:
    print("False")