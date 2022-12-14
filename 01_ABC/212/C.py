

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()
    a_cnt = 0
    b_cnt = 0
    C = []
    while True:
        if A[a_cnt] >= B[b_cnt]:
            C.append((B[b_cnt], 'b'))
            b_cnt += 1
            if b_cnt >= M:
                if a_cnt < N:
                    for a in A[a_cnt:]:
                        C.append((a, 'a'))
                break
        else:
            C.append((A[a_cnt], 'a'))
            a_cnt += 1
            if a_cnt >= N:
                if b_cnt < M:
                    for b in B[b_cnt:]:
                        C.append((b, 'b'))
                break

    ans = 10**9+1
    for i in range(N+M-1):
        if C[i+1][1] != C[i][1]:
            ans = min(ans, C[i+1][0]-C[i][0])

    print(ans)


