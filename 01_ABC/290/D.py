

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N, D, K = map(int, input().split())
        if D > N:
            D %= N
        '''
        ・一度塗れたら、最後までずっと塗れる
        '''

        T = [False] * N
        T[0] = True
        # 塗った回数
        cnt = 1
        if cnt == K:
            print(0)
            continue

        start_point = 0
        second_point = (start_point + D) % N
        while True:
            # 2箇所目
            # 2箇所目が塗られている限り
            if T[second_point]:
                second_point = (second_point + 1) % N
            cnt += 1
            if cnt == K:
                ans = second_point
                break
            # 今回second_pointを起点にして塗る量だけ足したらK番目を超える場合
            # 次に塗れる回数
            amount = (N-second_point-1) // D
            if K <= cnt + amount:
                ans = second_point + (K-cnt)*D
                break
            # 超えない場合
            else:
                cnt += amount
                second_point = (second_point + D*(amount+1)) % N
        print(ans)

