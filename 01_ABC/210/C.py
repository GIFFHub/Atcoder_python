from collections import defaultdict
from collections import deque


if __name__ == '__main__':
    N, K = map(int, input().split())
    C = list(map(int, input().split()))

    s = set()
    d = defaultdict(int)

    for c in C[:K]:
        d[c] += 1
        s.add(c)

    variety = len(s)
    ans = deque()
    ans.append(variety)
    for i in range(K, N):
        # 新しく検討する右のカード
        new = C[i]
        # 検討から外す左のカード
        old = C[i-K]

        # 新しいカードについて
        d[new] += 1
        if new not in s:
            s.add(new)
            variety += 1

        # 古いカードについて
        d[old] -= 1
        if d[old] == 0:
            s.remove(old)
            variety -= 1

        ans.append(variety)

    ans = list(ans)
    print(max(ans))



