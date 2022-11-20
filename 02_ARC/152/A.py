

if __name__ == '__main__':
    N, L = map(int, input().split())
    A = list(map(int, input().split()))

    '''
    考察
    ・最悪の座り方（１個ずつ開ける）で座っていき、
    　座れるところがない場合は空いているところを埋めるスタイルでいく
    ・上記の座り方して、最後まで到達した時に、
    　２人組が残っていたらOUT
    '''
    # 残りの座れる席
    rest = L
    for i in range(N):
        if rest > A[i]:
            rest -= (A[i]+1)
        elif rest == A[i]:
            rest -= A[i]
        else:
            # i番目の人以降は隙間の１席に座るしかない
            break
    else:
        print('Yes')
        exit()

    if A[i:].count(2) > 0:
        print('No')
    else:
        print('Yes')




