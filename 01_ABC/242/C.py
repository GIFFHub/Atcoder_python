
N = int(input())
T = 998244353
ans = 0

table = [1]*9

for i in range(N-1):
    tmp = [0]*9
    for x in range(0, 9):
        if x == 0:
            tmp[0] = table[0]+table[1]
        elif x == 8:
            tmp[8] = table[7]+table[8]
        else:
            tmp[x] = table[x-1]+table[x]+table[x+1]
    table = tmp

    if table[4] > T:
        for x in range(0, 9):
            table[x] %= T

print(sum(table) % T)
