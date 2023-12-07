from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    for i in range(N):
        A[i] %= 46
        B[i] %= 46
        C[i] %= 46

    d_A = defaultdict(int)
    d_B = defaultdict(int)
    d_C = defaultdict(int)

    for a, b, c in zip(A, B, C):
        d_A[a] += 1
        d_B[b] += 1
        d_C[c] += 1

    A_set_list = list(set(A))
    B_set_list = list(set(B))
    C_set_list = list(set(C))

    ans = 0
    for a in A_set_list:
        for b in B_set_list:
            for c in C_set_list:
                if (a+b+c) % 46 == 0:
                    ans += d_A[a] * d_B[b] * d_C[c]

    print(ans)
