N = int(input())
table = [True] * (2*N+1)
print(1)
table[0] = False

for _ in range(N):
    tmp = int(input())
    table[tmp-1] = False
    for i in range(1, 2*N+2):
        if table[i-1]:
            print(i)
            table[i-1] = False
            break

