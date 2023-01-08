

if __name__ == '__main__':
    N = int(input())
    S = []
    for _ in range(N):
        S.append(input())

    S.reverse()

    for s in S:
        print(s)