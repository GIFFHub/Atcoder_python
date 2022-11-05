
from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    d = defaultdict(int)

    for _ in range(N):
        d[input()] += 1

    print(max(d, key=d.get))
