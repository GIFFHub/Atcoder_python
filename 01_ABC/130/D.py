import bisect
if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A_cur = [0]
    tmp = 0
    for a in A:
        tmp += a
        A_cur.append(tmp)
    ans = 0
    for i in range(N):
        index = bisect.bisect_left(A_cur, K + A_cur[i])
        ans += (N+1) - index
    print(ans)


