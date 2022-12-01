import heapq
from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = []
    B = []
    T = list(range(1, N+1))
    d_a = dict() # 其々のAがどの値を制限しているか
    d_b = dict() # 其々のBがどの値によって制限されているか
    ans = deque()
    for _ in range(M):
        a, b = map(int, input().split())
        if a in d_a:
            d_a[a].add(b)
        else:
            d_a[a] = set()
            d_a[a].add(b)

        if b in d_b:
            d_b[b].add(a)
        else:
            d_b[b] = set()
            d_b[b].add(a)

        T[b-1] = 0



    T = set(T)
    T = list(T)
    heapq.heapify(T)
    heapq.heappop(T)

    while len(T) > 0:
        tmp = heapq.heappop(T) # 確定で置く値
        ans.append(tmp)
        if tmp in d_a: # 今回置く値が、Bの制限になっている場合
            for x in d_a[tmp]: # 制限されていた其々のBについて
                d_b[x].remove(tmp) # 各Bの制限のうち、今回置いたものの制限のみ消す

                if len(d_b[x]) == 0: # 制限がなくなった場合
                    heapq.heappush(T, x) # 置いていいリストに入れる

    if len(ans) == N:
        print(*ans)
    else:
        print(-1)



    '''
    方針
    ・置けるのは、前におくべき値がない値
    ・そのうち最小のもの
    ・よって、前におくべき値がない値を優先度付きキューで管理する
    ・最初は、1~NのうちBにない値が入る
    ・値が置かれることで、それがAに含まれるものだった場合、そのAに対応するBが解放される
    　とはかぎらない。他の値の制約になっている可能性がある
    ・
    ・
    ・
    ・
    '''


