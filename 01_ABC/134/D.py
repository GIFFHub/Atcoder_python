

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    T = [0]*N

    for i in range(N, 0, -1):
        x = i
        cnt = 1
        K = []
        while True:
            x *= cnt
            if x < N:
                K.append(x)
                cnt += 1
            else:
                break
        if len(K) == 1:
            T[i-1] = A[i-1]
        else:
            tmp = 0
            for y in K[1:]:
                tmp += T[y-1]
            T[i-1] = (A[i-1] + tmp) % 2

    ans = []
    for i, t in enumerate(T):
        if t == 1:
            ans.append(i+1)
    print(len(ans))
    print(*ans)


