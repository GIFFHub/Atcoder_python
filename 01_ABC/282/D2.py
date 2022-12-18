from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(5000000)


class UnionFind():
    """
    Union Find木クラス

    Attributes
    --------------------
    n : int
        要素数
    root : list
        木の要素数
        0未満であればそのノードが根であり、添字の値が要素数
    rank : list
        木の深さ
    """

    def __init__(self, n):
        """
        Parameters
        ---------------------
        n : int
            要素数
        """
        self.n = n
        self.root = [-1]*(n+1)
        self.rank = [0]*(n+1)

    def find(self, x):
        """
        ノードxの根を見つける

        Parameters
        ---------------------
        x : int
            見つけるノード

        Returns
        ---------------------
        root : int
            根のノード
        """
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]

    def unite(self, x, y):
        """
        木の併合

        Parameters
        ---------------------
        x : int
            併合したノード
        y : int
            併合したノード
        """
        x = self.find(x)
        y = self.find(y)

        if(x == y):
            return
        elif(self.rank[x] > self.rank[y]):
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rank[x] == self.rank[y]):
                self.rank[y] += 1

    def same(self, x, y):
        """
        同じグループに属するか判定

        Parameters
        ---------------------
        x : int
            判定したノード
        y : int
            判定したノード

        Returns
        ---------------------
        ans : bool
            同じグループに属しているか
        """
        return self.find(x) == self.find(y)

    def size(self, x):
        """
        木のサイズを計算

        Parameters
        ---------------------
        x : int
            計算したい木のノード

        Returns
        ---------------------
        size : int
            木のサイズ
        """
        return -self.root[self.find(x)]

    def roots(self):
        """
        根のノードを取得

        Returns
        ---------------------
        roots : list
            根のノード
        """
        return [i for i, x in enumerate(self.root) if x < 0]

    def group_size(self):
        """
        グループ数を取得

        Returns
        ---------------------
        size : int
            グループ数
        """
        return len(self.roots())

    def group_members(self):
        """
        全てのグループごとのノードを取得

        Returns
        ---------------------
        group_members : defaultdict
            根をキーとしたノードのリスト
        """
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members


if __name__ == '__main__':
    N, M = map(int, input().split())
    T = dict()
    s_all = set(list(range(1, N+1)))
    d_s = dict()
    for i in range(1, N+1):
        d_s[i] = s_all.copy()
        d_s[i].discard(i)

    for _ in range(M):
        u, v = map(int, input().split())
        if u in T:
            T[u].append(v)
        else:
            T[u] = [v]
        if v in T:
            T[v].append(u)
        else:
            T[v] = [u]
        d_s[u].discard(v)
        d_s[v].discard(u)


    d = deque()
    dist = dict()
    ans = 0
    while True:
        start = list(s_all)[0]
        s_all = set(s_all)
        s_all.discard(start)
        d.append(start)
        dist[start] = 0

        while True:
            if len(d) > 0:
                current_point = d.popleft()
                for next_point in T[current_point]:
                    # 行ったことないなら
                    if next_point not in dist:
                        s_all.discard(next_point)
                        #dist[next_point] = dist[current_point]+1
                        dist[next_point] = (dist[current_point]+1)%2

                        d.append(next_point)
                    # 行ったことあるなら
                    else:
                        if dist[next_point] != (dist[current_point]+1)%2:
                            print(0)
                            exit()

            else:
                break
        if len(s_all) == 0:
            break


    '''
    print(T)
    print(dist)

    print(s_black)
    print(s_white)
    print(d_s)
    '''


    ans = 0
    for k in d_s:
        for l in d_s[k]:
            if dist[k] != dist[l]:
                ans += 1

    print(ans//2)





