

if __name__ == '__main__':
    N, X = map(int, input().split())
    A = set(map(int, input().split()))

    if X in A:
        print('Yes')
    else:
        print('No')
