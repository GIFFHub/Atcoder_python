

if __name__ == '__main__':
    A, B = map(int, input().split())
    if (A+B)%2 == 0:
        print((A+B)//2)
    else:
        print('IMPOSSIBLE')