

if __name__ == '__main__':
    N = int(input())

    t = set()
    ans = 0
    for i in range(N):
        S = input()
        if S in t:
            continue
        elif S[::-1] in t:
            continue
        else:
            t.add(S)
            ans += 1

    print(ans)


