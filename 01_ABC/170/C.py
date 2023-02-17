import bisect

if __name__ == '__main__':
    X, N = map(int, input().split())
    P = list(map(int, input().split()))

    P_set = set(P)

    if X not in P_set:
        ans = X
    else:
        bias = 1
        while True:
            if X-bias not in P_set:
                ans = X-bias
                break
            elif X+bias not in P_set:d
                ans = X+bias
                break
            else:
                bias += 1

    print(ans)








