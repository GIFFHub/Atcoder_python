from collections import deque


class Node(object):
    def __init__(self):
        self.parent = -1
        self.children = []


if __name__ == '__main__':
    N, Q = map(int, input().split())
    edges = dict()
    for _ in range(N-1):
        a, b = map(int, input().split())
        if a in edges:
            edges[a].append(b)
        else:
            edges[a] = [b]
        if b in edges:
            edges[b].append(a)
        else:
            edges[b] = [a]

    print(edges)

    #dfs

    # 初期設定
    dfs_deque = deque()
    dist = dict()

    # スタート地点設定
    dfs_deque.append(1)
    dist[1] = 0
    tree = dict()
    tree[1] = Node()
    while len(dfs_deque) > 0:
        current_point = dfs_deque.popleft()
        next_points = edges[current_point]
        tree[current_point].children = next_points.copy()
        for next_point in next_points:
            if next_point in dist:
                pass
            else:
                tree[next_point] = Node()
                tree[next_point].parent = current_point
                dfs_deque.append(next_point)
                dist[next_point] = dist[current_point]+1

    print(tree)








