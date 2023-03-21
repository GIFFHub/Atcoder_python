

if __name__ == '__main__':

    A, B = map(int, input().split())
    m = 1
    ans = 0
    while m < B:
        m += A-1
        ans += 1

    print(ans)


