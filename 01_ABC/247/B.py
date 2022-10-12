N = int(input())

S = []
T = []
all = set()
black_list = set()

for _ in range(N):
    s, t = input().split()
    if s in all:
        black_list.add(s)
    if t in all:
        black_list.add(t)
    all.add(s)
    all.add(t)
    S.append(s)
    T.append(t)

for i in range(N):
    if S[i] in black_list:
        if T[i] in black_list:
            print('No')
            break
else:
    print('Yes')


