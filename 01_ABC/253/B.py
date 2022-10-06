
H, W = map(int, input().split())

index = []

for i in range(H):
    if len(index) > 1:
        break

    s = input()
    s_cnt = s.count('o')
    if s_cnt == 0:
        pass
    elif s_cnt == 1:
        index.append((i, s.find('o')))
    else:
        index.append((i, s.find('o')))
        index.append((i, s.rfind('o')))

print(abs(index[0][0]-index[1][0])+abs(index[0][1]-index[1][1]))

