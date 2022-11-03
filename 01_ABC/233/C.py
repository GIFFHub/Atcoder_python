import itertools
import copy

if __name__ == '__main__':
    # input
    N, M = map(int, input().split())
    if M <= 1:
        print('Yes')
        exit()
    if N == 1:
        print('Yes')
        exit()

    A = []
    B = []
    C = []
    D = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a-1)
        B.append(b-1)
    for _ in range(M):
        c, d = map(int, input().split())
        C.append(c-1)
        D.append(d-1)

    # check which ball connect other ball
    Takahashi = [[] for _ in range(N)]
    Aoki = [[] for _ in range(N)]
    for i in range(M):
        for j in range(N):
            if A[i] == j:
                Takahashi[j].append(B[i])
            if B[i] == j:
                Takahashi[j].append(A[i])
            if C[i] == j:
                Aoki[j].append(D[i])
            if D[i] == j:
                Aoki[j].append(C[i])

    # 順列全探索
    all_pattern = list(itertools.permutations([_ for _ in range(N)]))

    for pattern in all_pattern:
        Aoki_copy = copy.deepcopy(Aoki)
        # 入れ替えパターン
        d = dict()
        for i in range(N):
            d[i] = pattern[i]

        for x in range(len(Aoki_copy)):
            for y in range(len(Aoki_copy[x])):
                Aoki_copy[x][y] = d[Aoki_copy[x][y]]

        # 各パターンについて、一致有無確認

        for i in range(N):
            Takahashi_set = set(Takahashi[d[i]])
            Aoki_set = set(Aoki_copy[i])

            if Takahashi_set == Aoki_set:
                pass
            else:
                break
        else:
            print('Yes')
            exit()

    print('No')



