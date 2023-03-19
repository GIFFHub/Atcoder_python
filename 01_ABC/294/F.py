

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    Taka = []
    Aoki = []
    for _ in range(N):
        a, b = map(int, input().split())
        tmp = (100*a) / (a+b)
        Taka.append(tmp)
    for _ in range(M):
        a, b = map(int, input().split())
        tmp = (100 * a) / (a + b)
        Aoki.append(tmp)
    Taka.sort()
    Aoki.sort()

    print(Taka)
    print(Aoki)


