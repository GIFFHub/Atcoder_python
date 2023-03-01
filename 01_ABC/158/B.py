

if __name__ == '__main__':
    N, A, B = map(int, input().split())

    AB_num = N // (A+B)
    rem = N % (A+B)
    rem = min(rem, A)
    ans = AB_num*A + rem

    print(ans)
