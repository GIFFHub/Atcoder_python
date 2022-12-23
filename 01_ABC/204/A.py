

if __name__ == '__main__':
    x, y = map(int, input().split())
    if x == y:
        ans = x
    else:
        ans = 3-(x+y)

    print(ans)