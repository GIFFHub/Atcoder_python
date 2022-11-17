def func(x):
    str_x = str(x)
    tmp = 0
    for a in str_x:
        tmp += int(a)
    return tmp


if __name__ == '__main__':
    N = int(input())
    '''
    考察
    ・求めるのは最大のMに対する最小のx
    ・f(x) = N : xを構成する各桁の和がN（いくらでもある）
    ・f(2x) = M : 2xを構成する各桁の和がN（順番入れ替えればいっぱいある）
        →Mが最大：2xを
    ・Mを最大にしたいなら、2xは8888にしたいから、できればxは4444がいい？
    ・x:10
    442:10
    884:20
    '''

    if N >= 4:
        s = N//4
        rem = N%4

        M = 8*s + 2*rem
        if rem == 0:
            x = '4'*s
        else:
            x = str(rem) + '4'*s

    else:
        M = 2*N
        x = N

    print(M)
    print(x)


