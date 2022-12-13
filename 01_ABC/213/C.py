

if __name__ == '__main__':
    H, W, N = map(int, input().split())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    A_ans = sorted(list(set(A)))
    B_ans = sorted(list(set(B)))

    d_a = dict()
    d_b = dict()
    for i, a in enumerate(A_ans):
        d_a[a] = i+1

    for i, b in enumerate(B_ans):
        d_b[b] = i+1

    for i in range(N):
        print(d_a[A[i]], d_b[B[i]])

