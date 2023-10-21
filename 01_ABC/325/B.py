

if __name__ == '__main__':
    N = int(input())
    T = [0] * 24
    for _ in range(N):
        w, x = map(int, input().split())

        for t in range(9, 18):
            T[(x+t) % 24] += w

    print(max(T))







