
if __name__ == '__main__':
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = []
    ans = 0
    for _ in range(N):
        A = list(map(int, input().split()))
        tmp = C
        for a, b in zip(A, B):
            tmp += a*b
        if tmp > 0:
            ans += 1

    print(ans)

