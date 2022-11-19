

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for _ in range(K):
        tmp = A.pop(0)
        A.append(0)

    print(*A)