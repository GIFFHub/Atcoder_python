

if __name__ == '__main__':
    N, D = map(int, input().split())
    T = list(map(int, input().split()))
    tmp = T[0]
    for i in range(1, N):
        if T[i] - tmp <= D:
            print(T[i])
            break
        tmp = T[i]
    else:
        print(-1)
