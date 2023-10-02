

if __name__ == '__main__':
    N, P, Q = map(int, input().split())
    D = list(map(int, input().split()))

    min_D = min(D)

    print(min(P, Q+min_D))