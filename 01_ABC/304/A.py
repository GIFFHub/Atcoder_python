if __name__ == '__main__':

    N = int(input())
    S = []
    A = []
    d = dict()
    for _ in range(N):
        s, a = input().split()
        a = int(a)
        A.append(a)
        d[a] = s

    min_A = min(A)

    A_2 = A + A

    for i in range(N):
        if A_2[i] == min_A:
            for j in range(i, i+N):
                print(d[A_2[j]])
            break


