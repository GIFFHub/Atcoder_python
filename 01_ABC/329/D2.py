
from collections import defaultdict

if __name__ == '__main__':
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)

    prev = 0
    for a in A:
        d[a] += 1
        if prev in d:
            if d[prev] > d[a]:
                print(prev)
            elif d[prev] < d[a]:
                print(a)
                prev = a
            else:
                if prev > a:
                    print(a)
                    prev = a
                else:
                    print(prev)
        else:
            print(a)
            prev = a




