
if __name__ == '__main__':
    X, Y = map(int, input().split())
    if Y > X:
        if Y-X >= 3:
            print('No')
        else:
            print('Yes')
    else:
        if X-Y >= 4:
            print('No')
        else:
            print('Yes')