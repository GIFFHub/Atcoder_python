
N = int(input())
A = sorted(list(map(int, input().split())))
A_set = set(A)


len_A = N
tmp = 0
for i in range(1, N+1):
    if i not in A_set:
        if len_A >= tmp+2:
            len_A -= 2
        else:
            print(i-1)
            exit()
    else:
        if len_A < tmp+1:
            print(i-1)
            exit()
        else:
            tmp += 1

print(i)






