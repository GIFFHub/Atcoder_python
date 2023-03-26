

if __name__ == '__main__':
    N = int(input())
    A = []
    for _ in range(N):
        A.append(int(input()))

    B = A.copy()
    B.sort(reverse=True)
    M1 = B[0]
    M2 = B[1]

    for a in A:
        if a == M1:
            print(M2)
        else:
            print(M1)

