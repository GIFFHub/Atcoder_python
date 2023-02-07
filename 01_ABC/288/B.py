
if __name__ == '__main__':
    N, K = map(int, input().split())
    S = []
    for _ in range(K):
        S.append(input())

    S.sort()


    for s in S:
        print(s)