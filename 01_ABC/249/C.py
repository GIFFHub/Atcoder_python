import string
from itertools import product

N, K = map(int, input().split())

S = []
for _ in range(N):
    S.append(set(input()))

alphabet = string.ascii_lowercase

ans = 0
for pro in product((0, 1), repeat=N):
    tmp = [0] * 27
    for flg_index, flg in enumerate(pro):
        if flg:
            alp_num = 0
            s = S[flg_index]
            for alp_index, alp in enumerate(alphabet):
                if alp in s:
                    tmp[alp_index] += 1
    ans = max(ans, tmp.count(K))

print(ans)


