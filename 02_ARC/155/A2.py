

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        S = input()
        rS = ''.join(reversed(S))
        K = K % (2*N)

        l = min(K, N)
        top = rS[:l]
        down = rS[-l:]
        overlap = 2*l-K
        if top[K-overlap:] == down[:overlap]:
            print('Yes')
        else:
            print('No')



