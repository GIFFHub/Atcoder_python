import numpy as np


def cal_sum(t):
    if t == N:
        return t
    elif t > N:
        return 0
    else:
        t_num = N//t
        t_last = t*t_num
        return t_num*(t+t_last)//2


if __name__ == '__main__':
    N, A, B = map(int, input().split())
    C = np.lcm(A, B)

    '''
    初項1公差1項数Nの数列の和
    ー    初項A公差A項数?の数列の和
    ー    初項B公差B項数?の数列の和
    ＋    初項C公差C項数?の数列の和（CはAとBの最小公倍数）
    '''

    N_sum = N*(1+N)//2
    A_sum = cal_sum(A)
    B_sum = cal_sum(B)
    C_sum = cal_sum(C)

    ans = N_sum - A_sum - B_sum + C_sum

    print(ans)



