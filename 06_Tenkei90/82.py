

if __name__ == '__main__':
    L, R = map(int, input().split())
    K = 10**9 + 7

    # Lの桁数
    L_keta = len(str(L))
    R_keta = len(str(R))

    ans = 0
    while L_keta <= R_keta:
        syokou = L
        makkou = min(int('9'*L_keta), R)
        kousuu = makkou - syokou + 1
        souwa = kousuu * (syokou + makkou) // 2

        ans += L_keta * souwa
        ans %= K

        L_keta += 1
        L = makkou + 1
    print(ans)











