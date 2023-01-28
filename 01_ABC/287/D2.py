import re

if __name__ == '__main__':
    S = input()
    T = input()
    len_T = len(T)

    Ts = []
    flg = 0 # 前が?なら1
    tmp = ''
    for t in T:
        if t == '?':
            if flg:
                tmp += t
            else:
                Ts.append(tmp)
                tmp = t
                flg = 1 - flg
        else:
            if flg:
                Ts.append(tmp)
                tmp = t
                flg = 1 - flg
            else:
                tmp += t

    Ts.append(tmp)

    print(Ts)
    while True:
        re.findall(Ts[0], S)


    '''
    for i, t in enumerate(T):
        if t == '?':
            if cnt == 0:
                Ts.append((T[tmp+1:i], cnt))
                tmp = i
            cnt += 1
        else:
            cnt = 0
        if i == len_T-1:
            if t != '?':
                Ts.append((T[tmp+cnt:i], cnt))

    print(Ts)
    '''

