

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    # マイナスの数が奇数かどうか
    flg = 0
    for a in A:
        if a < 0:
            flg = 1 - flg

    if flg == 0:
        ans = 0
        for a in A:
            ans += abs(a)
        print(ans)
        exit()

    ans = 0
    min_A = 10**9+1
    min_index = -1
    for i in range(N):
        if min_A > abs(A[i]):
            min_A = abs(A[i])
            min_index = i

    for i in range(N):
        if i == min_index:
            ans -= abs(A[i])
        else:
            ans += abs(A[i])

    print(ans)