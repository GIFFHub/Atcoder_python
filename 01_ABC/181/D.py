from collections import defaultdict

if __name__ == '__main__':
    S = input()
    len_S = len(S)
    '''
    ・8の倍数
    ・2で3回割れる
    ・
    ・
    '''
    K = []
    tmp = 0
    while True:
        tmp += 8
        if tmp > 99:
            K.append(tmp)
        if tmp > 999:
            break

    if len_S == 1:
        if S == '8':
            ans = 'Yes'
        else:
            ans = 'No'
    elif len_S == 2:
        if int(S) % 8 == 0:
            ans = 'Yes'
        elif int(S[1]+S[0]) % 8 == 0:
            ans = 'Yes'
        else:
            ans = 'No'
    else:
        d = defaultdict(int)
        for s in S:
            d[s] += 1
        for k in K:
            d_tmp = d.copy()
            for ks in str(k):
                d_tmp[ks] -= 1
            for ks in str(k):
                if d_tmp[ks] < 0:
                    break
            else:
                ans = 'Yes'
                break
        else:
            ans = 'No'

    print(ans)














