h, w = map(int, input().split(' '))
ls = []
row_sum = [0] * h
col_sum = [0] * w
for i in range(h):
    val = list(map(int, input().split(' ')))
    ls.append(val)
    row_sum[i] = sum(val)
    for j in range(w):
        col_sum[j] += val[j]
for i, s in enumerate(ls):
    val = []
    for j, t in enumerate(s):
        val.append(str(row_sum[i] + col_sum[j] - t))
    print(' '.join(val))