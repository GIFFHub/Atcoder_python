if __name__ == '__main__':
    N = int(input())
    L = list(map(int, input().split()))

    max_L = max(L)
    sum_L = sum(L)

    if sum_L - max_L > max_L:
        print('Yes')
    else:
        print('No')


