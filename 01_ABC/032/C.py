if __name__ == '__main__':
    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        S.append(int(input()))

    S_set = set(S)
    if 0 in S_set:
        print(len(S))
    else:
        R = [None]*N
        ans = 0
        for i in range(N):
            mul = 1
            if i == 0:
                R[i] = 0
            else:
                R[i] = R[i-1]

            while R[i] < N and mul * S[R[i]] <= K:
                mul *= S[R[i]]
                R[i] += 1

            ans = max(ans, R[i]-i)

        print(ans)

