

if __name__ == '__main__':
    N = int(input())
    T = []
    for _ in range(N):
        a, p, x = map(int, input().split())
        T.append((a, p, x))

    T.sort(key=lambda x: x[1])

    for t in T:
        a = t[0]
        p = t[1]
        x = t[2]
        if x > a:
            print(p)
            break
    else:
        print(-1)
