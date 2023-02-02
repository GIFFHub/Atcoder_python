

if __name__ == '__main__':
    N = list(input())
    len_N = len(N)
    for i in range(len(N)):
        N[i] = int(N[i])
    N_sum = sum(N)
    cnt = 0
    ans = -1
    if N_sum % 3 == 0:
        ans = 0
    elif N_sum % 3 == 1:
        cnt = 0
        for n in N:
            if n % 3 == 1:
                if len_N > 1:
                    ans = 1
                    break

            elif n % 3 == 2:
                cnt += 1
                if cnt == 2:
                    if len_N > 2:
                        ans = 2
    else:
        cnt = 0
        for n in N:
            if n % 3 == 1:
                cnt += 1
                if cnt == 2:
                    if len_N > 2:
                        ans = 2
            elif n % 3 == 2:
                if len_N > 1:
                    ans = 1
                    break
    print(ans)




