import heapq

if __name__ == '__main__':

    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    q = [0]
    s = set() # なりえる合計値
    for _ in range(K):
        x = heapq.heappop(q)
        for a in A:
            # なりえる合計値+A[j]もなりえる合計値
            y = x + a
            if y not in s:
                s.add(y)
                # すでに入れてない場合のみ、qに追加
                heapq.heappush(q, y)
    print(heapq.heappop(q))