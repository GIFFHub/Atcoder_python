from collections import defaultdict

if __name__ == '__main__':
    N, Q = map(int, input().split())
    d = defaultdict(int)
    s = set()
    for _ in range(Q):
        event = list(map(int, input().split()))
        if event[0] == 1:
            d[event[1]] += 1
            if d[event[1]] == 2:
                s.add(event[1])
        elif event[0] == 2:
            d[event[1]] += 2
            s.add(event[1])
        else:
            if event[1] in s:
                print('Yes')
            else:
                print('No')