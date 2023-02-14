

if __name__ == '__main__':
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    P.sort()
    print(sum(P[:K]))

