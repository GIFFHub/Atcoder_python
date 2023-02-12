

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    X = int(input())

    s = set()
    for b in B:
        s.add(b)


    '''
    dp[i] : i段目に登ることができるか否か
    '''

    dp = [False]*(X+1)
    dp[0] = True

    for i in range(X):
        if dp[i] and i not in s:
            for a in A:
                if i+a <= X:
                    dp[i+a] = True

    if dp[X]:
        print('Yes')
    else:
        print('No')
