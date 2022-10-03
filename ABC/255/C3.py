



if __name__ == '__main__':

    X, A, D, N = map(int, input().split())

    if D < 0:
        A = A+D*(N-1) # 最後尾を初期値にする
        D = -D

    if X <=A+D*(N-1):
        ans = abs(X-A+D*(N-1))

    elif X <= A:
        ans = abs(A-X)

    else:
        ans = min(abs(X-A)%D, D//2)

    print(ans)