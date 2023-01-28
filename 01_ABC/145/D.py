from scipy.special import comb


if __name__ == '__main__':
    X, Y = map(int, input().split())
    ans = 0
    if (X+Y) % 3 == 0:
        # (X, Y)にはn回移動してたどり着く
        n = (X+Y) // 3
        # x方向にa回、y方向にb回移動したとする
        a = X-n
        b = n-a
        ans = comb(a+b, b, exact=True)

    print(ans)






