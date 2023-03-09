
from collections import defaultdict
if __name__ == '__main__':
    N, M = map(int, input().split())
    d = defaultdict(int)
    s = set()
    Problem = [False]*N
    penalty = [0]*N
    penalty_num = 0
    AC_num = 0
    for _ in range(M):
        p, S = input().split()
        p = int(p)
        if S == 'WA':
            penalty[p-1] += 1
        else:
            if not Problem[p-1]:
                Problem[p-1] = True
                AC_num += 1
                penalty_num += penalty[p-1]
    print(AC_num, penalty_num)






