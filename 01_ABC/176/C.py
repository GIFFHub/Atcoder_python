

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    tmp = 0
    ans = 0
    for a in A:
        if a < tmp:
            ans += tmp-a
        else:
            tmp = a

    print(ans)



