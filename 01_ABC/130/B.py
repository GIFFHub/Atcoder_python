

if __name__ == '__main__':
    N, X = map(int, input().split())
    L = list(map(int, input().split()))

    t = 0
    cnt = 0
    while t <= X:
        cnt += 1
        if cnt == N+1:
            break
        t = t + L[cnt-1]

    print(cnt)
