from collections import deque
import sys
sys.setrecursionlimit(5000000)


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    B = []
    T = [deque() for _ in range(N)]
    C = 10**9+7
    for _ in range(M):
        a, b = map(int, input().split())
        T[a-1].append(b-1)
        T[b-1].append(a-1)

    d = deque()
    d.append(0)

    dist = dict()
    dist[0] = 0
    cnt = dict()
    cnt[0] = 1
    while True:
        if len(d) > 0:
            current_city = d.popleft()
            for next_city in T[current_city]:
                # 行ったことないなら
                if next_city not in dist:
                    dist[next_city] = dist[current_city]+1
                    d.append(next_city)
                    cnt[next_city] = cnt[current_city]
                # 行ったことあるなら
                else:
                    # 今まで行ったことある最短ルートと同じコストなら
                    if dist[next_city] == dist[current_city]+1:
                        # パターン（cnt)を追加
                        cnt[next_city] += cnt[current_city]
        else:
            break

    if N-1 not in dist:
        print(0)
    else:
        print(cnt[N-1]%C)


