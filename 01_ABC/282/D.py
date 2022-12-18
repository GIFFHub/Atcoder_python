from collections import deque
from collections import defaultdict
import sys
sys.setrecursionlimit(500000)

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
    uf = UnionFind(N+1)
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
                        uf.union(start, next_point)
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
            if not uf.same(dist[k], dist[l]):
                ans += 1
            elif dist[k] != dist[l]:
                ans += 1

    print(ans//2)





