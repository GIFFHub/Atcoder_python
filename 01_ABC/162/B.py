

if __name__ == '__main__':
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        if i % 15 == 0:
            pass
        elif i % 5 == 0:
            pass
        elif i % 3 == 0:
            pass
        else:
            ans += i

    print(ans)