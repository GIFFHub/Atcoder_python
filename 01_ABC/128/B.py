from collections import  defaultdict

if __name__ == '__main__':
    N = int(input())
    T = []
    d = defaultdict(int)
    for i in range(N):
        s, p = input().split()
        T.append((s, int(p), i))
        d[s] += 1

    T = sorted(T, key=lambda x: x[1], reverse=True)
    T = sorted(T, key=lambda x: x[0])

    for t in T:
        print(t[2]+1)

