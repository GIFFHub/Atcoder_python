

if __name__ == '__main__':
    A, B, C = map(int, input().split())

    if A > B:
        print('Takahashi')
    elif A < B:
        print('Aoki')
    else:
        if C == 1:
            print('Takahashi')
        else:
            print('Aoki')
