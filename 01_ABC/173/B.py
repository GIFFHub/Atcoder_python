from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        d[input()] += 1

    T = ['AC', 'WA', 'TLE', 'RE']

    for t in T:
        if t in d:
            print(t, 'x', d[t])
        else:
            print(t,'x', 0)



