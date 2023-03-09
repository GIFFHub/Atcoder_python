

if __name__ == '__main__':
    N, K, M = map(int, input().split())
    A = list(map(int, input().split()))

    sum_A = sum(A)
    x = M*N - sum_A

    if x > K:
        print(-1)
    else:
        print(max(0,x))
