

if __name__ == '__main__':
    S = input()
    T = input()

    len_S = len(S)
    len_T = len(T)

    ans = 1000
    for i in range(len_S-len_T+1):
        S2 = S[i:i+len_T]
        cnt = 0
        for j in range(len_T):
            if T[j] != S2[j]:
                cnt += 1
        ans = min(ans, cnt)

    print(ans)
