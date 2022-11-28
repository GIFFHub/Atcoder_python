

if __name__ == '__main__':
    N = int(input())
    A = []
    B = []
    T = [[] for _ in range(N)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
        T[a-1].append(b-1)
        T[b-1].append(a-1)

    for t in T:
        if len(t) == N-1:
            print('Yes')
            break
    else:
        print('No')
