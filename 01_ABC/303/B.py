if __name__ == '__main__':
    N, M = map(int, input().split())
    all_pair = N*(N-1)//2
    pairs = [set() for _ in range(N)]

    for i in range(M):
        A = list(map(int, input().split()))
        for j in range(N-1):
            pairs[A[j]-1].add(A[j+1]-1)
            pairs[A[j+1]-1].add(A[j]-1)

    tmp = 0
    for pair in pairs:
        tmp += len(pair)

    print(all_pair - tmp//2)


