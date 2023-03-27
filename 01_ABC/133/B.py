

if __name__ == '__main__':
    N, D = map(int, input().split())
    X = []
    for _ in range(N):
        X.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            dist = 0
            for y, z in zip(X[i], X[j]):
                dist += (y-z)**2
            for t in range(1000):
                if t**2 == dist:
                    ans += 1
    print(ans)


