

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))

    Q = [None]*N

    for i, p in enumerate(P):
        Q[p-1] = i+1

    print(*Q)
