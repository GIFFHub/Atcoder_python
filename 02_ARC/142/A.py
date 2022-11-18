

if __name__ == '__main__':
    N, K = map(int, input().split())

    K_str = str(K)
    K_str_rev = K_str[::-1]
    K_rev = int(K_str_rev)
    if K_str[-1] == 0:
        cnt = 0
    elif K_str == K_str_rev:
        tmp = K
        cnt = 0
        while True:
            if N >= tmp:
                cnt += 1
                tmp *= 10
            else:
                break
    elif K > K_rev:
        cnt = 0
    else:
        tmp = K_rev
        cnt = 0
        while True:
            if N >= tmp:
                cnt += 1
                tmp *= 10
            else:
                break
        tmp = K
        while True:
            if N >= tmp:
                cnt += 1
                tmp *= 10
            else:
                break
    print(cnt)


