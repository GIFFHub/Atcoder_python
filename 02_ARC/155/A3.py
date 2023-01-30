

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    K %= 2*N
    S = input()
    if K > N:
        S2 = S[::-1] + S[::-1][-(K-N):]
    else:
        S2 = S[::-1][:K]
    SS1 = S + S2
    SS2 = S2 + S
    if SS1 == SS1[::-1] and SS2 == SS2[::-1]:
        print('Yes')
    else:
        print('No')