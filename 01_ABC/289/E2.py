from collections import defaultdict, deque

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        C = list(map(int, input().split()))
        edge = [[] for _ in range(N)]
        for _ in range(M):
            u, v = map(int, input().split())
            edge[u-1].append(v-1)
            edge[v-1].append(u-1)

        todo = deque()
        todo.append((0, 0, N-1))
        INF = 10**9
        seen = [[INF]*N for _ in range(N)]
        seen[0][N-1] = 0

        while todo:
            d, x, y = todo.pop()

            # 現在地(x, y)から行ける全ての場所へ
            for tox in edge[x]:
                for toy in edge[y]:
                    # 行ったことなく、かつ異なる色なら
                    if seen[tox][toy] == INF and C[tox] != C[toy]:
                        seen[tox][toy] = d+1
                        todo.appendleft((d+1, tox, toy))
        ans = seen[N-1][0]
        if ans == INF:
            ans = -1

        print(ans)

