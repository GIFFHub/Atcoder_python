from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    for i in range(1, N+1):
        if i in d:
            print(d[i])
        else:
            print(0)


