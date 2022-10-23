def func(k):
    '''

    :param k: 桁数
    :return: inputの桁数の全ての答えの合算
    '''
    rtn = 0
    for i in range(1, k+1):
        if i == 1:
            rtn += 45
        else:
            tmp = 1+9*10**(i-1)
            rtn += tmp*((tmp-1)//2)
        rtn %= T
    return rtn

def func2(k):
    if str_N[1:] == '0'*(len(str_N)-1):
        return 1
    if N % 2 == 1:
        tmp = (N-int('9'*(len(str_N)-1)))
        return (1+tmp)*(tmp//2) % T
    else:
        tmp = (N-int('9'*(len(str_N)-1)))
        return ((1+tmp)*(tmp//2) + tmp//2 + 1) % T


if __name__ == '__main__':
    N = int(input())
    T = 998244353
    ans = 0
    if N < 10:
        for i in range(1, N+1):
            ans += i
    else:
        str_N = str(N)
        ans += func(len(str_N)-1)
        ans += func2(len(str_N))
        ans %= T
    print(ans)