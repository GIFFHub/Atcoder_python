

if __name__ == '__main__':
    A, B = map(int, input().split())

    ans = 0
    cnt = 0
    while True:
        if A == B:
            break
        if A == 1 or B == 1:
            ans += abs(B-A)
            break

        if A > B:
            ans += A // B
            A %= B
            if A == 0:
                ans -= 1
                break
        elif B > A:
            ans += B // A
            B %= A
            if B == 0:
                ans -= 1
                break
    print(ans)