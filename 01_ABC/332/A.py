

if __name__ == '__main__':
    N, S, K = map(int, input().split())
    tmp = 0
    for i in range(N):
        p, q = map(int, input().split())
        tmp += p*q

    if tmp < S:
        tmp += K

    print(tmp)
