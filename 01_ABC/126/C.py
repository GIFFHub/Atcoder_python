import math

if __name__ == '__main__':
    N, K = map(int, input().split())
    # K以上になるまでコインが表が出続ける確率

    ans = 0
    for x in range(1, N+1):
        point = x
        cnt = 0
        while point < K:
            point *= 2
            cnt += 1

        P = (1/N) * math.pow(1/2, cnt)
        ans += P

    print(ans)





