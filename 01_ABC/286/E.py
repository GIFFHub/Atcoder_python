

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    d = dict()
    for i in range(N):
        for j, s in enumerate(input()):
            if s == 'Y':
                if i+1 in d:
                    d[i+1].append(j+1)
                else:
                    d[i+1] = [j+1]

    for _ in range(int(input())):
        u, v = map(int, input().split())

