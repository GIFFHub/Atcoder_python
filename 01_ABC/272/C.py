

N = int(input())
A = list(map(int, input().split()))

g_cnt = 0
k_cnt = 0
for i in range(N):
    if A[i] % 2 == 0:
        g_cnt += 1
    else:
        k_cnt += 1

ans1 = -1
ans2 = -1
ans3 = -1
ans4 = -1
ans5 = -1
ans6 = -1

if g_cnt < 2 and k_cnt < 2:
    print(-1)
else:
    A.sort(reverse=True)

    if A[0] % 2 == 0:
        if A[1] % 2 == 0:
            ans1 = A[0]+A[1]
            print(ans1)
            exit()
        else:
            for i in range(2, N):
                if A[i] % 2 == 0:
                    ans2 = max(ans2, A[0]+A[i])
                else:
                    ans3 = max(ans3, A[1]+A[i])

    elif A[0] % 2 == 1:
        if A[1] % 2 == 1:
            ans4 = A[0]+A[1]
            print(ans4)
            exit()
        else:
            for i in range(2, N):
                if A[i] % 2 == 0:
                    ans5 = max(ans5, A[1]+A[i])
                else:
                    ans6 = max(ans6, A[0]+A[i])

    print(max(ans1, ans2, ans3, ans4, ans5, ans6))





