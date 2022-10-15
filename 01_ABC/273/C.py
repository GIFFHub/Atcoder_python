from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)

for a in A:
    d[a] += 1

A_set = set(A)
A_set_list = list(A_set)
A_set_list.sort()
len_A_set_list = len(A_set_list)
#print(A)
#print(A_set_list)
#print(A_set_list[-3])

for k in range(N):
    if k+1 <= len_A_set_list:
        #print(A_set_list[-(k+1)]) # ちょうどK種類のAi
        tmp_Ai = A_set_list[-(k+1)]
        #print(A.count(tmp_Ai))
        print(d[tmp_Ai])
    else:
        print(0)