import bisect

def getpos(p):

    pos1 = p[0]
    pos2 = p[1]
    pos3 = (X[pos1], Y[pos2])
    pos4 = (X[pos2], Y[pos1])

    return pos3, pos4



N = int(input())
X = []
Y = []
for i in range(N):
  x, y = map(int, input().split())
  X.append(x)
  Y.append(y)

pos = []
for i in range(N):
  pos.append((X[i], Y[i]))

#pos.sort(key=lambda x:x[1])
#pos.sort(key=lambda x:x[0])
pos = set(pos)


# 2点（右上、左下）の組み合わせを全探索
T = []
for i in range(N):
  for j in range(i+1, N):
    if X[i] != X[j] and Y[i] != Y[j]:
      T.append((i, j))


ans = 0
for t in T:
  target_pos = getpos(t)
  pos3 = target_pos[0]
  pos4 = target_pos[1]
  if pos3 in pos:
    if pos4 in pos:
      ans += 1

ans //= 2

print(ans)
