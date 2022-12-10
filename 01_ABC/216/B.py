

if __name__ == '__main__':
    N = int(input())
    S = []
    T = []
    d = dict()
    s = set()
    for _ in range(N):
        s, t = input().split()
        if s not in d:
            d[s] = [t]
        else:
            d[s].append(t)

    for ds in d:
        if len(d[ds]) != len(set(d[ds])):
            print('Yes')
            break
    else:
        print('No')



