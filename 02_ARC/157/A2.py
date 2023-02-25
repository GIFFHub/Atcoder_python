
if __name__ == '__main__':
    N, A, B, C, D = map(int, input().split())
    if B == 0 and C == 0 and A > 0 and D > 0:
        print('No')
    elif abs(B-C) <= 1:
        print('Yes')
    else:
        print('No')





