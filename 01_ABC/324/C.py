if __name__ == '__main__':
    N, T = input().split()
    N = int(N)

    len_T = len(T)
    ans = []
    for i in range(N):
        S = input()

        if S == T:
            ans.append(i+1)
        else:
            len_S = len(S)

            if len_S + 1 == len_T:
                for j in range(len_S):
                    if S[j] != T[j]:
                        if T[:j] + T[j+1:] == S:
                            ans.append(i+1)
                            break
                        else:
                            break
                else:
                    ans.append(i+1)

            elif len_S - 1 == len_T:
                for j in range(len_T):
                    if S[j] != T[j]:
                        if S[:j] + S[j+1:] == T:
                            ans.append(i+1)
                            break
                        else:
                            break
                else:
                    ans.append(i+1)

            elif len_S == len_T:
                flg = 0
                for j in range(len_S):
                    if S[j] != T[j]:
                        if flg == 0:
                            flg = 1
                        else:
                            break
                else:
                    ans.append(i+1)
    print(len(ans))
    print(*ans)






