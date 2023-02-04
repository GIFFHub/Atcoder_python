

if __name__ == '__main__':
    X, Y, A, B = map(int, input().split())
    K = 0
    '''
    ・A倍するのとB足すので、より大きくならない方を選択し続ける
    ・
    ・
    '''
    while True:
        if X*A < X+B:
            if X*A <= Y:
                X *= A
                K += 1
            else:
                break
        else:
            break
    R = max(0, Y-X) // B
    X += R*B
    K += R
    if X == Y:
        K -= 1

    print(K)






