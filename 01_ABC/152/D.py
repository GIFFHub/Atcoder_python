

if __name__ == '__main__':
    N = int(input())

    # cnt[i][j] : 先頭がiで末尾がjであり、N以下である値の個数
    cnt = [[0] * 9 for _ in range(9)]
    ans = 0
    for num in range(1, N+1):
        str_num = str(num)
        top = str_num[0]
        btm = str_num[-1]
        if btm != '0':
            cnt[int(top)-1][int(btm)-1] += 1

    ans = 0
    for a in range(9):
        for b in range(9):
            ans += cnt[a][b]*cnt[b][a]

    print(ans)



