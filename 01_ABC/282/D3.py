
from collections import deque
from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


if __name__ == '__main__':
    N, M = map(int, input().split())
    uf = UnionFind(N)

    # 隣接辞書表現
    edges = dict()
    for _ in range(M):
        u, v = map(int, input().split())
        if u-1 in edges:
            edges[u-1].append(v-1)
        else:
            edges[u-1] = [v-1]
        if v-1 in edges:
            edges[v-1].append(u-1)
        else:
            edges[v-1] = [u-1]

    # dfs
    dfs_deque = deque()  # dfs用のdeque
    dist = dict()  # 視点からの移動距離

    groups = deque() # 連結グループ
    ans = 0
    for p in range(N):
        if p in dist:
            continue
        else:
            dfs_deque.append(p)  # pから始める
            dist[p] = 0  # スタート地点の距離は0
            tmp_group = []

            white_points = [p]
            black_points = []
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
                            uf.union(current_point, next_point)
                            dfs_deque.append(next_point)
                            dist[next_point] = dist[current_point]+1
                            if dist[next_point] % 2 == 1:
                                black_points.append(next_point)
                            else:
                                white_points.append(next_point)
                        # 行ったことがあれば
                        else:
                            # 既に2部グラフでない場合
                            if dist[next_point] % 2 != (dist[current_point]+1) % 2:
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
                    ans += len_black - len(edges[point]) + (N-(len_white+len_black))

            groups.append(tmp_group)


    '''
    ans = 0
    tmp = 0 # 非連結用
    
    for root in uf.all_group_members():
        points = uf.members(root) # 連結している点について
        print(points)
        size = uf.size(root)
        
        
        for i in range(size):
            for j in range(i+1, size):
                if points[j] not in edges[points[i]]:
                    if dist[points[i]] % 2 != dist[points[j]] % 2:
                        ans += 1
            # 連結していない点への辺を追加する。
            # 後で重複分を//2するために、別に変数を管理
            tmp += N-size
    '''
    '''
    for group in groups:
        len_group = len(group)
        for i in range(len_group):
            for j in range(i+1, len_group):
                if group[j] not in edges[group[i]]:
                    if dist[group[i]] % 2 != dist[group[j]] % 2:
                        ans += 1
            # 連結していない点への辺を追加する。
            # 後で重複分を//2するために、別に変数を管理
            tmp += N - len_group
    print(ans+tmp//2)
    print(white_points)
    print(black_points)
    #print(group)
    '''














