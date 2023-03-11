

if __name__ == '__main__':
    A, B, K = map(int, input().split())

    if K > A:
        K -= A
        A = 0
        B -= K
        B = max(0, B)
    else:
        A -= K

    print(A, B)