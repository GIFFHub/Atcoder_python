

if __name__ == '__main__':
    N = int(input())
    T = []
    for _ in range(N):
        a, b = map(int, input().split())
        T.append((a, b))
    T = sorted(T, key=lambda x: x[1])

    used_time = 0
    for i in range(N):
        used_time += T[i][0]
        if used_time > T[i][1]:
            print('No')
            break
    else:
        print('Yes')

