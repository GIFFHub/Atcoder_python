

if __name__ == '__main__':
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if 1 <= i <= 9:
            ans += 1
        elif 100 <= i <= 999:
            ans += 1
        elif 10000 <= i <= 99999:
            ans += 1

    print(ans)
