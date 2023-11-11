
if __name__ == '__main__':
    N, D, P = map(int, input().split())
    F = list(map(int, input().split()))

    F.sort(reverse=True)

    sum_F = sum(F)
    # money_list[i] : i日分が無料になった場合の最小合計料金
    money_list = [sum_F]*(N+1)
    for i in range(1, N+1):
        money_list[i] = money_list[i-1] - F[i-1]

    ans = sum_F
    # 周遊パス購入枚数でループ
    for m in range(N+1):
        if m*D <= N:
            money = m*P + money_list[m*D]
        else:
            money = m*P
        ans = min(ans, money)

    print(ans)







