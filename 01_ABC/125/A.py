

if __name__ == '__main__':
    A, B, T = map(int, input().split())

    time = 0
    ans = 0
    while True:
        time += A
        if time > T + 0.5:
            break

        ans += B

    print(ans)


