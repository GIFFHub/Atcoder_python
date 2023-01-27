

if __name__ == '__main__':
    N = int(input())
    A = [0] * N
    B = [0] * N
    T = []
    for i in range(N):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
        T.append((2*a+b, i))

    T.sort(reverse=True)

    t_vote = 0
    a_vote = sum(A)

    cnt = 0
    for t in T:
        cnt += 1
        t_vote += A[t[1]]+B[t[1]]
        a_vote -= A[t[1]]
        if t_vote > a_vote:
            print(cnt)
            break


    '''
    ・初期値
        ・高橋票：0
        ・青木票：sum(a)
    ・演説を行う
        ・高橋 +a+b
        ・青木 -a
    '''
