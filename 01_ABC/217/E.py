from collections import deque
import heapq
if __name__ == '__main__':
    Q = int(input())
    A_deque = deque()
    A_heapq = []
    heapq.heapify(A_heapq)

    flg = 0
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            A_deque.append(query[1])
            heapq.heappush(A_heapq, query[1])
            flg = 1
        elif query[0] == 2:
            print(A_deque.popleft())
            flg = 2
        else:

            flg = 3
