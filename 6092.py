n = int(input())
lst = list(map(int,input().split()))
print_lst = [0] * 23

for j in range(n):
    for i in range(24):
        if(lst[j] == i+1):
            print_lst[i] += 1

print(*print_lst)