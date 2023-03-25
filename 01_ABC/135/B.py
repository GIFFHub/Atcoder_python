

if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split()))
    cnt = 0
    for i, p in enumerate(P):
        if p != i+1:
            cnt += 1

    if cnt > 2:
        print('NO')
    else:
        print('YES')