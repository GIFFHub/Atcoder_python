

if __name__ == '__main__':
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    flg = 0
    for i in range(N):
        if flg:
            A[i] -= 1
            flg = 0
        else:
            flg = 1

    if X >= sum(A):
        print('Yes')
    else:
        print('No')
