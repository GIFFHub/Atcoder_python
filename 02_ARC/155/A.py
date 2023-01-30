

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        S = input()
        len_S = len(S)
        if len_S == 1:
            print('Yes')
            continue

        if S == S[0]*len_S:
            print('Yes')
            continue

        if K == len_S:
            print('Yes')
            continue

        half = len_S //2
        rev = ''.join(reversed(S[-half:]))
        if S[:half] == rev:
            if K % len_S == 0:
                print('Yes')
                continue

        if (K - len_S) % (2*len_S) == 0 and K >= len_S:
            print('Yes')
            continue

        if S == S[:K] * (len_S // K):
            print('Yes')
            continue

        if len_S % 3 == 0:
            idx = len_S // 3
            front = S[:idx]
            middle = S[idx:-idx]
            back = S[-idx:]
            middle = ''.join(reversed(middle))
            if front == back == middle:
                if idx == K:
                    print('Yes')
                    continue

                else:
                    if (K - idx) % (2*idx) == 0 and K >= idx:
                        print('Yes')
                        continue
                    else:
                        print('No')
                        continue
            else:
                print('No')
                continue

        else:
            print('No')


