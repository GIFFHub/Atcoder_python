

if __name__ == '__main__':
    N, L, R = map(int, input().split())
    A_list = list(map(int, input().split()))

    for i in range(N):
        A = A_list[i]
        if A > R:
            print(R)
        elif A < L:
            print(L)
        else:
            print(A)


        
