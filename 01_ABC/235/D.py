
def shift(t):
    t = str(t)
    if t[-1] != 0:
        return int(t[-1]+t[:-1])
    else:
        return t


if __name__ == '__main__':
    a, N = map(int, input().split())
    x = 1

    # Nをシフトして最小に
    # Nを半分に
    s = set()
    s.add(N)
    cnt = 0
    while True:
        cnt += 1
        if N == 1:
            print(cnt)
        if N % a == 0:
            N //= a
        else:
            N = shift(N)
            if N in s:
                print(-1)
                break
            else:
                s.add(N)




