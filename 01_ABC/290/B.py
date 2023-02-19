

if __name__ == '__main__':
    N, K = map(int, input().split())
    S = input()

    T = []
    cnt = 0
    for s in S:
        if s == 'o':
            cnt += 1
            if cnt <= K:
                T.append('o')
            else:
                T.append('x')
        else:
            T.append('x')

    print(''.join(T))


