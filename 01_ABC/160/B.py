

if __name__ == '__main__':
    X = int(input())
    ans = 0
    M = X // 500
    ans += M * 1000
    X -= M*500
    m = X // 5
    ans += m * 5
    print(ans)