from collections import deque
from collections import defaultdict


if __name__ == '__main__':
    N, M = map(int, input().split())

    # 隣接辞書表現
    edges = dict()
    for _ in range(M):
        u, v = map(int, input().split())
        if u - 1 in edges:
            edges[u - 1].append(v - 1)
        else:
            edges[u - 1] = [v - 1]
        if v - 1 in edges:
            edges[v - 1].append(u - 1)
        else:
            edges[v - 1] = [u - 1]

    # dfs
    dfs_deque = deque()  # dfs用のdeque
    dist = dict()  # 視点からの移動距離

    groups = deque()  # 連結グループ
    ans = 0
    for p in range(N):
        white_points = set()
        white_points.add(p)
        black_points = set()
        if p in dist:
            continue
        else:
            dfs_deque.append(p)  # pから始める
            dist[p] = 0  # スタート地点の距離は0
            tmp_group = []

            # dfs
            while len(dfs_deque) > 0:
                # 現在点
                current_point = dfs_deque.popleft()
                tmp_group.append(current_point)
                # 現在から隣接する点について
                if current_point in edges:
                    for next_point in edges[current_point]:
                        # まだ行ったことなければ
                        if next_point not in dist:
                            dfs_deque.append(next_point)
                            dist[next_point] = dist[current_point]+1
                            if dist[next_point] % 2 == 1:
                                black_points.add(next_point)
                            else:
                                white_points.add(next_point)
                        # 行ったことがあれば
                        else:
                            # 既に2部グラフでない場合
                            if dist[next_point] % 2 != (dist[current_point] + 1) % 2:
                                print(0)
                                exit()
                # 単独点の場合
                else:
                    dist[current_point] = 0
                    break

            len_white = len(white_points)
            len_black = len(black_points)
            for point in tmp_group:
                if point in white_points:
                    ans += len_black + (N - (len_white + len_black))
                else:
                    ans += len_white + (N - (len_white + len_black))
                if point in edges:
                    ans -= len(edges[point])
    print(ans//2)

