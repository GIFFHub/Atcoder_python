from collections import deque


class Node(object):
    def __init__(self):
        self.parent = -1
        self.children = []
        self.depth = 0


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
        for next_point in next_points:
            if next_point in dist:
                pass
            else:
                tree[next_point] = Node()
                tree[current_point].children.append(next_point)
                tree[next_point].parent = current_point
                tree[next_point].depth = tree[current_point].depth+1
                dfs_deque.append(next_point)
                dist[next_point] = dist[current_point]+1

    for _ in range(Q):
        c, d = map(int, input().split())
        if tree[c].depth % 2 == tree[d].depth % 2:
            print('Town')
        else:
            print('Road')








