

if __name__ == '__main__':
    H, N = map(int, input().split())
    A = list(map(int, input().split()))
    if H > sum(A):
        print('No')
    else:
        print('Yes')