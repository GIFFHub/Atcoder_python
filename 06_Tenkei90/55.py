if __name__ == '__main__':
    N, P, Q = map(int, input().split())
    A = list(map(int, input().split()))
    for i in range(N):
        A[i] %= P

    ans = 0
    for a in range(N):
        for b in range(a+1, N):
            for c in range(b+1, N):
                for d in range(c+1, N):
                    for e in range(d+1, N):
                        ab = (A[a]*A[b]) % P
                        cd = (A[c]*A[d]) % P
                        abcd = (ab*cd) % P
                        abcde = (abcd*A[e]) % P
                        if abcde == Q:
                            ans += 1

    print(ans)




