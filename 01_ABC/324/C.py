if __name__ == '__main__':
    N, T = input().split()
    N = int(N)
    K = []
    len_T = len(T)
    for i in range(1, N+1):
        S = input()

        if S == T:
            K.append(i)
        else:
            flg = 0
            len_S = len(S)
            # 一文字挿入した可能性があるもの
            if len_T == len_S + 1:
                for j in range(len_S):
                    if flg == 0:
                        if S[j] != T[j]:
                            if S[j] == T[j+1]:
                                flg = 1
                            else:
                                break
                    else:
                        if S[j] != T[j+1]:
                            break
                else:
                    K.append(i)
            # 一文字変更した可能性があるもの
            elif len_T == len_S:
                for j in range(len_S):
                    if flg == 0:
                        if S[j] != T[j]:
                            flg = 1
                    else:
                        if S[j] != T[j]:
                            break
                else:
                    K.append(i)
            # 一文字削除した可能性があるもの
            else:
                for j in range(len_T):
                    if flg == 0:
                        if S[j] != T[j]:
                            if S[j+1] == T[j]:
                                flg = 1
                            else:
                                break
                    else:
                        if S[j+1] != T[j]:
                            break
                else:
                    K.append(i)


    print(len(K))
    print(*K)

