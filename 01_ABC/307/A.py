

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))

    cnt = 0
    tmp = 0
    ans = []
    for a in A:
        tmp += a
        cnt += 1
        if cnt % 7 == 0:
            ans.append(tmp)
            tmp = 0
            cnt = 0

    print(*ans)







