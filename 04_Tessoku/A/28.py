

if __name__ == '__main__':
    N = int(input())
    T = []
    A = []
    ans = 0
    for _ in range(N):

        t, a = input().split()
        '''
        T.append(t)
        A.append(a)
        '''
        a = int(a)
        if t == '+':
            ans += a
        elif t == '-':
            ans -= a
        elif t == '*':
            ans *= a
        ans %= 10000
        print(ans)



