

if __name__ == '__main__':
    X, Y = map(int, input().split())
    ans = (Y-X)//10
    if (Y-X)%10 > 0:
        ans += 1
    print(max(0, ans))