
if __name__ == '__main__':

    '''
    ・できるだけ多くのYグループをくっつけたい
    ・全体として大きな連続YYYYYを作成する必要はない
    ・限られたKの中でどれだけのYグループをくっつけられるかという問題
    ・とりあえず、それぞれのYグループがどれだけ離れているかを調べる
    '''

    N, K = map(int, input().split())
    S = input()
    ans = 0

    for i in range(1, N):
        if S[i-1] == 'Y' and S[i] == 'Y':
            ans += 1

    # あいまのXがそれぞれどのくらい続くか
    # 先頭がYの場合、0から始まる
    # 後ろがYの場合、0で終わる
    T_X = []
    cnt = 0
    flg = 0
    for i in range(N):
        if S[i] == 'X':
            cnt += 1
            flg = 0
        else:
            if flg == 0:
                T_X.append(cnt)
                cnt = 0
                flg = 1
    T_X.append(cnt)

    len_T = len(T_X)
    if len_T == 1:
        ans = max(0, K-1)
    else:
        P_X = T_X[1:-1].copy()
        P_X.sort()
        for p in P_X:
            if p <= K:
                K -= p
                ans += p+1
            else:
                ans += K
                break
        else:
            # 先頭の連続XをYに変える
            if K > 0:
                if K < T_X[0]:
                    ans += K
                else:
                    K -= T_X[0]
                    ans += T_X[0]
                    if K > 0:
                        if K < T_X[-1]:
                            ans += K
                        else:
                            K -= T_X[-1]
                            ans += T_X[-1]
                            if K > 0:
                                # 全てYにして残り操作がK回残っている場合
                                # Yの元々の連続部分を調べる（連続部分をXに変えるほうがダメージが少ない）
                                T_Y = []
                                cnt = 0
                                flg = 0
                                for i in range(N):
                                    if S[i] == 'Y':
                                        cnt += 1
                                        flg = 0
                                    else:
                                        if flg == 0:
                                            T_Y.append(cnt)
                                            cnt = 0
                                            flg = 1
                                T_Y.append(cnt)

                                if K < T_Y[0]:
                                    ans -= K
                                else:
                                    K -= T_Y[0]
                                    ans -= T_Y[0]
                                    if K > 0:
                                        if K < T_Y[-1]:
                                            ans -= K
                                        else:
                                            K -= T_Y[-1]
                                            ans -= T_Y[-1]
                                            if K > 0:
                                                P_Y = T_Y[1:-1].copy()
                                                P_Y.sort(reverse=True)
                                                for p in P_Y:
                                                    if K == 0:
                                                        break
                                                    if p <= K:
                                                        K -= p
                                                        ans -= (p+1)
                                                    else:
                                                        ans -= K+1
                                                        break
    print(max(0, ans))
