

if __name__ == '__main__':
    N, Q = map(int, input().split())
    S = input()
    T = [0] * N
    tmp = 0

    for i in range(N-1):
        if S[i] == S[i+1]:
            tmp += 1
        T[i+1] = tmp

    for _ in range(Q):
        l, r = map(int, input().split())
        ans = T[r-1] - T[l-1]
        print(ans)


