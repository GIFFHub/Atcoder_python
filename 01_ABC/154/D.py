

if __name__ == '__main__':
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    # 各サイコロの出る目の期待値を事前に求める
    P_K = [0]*N
    for i in range(N):
        P_K[i] = (P[i]*(1+P[i])) / (2*P[i])

    ans = sum(P_K[:K])
    tmp = ans
    for i in range(N-K):
        tmp -= P_K[i]
        tmp += P_K[i+K]
        ans = max(ans, tmp)

    print(ans)

