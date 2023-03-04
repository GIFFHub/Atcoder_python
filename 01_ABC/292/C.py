

def prime_factorize(N):
    # 答えを表す可変長配列
    res = []

    # √N まで試し割っていく
    for p in range(2, N):
        # p * p <= N の範囲でよい
        if p * p > N:
            break

        # N が p で割り切れないならばスキップ
        if N % p != 0:
            continue

        # N の素因数 p に対する指数を求める
        e = 0
        while N % p == 0:
            # 指数を 1 増やす
            e += 1

            # N を p で割る
            N //= p

        # 答えに追加
        res.append((p, e))

    # 素数が最後に残ることがありうる
    if N != 1:
        res.append((N, 1))

    return res


if __name__ == '__main__':
    N = int(input())
    ans = 0
    for i in range(1, N):
        AB = i
        CD = N-i
        AB_pri = prime_factorize(AB)
        AB_ans = 1
        for ab in AB_pri:
            AB_ans *= ab[1]+1
        CD_ans = 1
        CD_pri = prime_factorize(CD)
        for cd in CD_pri:
            CD_ans *= cd[1]+1

        ans += AB_ans * CD_ans

    print(ans)