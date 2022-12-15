import heapq
from collections import deque

if __name__ == '__main__':
    Q = int(input())
    ans = []
    heapq.heapify(ans)

    bias = []
    d = dict()
    for i in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            if len(bias) == 0:
                bias.append(0)
            else:
                bias.append(bias[-1])
            heapq.heappush(ans, query[1]-bias[-1])
            if query[1]-bias[-1] in d:
                d[query[1]-bias[-1]].append(i)
            else:
                d[query[1]-bias[-1]] = deque([i])

        elif query[0] == 2:
            if len(bias) == 0:
                bias.append(0)
            else:
                bias.append(bias[-1]+query[1])
        else:
            ball = heapq.heappop(ans)
            cnt = d[ball].pop()
            print(bias[i-1]+ball)
            bias.append(bias[-1])


