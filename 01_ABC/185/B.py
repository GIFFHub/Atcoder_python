

if __name__ == '__main__':
    N, M, T = map(int, input().split())
    max_N = N
    current_time = 0
    for _ in range(M):
        a, b = map(int, input().split())
        N -= (a - current_time)
        N = max(N, 0)
        if N <= 0:
            print('No')
            break
        N += (b-a)
        N = min(N, max_N)
        current_time = b
    else:
        N -= (T-current_time)
        if N <= 0:
            print('No')
        else:
            print('Yes')



