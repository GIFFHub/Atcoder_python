

if __name__ == '__main__':
    N = int(input())
    ans = 0
    cnt = 0
    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if i*j >= N:
                break
            ans += 1

    ans *= 2

    for i in range(1, N+1):
        if i**2 >= N:
            break
        ans += 1

    print(ans)
