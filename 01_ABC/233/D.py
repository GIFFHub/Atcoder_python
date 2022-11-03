

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    A_sum = []
    tmp = 0
    for i in range(N):
        tmp += A[i]
        A_sum.append(tmp)
    print(A_sum)


