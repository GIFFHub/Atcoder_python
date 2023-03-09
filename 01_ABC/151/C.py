
from collections import defaultdict
if __name__ == '__main__':
    N, M = map(int, input().split())
    d = defaultdict(int)
    s = set()
    penalty = 0
    for _ in range(M):
        p, S = input().split()
        if S == 'AC':
            s.add(p)
        else:
            if p not in s:
                penalty += 1
    print(len(s), penalty)



