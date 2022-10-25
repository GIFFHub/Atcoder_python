# 尺取り法
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
        mul = 1
        for i in range(N):
            if i == 0:
                R[i] = 0
            else:
                R[i] = R[i-1]

            # R[i]をぎりぎりいけるかこれから判定する
            while R[i] < N and mul * S[R[i]] <= K:
                # R[i] がいけることがわかった
                # 次の準備
                mul *= S[R[i]]
                R[i] += 1

            # この時点でR[i]はぎりぎりいけないライン
            ans = max(ans, R[i]-i)

            # 今回は、差分を取るしゃくとりとは違い、一つ目からNGの可能性がある
            # よって、その場合は、iも次に行く時に、R[i]も次に行く必要がある。
            if R[i] == i:
                R[i] += 1
            else:
                # この時にmulの値は、ギリギリいけなかった時の値
                # よって、しゃくとりで次に行く時、S[i]（最初の乗算）を割って次に行く。（次も行けるかどうかはわからない）
                mul /= S[i]

        print(ans)
