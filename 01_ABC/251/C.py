def judge(index):
    if


if __name__ == '__main__':
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s, t = map(int, input().split())
        S.append(s)
        T.append(t)

    T.index(max(T))
