
'''
方針：同じ行で内側に移動する二者が移動する方向と反対側にいれば衝突する

'''

# input
N = int(input())
X = []
Y = []
for _ in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)
S = input()

# 同じ行にいる二者を調べる
Y_set = set()
Y_kouho = {}
for i in range(N):
    # 同じ行の人がすでに検出されている場合
    if Y[i] not in Y_set:
        Y_set.add(Y[i])
        # その人のindexとx位置を記録する
        # key:x位置, value:index
        Y_kouho[Y[i]] = [i]
    else:
        Y_kouho[Y[i]].append(i)


for indices in Y_kouho.values():
    if len(indices) == 1:
        continue
    else:
        left_pos = 10 ** 9
        right_pos = 0
        for index in indices:
            # 右向きに動く一番左にいる人を記録(left_pos)
            if S[index] == 'R':
                left_pos = min(left_pos, X[index])
            elif S[index] == 'L':
                right_pos = max(right_pos, X[index])

        if left_pos < right_pos:
            print('Yes')
            break
else:
    print('No')

