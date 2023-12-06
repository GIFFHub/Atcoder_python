if __name__ == '__main__':
    N = int(input())
    A, B, C = map(int, input().split())

    ans = 10000
    for a in range(N//A+1):
        for b in range(N//B+1):
            if a + b > 10000:
                break
            a_money = A * a
            b_money = B * b
            c_money = N - (a_money + b_money)
            if c_money < 0:
                continue
            if c_money % C != 0:
                continue
            else:
                c = c_money // C
                ans = min(ans, a+b+c)
    print(ans)




