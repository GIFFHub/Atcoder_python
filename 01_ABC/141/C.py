

if __name__ == '__main__':
    N, K, Q = map(int, input().split())
    P = [0]*N
    for _ in range(Q):
        x = int(input())
        P[x-1] += 1

    for p in P:
        if p + K - Q > 0:
            print('Yes')
        else:
            print('No')

