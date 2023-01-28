

if __name__ == '__main__':
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if '7' not in str(i):
            if '7' not in oct(i):
                ans += 1

    print(ans)


