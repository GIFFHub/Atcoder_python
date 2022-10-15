def binary_search(ng, ok, table, target):
    if ok - ng == 1:
        return ok
    cen = (ng+ok)//2
    if table[cen] <= target:
        return binary_search(cen, ok, table, target)
    elif table[cen] > target:
        return binary_search(ng, cen, table, target)


H, W, rs, cs = map(int, input().split())

N = int(input())
dict_r = {} # 各行にある壁の列番号 （行がKey）
dict_c = {} # 各列にある壁の行番号　(列がKey)
for _ in range(N):
    r, c = map(int, input().split())
    if r in dict_r:
        dict_r[r].append(c)
    elif c in dict_c:
        dict_c[c].append(r)
    else:
        dict_r[r] = [c]
        dict_c[c] = [r]

for r_list, c_list in zip(dict_r.values(), dict_c.values()):
    r_list.sort()
    c_list.sort()

Q = int(input())

D = []
L = []
for _ in range(Q):
    d, l = input().split()
    D.append(d)
    L.append(int(l))

for i in range(Q):
    if D[i] == 'L':
        if cs == 1:
            break
        move = min(L[i], binary_search(-1, len(dict_r[rs]), dict_r[rs], cs)-cs)
        cs -= move

    if D[i] == 'R':
        if cs == W:
            break
        move = min(L[i], binary_search(-1, len(dict_r[rs]), dict_r[rs], cs) - cs)
        cs -= move
        cs += 1
    if D[i] == 'U':
        if rs == 0:
            break
        elif (rs-1, cs) in wall:
            break
        else:
            rs -= 1
    if D[i] == 'D':
        if rs == H:
            break
        elif (rs+1, cs) in wall:
            break
        else:
            rs += 1

    print(rs, cs)
