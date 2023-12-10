if __name__ == '__main__':
    N, D = map(int, input().split())
    W = list(map(int, input().split()))
    W.sort(reverse=True)

    T = [0] * D

    for i in range(N):
        index = T.index(min(T))
        T[index] += W[i]

    ave = sum(T) / len(T)
    ans = 0
    for j in range(D):
        ans += (T[j]-ave)**2
    ans /= D

    print(ans)


