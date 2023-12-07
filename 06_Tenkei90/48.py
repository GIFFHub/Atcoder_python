if __name__ == '__main__':
    N, K = map(int, input().split())
    T = []
    for _ in range(N):
        a, b = map(int, input().split())
        T.append(b)
        T.append(a-b)

    T.sort(reverse=True)
    ans = sum(T[:K])
    print(ans)