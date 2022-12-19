

if __name__ == '__main__':
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    every = 0
    while N <= K:
        every += K//N
        K = K % N

    B = []
    for i, a in enumerate(A):
        B.append([i, a, 0])

    B.sort(key=lambda x: x[1])

    for j in range(K):
        B[j][2] += 1

    B.sort(key=lambda x: x[0])

    for b in B:
        print(b[2]+every)






