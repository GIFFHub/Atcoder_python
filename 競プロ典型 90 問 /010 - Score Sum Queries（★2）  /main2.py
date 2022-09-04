# input()
N = int(input())

C = []
P = []

for _ in range(N):
    c, p = map(int, input().split())
    C.append(c)
    P.append(p)

Q = int(input())

L = []
R = []

for _ in range(Q):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

# 累積和計算

P_sum_1 = [0]*N
P_sum_2 = [0]*N

for i in range(N):
    P_sum_1[i] = P_sum_1[max(0, i-1)]
    P_sum_2[i] = P_sum_2[max(0, i-1)]

    if C[i] == 1:
        P_sum_1[i] += +P[i]
    elif C[i] == 2:
        P_sum_2[i] += +P[i]

for i in range(Q):
    if L[i] == 1:
        ans_1 = P_sum_1[R[i]-1]
        ans_2 = P_sum_2[R[i]-1]

    else:
        ans_1 = P_sum_1[R[i]-1] - P_sum_1[L[i]-2]
        ans_2 = P_sum_2[R[i]-1] - P_sum_2[L[i]-2]

    print(ans_1, ans_2)


# print('fin')
