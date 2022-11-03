
def calc(a, b, cnt_L, cnt_A):
    global ans
    # 割り切れなくなった場合、終了
    if b%a > 0:
        return 0

    next_b = b//a
    # 最後までいった場合
    if cnt_L == N-1:
        if next_b == 1:
            return 1
        else:
            return 0
    # if next_b == 1:
    #     return 0

    cnt_L += 1

    rtn = 0
    for i in range(L[cnt_L]):
        rtn += calc(A[cnt_L][i], next_b, cnt_L, i)
    return rtn


if __name__ == '__main__':
    N, X = map(int, input().split())
    L = []
    A = [[] for _ in range(N)]
    for _ in range(N):
        tmp = list(map(int, input().split()))
        L.append(tmp[0])
        A[_] = tmp[1:]

    ans = 0

    for i in range(len(A[0])):
        ans += calc(A[0][i], X, 0, 0)

    print(ans)

