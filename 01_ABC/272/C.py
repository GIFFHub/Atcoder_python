

N = int(input())
A = list(map(int, input().split()))
ans = -1

A.sort(reverse=True)

if A[0] % 2 == 0:
    if A[1] % 2 == 0:
        ans = A[0]+A[1]
        print(ans)
        exit()
    else:
        for i in range(2, N):
            if A[i] % 2 == 0:
                ans = max(ans, A[0]+A[i])
            else:
                ans = max(ans, A[1]+A[i])

elif A[0] % 2 == 1:
    if A[1] % 2 == 1:
        ans = A[0]+A[1]
        print(ans)
        exit()
    else:
        for i in range(2, N):
            if A[i] % 2 == 0:
                ans = max(ans, A[1]+A[i])
            else:
                ans = max(ans, A[0]+A[i])

print(ans)





