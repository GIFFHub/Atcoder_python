

if __name__ == '__main__':

    P = int(input())
    for _ in range(P):
        N, K = map(int, input().split())
        S = input()
        rS = ''.join(reversed(S))
        K %= (2*N)
        l = min(K, N)
        top = rS[:l]
        down = rS[-l:]
        overlap = 2*l-K
        if top[K-overlap:] != down[:overlap]:
            print('No')
            continue
        T = top + down[overlap:]

        half = len(T+S)//2
        ST = S + T
        TS = T + S
        if ST[:half] == ST[half:] and TS[:half] == TS[half:]:
            print('Yes')
        else:
            print('No')


