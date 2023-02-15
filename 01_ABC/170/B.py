

if __name__ == '__main__':
    X, Y = map(int, input().split())
    min_num = 2*X
    max_num = 4*X
    if min_num <= Y <= max_num and Y%2 == 0:
        print('Yes')
    else:
        print('No')