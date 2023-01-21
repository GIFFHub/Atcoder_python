

if __name__ == '__main__':
    N = int(input())
    S = input()
    N = int(N)
    ans = []
    flg = 0
    for i in range(N):
        if flg != 0:
            flg -= 1
            continue
        if S[i] == 'n':
            if i != N-1:
                if S[i+1] == 'a':
                    ans.append('nya')
                    flg = 1
                else:
                    ans.append(S[i])
            else:
                ans.append(S[i])
        else:
            ans.append(S[i])


    print(''.join(ans))



