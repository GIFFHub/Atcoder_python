from collections import deque
import heapq

Q = int(input())

A_d = deque()
A_h = []
heapq.heapify(A_h)

for i in range(Q):
  query = list(map(int, input().split()))

  if query[0] == 1:
    A_d.append(query[1])

  elif query[0] == 2:
    if len(A_h) == 0:
      print(A_d.popleft())
    else:
      print(heapq.heappop(A_h))

  else:
    for x in A_d:
      heapq.heappush(A_h, x)
    A_d = deque()

  #print('A_d:', A_d)
  #print('A_h:', A_h)

'''
考察
・ヒープとデックを用意する
・①のとき、デックに追加する
・③のとき、デックをヒープに入れる
・②のとき、ヒープの最小値を取り出す。ヒープが空のときっはデックの先頭を取り出す


'''