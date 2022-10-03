
N, M = map(int, input().split())

for i in range(N,0,-1):
    for j in range(9,0,-1):
        num = j*int('1'*i)
        #num = int(str(j)*i)
        if num % M == 0:
            print(num)
            exit()

print(-1)

